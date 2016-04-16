import os
import csv

LOAD_HISTORY = os.path.join('Data', 'Global Energy Forecasting Competition', 'load_history.csv')
FORMATTED_LOAD_HISTORY = os.path.join('Data', 'Global Energy Forecasting Competition', 'formatted_load_history.csv')
HOURS = range(1,25)

with open(LOAD_HISTORY, 'r') as lh_contents, \
	 open(FORMATTED_LOAD_HISTORY, 'w') as flh_contents:
	# zone_id,year,month,day,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24
	lh_contents = csv.reader(lh_contents, delimiter=',', quotechar='"')
	header = next(lh_contents)
	print >> flh_contents, ','.join(['zone_id','year', 'month', 'day', 'hour', 'temperature'])
	for data in lh_contents:
		zone_id, year, month, day = data[:4]
		for hour in HOURS:
			print >> flh_contents, ','.join([zone_id, year, month, day, str(hour), data[3 + hour].replace(',', '')])
