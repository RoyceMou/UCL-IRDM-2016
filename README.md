# UCL-IRDM-2016

MLR.ipynb: The code used to run the MLR model.

arima.R: The code used to run the ARIMA model.

lstm.py: The code used to run the LSTM model

format_data_by_zone.py: Formats both load and temperature data by zone. Requires MLR_results.csv to fill in the missing data. Used to format the data for lstm.py.

format_load_history.py: Formats load history. Used to format the data for MLR.ipynb and arima.R.

format_temperature_history.py: Formats temperature history. Used to format the data for MLR.ipynb and arima.R.

fill_data.py: Uses MLR_results.csv to fill in the missing data. Used to format the data output by format_load_history.py for MLR.ipynb and arima.R.

formatted_load_history_with_trend.csv: Load history with the trend used to calculate the MLR model.

formatted_temperature_history_missingValue_to_average.csv: Temperature history with interpolated missing values.

MLR_results.csv: Full backcasted and forecasted data as per a sample kaggle submission. The backcasted data is used to format the data for lstm.py and arima.R.


The scripts are fairly straightforward to run on each respective platform. In lstm.py, the zone needs to be set since the runtime is fairly long compared to the other models. The folder structure is not completely replicated here to run these files from scratch. Changing the paths in the scripts will allow the scripts to be run.


