import os
import csv
import numpy as np
np.random.seed(1337)  # for reproducibility

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM
from keras.models import model_from_json

################################################################################
## Constants
################################################################################

LOAD_HISTORY_FOLDER = os.path.join('data', 'load_history')
TEMPERATURE_HISTORY_FOLDER = os.path.join('data', 'temperature_history')
model_file_template = os.path.join('history', 'model_')
weight_file_template = os.path.join('history', 'weights_')
zone = 1

################################################################################
## Preparing input data
################################################################################

tsteps = 1
tsteps_predict = 186
# test_split = 0.1

print 'Loading data for zone', zone
loads = []
with open(os.path.join(LOAD_HISTORY_FOLDER, str(zone)), 'r') as f:
    f = csv.reader(f, delimiter=',', quotechar='"')
    header = next(f)
    for data in f:
        zone_id, year, month, day, hour, load = data        
        if load:
            loads.append(float(load))

X, Y = zip(*((loads[i:i + tsteps], loads[i + tsteps - 1 + tsteps_predict]) 
             for i in range(len(loads) - (tsteps - 1 + tsteps_predict))))

X = np.asarray(X).reshape((len(X), tsteps, 1))
Y = np.asarray(Y).reshape((len(Y), 1))

X_train = X[:-tsteps_predict]
Y_train = Y[:-tsteps_predict]
X_test = X[-tsteps_predict:]
Y_test = Y[-tsteps_predict:]

print 'X_train shape:', X_train.shape
print 'Y_train shape:', Y_train.shape
print 'X_test shape:', X_test.shape
print 'Y_test shape:', Y_test.shape

################################################################################
## Creating model
################################################################################

batch_size = 1  # batch size needs to be a factor or len(X_train and X_test)
epochs = 15

print 'Creating Model'
model = Sequential()
model.add(LSTM(50,
               batch_input_shape=(batch_size, tsteps, 1),
               return_sequences=True))
model.add(LSTM(25,
               batch_input_shape=(batch_size, tsteps, 1),
               return_sequences=True))
model.add(LSTM(10,
               batch_input_shape=(batch_size, tsteps, 1),
               return_sequences=False))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop')

################################################################################
## Training and saving model
################################################################################

# print "Training..."
# model.fit(X_train, Y_train, nb_epoch=epochs, batch_size=batch_size,
#         verbose=1, shuffle=False)

print 'Training...'
for i in range(epochs):
    print 'Epoch', i + 1, '/', epochs
    model.fit(X_train,
              Y_train,
              batch_size=batch_size,
              verbose=1,
              nb_epoch=1,
              shuffle=False)
    model.reset_states()

file_initial = 0
while os.path.isfile(model_file_template + str(file_initial)):
    file_initial += 1
with open(model_file_template + str(file_initial), 'w') as f:
    f.write(model.to_json())
model.save_weights(weight_file_template + str(file_initial))

################################################################################
## Loading model
################################################################################

# file_initial = 0
# with open(model_file_template + str(file_initial)) as f:
#   model = model_from_json(f.read())
# model.load_weights(weight_file_template + str(file_initial))

################################################################################
## Evaluating model
################################################################################

score = model.evaluate(X_test, Y_test, batch_size=batch_size)

print 'Test score:', score