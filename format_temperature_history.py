import os
import csv

TEMPERATURE_HISTORY = os.path.join('Data', 'Global Energy Forecasting Competition', 'temperature_history.csv')
FORMATTED_TEMPERATURE_HISTORY = os.path.join('Data', 'Global Energy Forecasting Competition', 'formatted_temperature_history.csv')
HOURS = range(1,25)

with open(TEMPERATURE_HISTORY, 'r') as th_contents, \
	 open(FORMATTED_TEMPERATURE_HISTORY, 'w') as fth_contents:
	th_contents = csv.reader(th_contents)
	# station_id,year,month,day,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24
	header = next(th_contents)
	print >> fth_contents, ','.join(['station_id','year', 'month', 'day', 'hour', 'temperature'])
	for data in th_contents:
		station_id, year, month, day = data[:4]
		for hour in HOURS:
			print >> fth_contents, ','.join([station_id, year, month, day, str(hour), data[3 + hour]])