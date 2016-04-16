import os
import csv
import datetime

LOAD_HISTORY = os.path.join('data', 'load_history.csv')
TEMPERATURE_HISTORY = os.path.join('data', 'temperature_history.csv')
LOAD_HISTORY_FOLDER = os.path.join('data', 'load_history')
TEMPERATURE_HISTORY_FOLDER = os.path.join('data', 'temperature_history')

HOURS = range(1,25)


################################################################################
# Fill in backcasted data
################################################################################

backcasted_dates = dict()
with open(os.path.join('data', 'MLR_results.csv'), 'r') as f_m:
    f_m_contents = csv.reader(f_m, delimiter=',', quotechar='"')
    header = next(f_m_contents)
    for data in f_m_contents:
        day, hour, load, month, year, zone_id = data
        backcasted_dates[(zone_id, year, month, day, hour)] = load

################################################################################
# Split load history
################################################################################

with open(LOAD_HISTORY, 'r') as lh_contents:
	# zone_id,year,month,day,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24
	lh_contents = csv.reader(lh_contents, delimiter=',', quotechar='"')
	next(lh_contents)	# clear header
	header = ','.join(['zone_id','year', 'month', 'day', 'hour', 'load'])

	zones = range(1, 21)
	zone_handles = dict((zone, open(os.path.join(LOAD_HISTORY_FOLDER, str(zone)), 'w')) for zone in zones)

	for zone in zone_handles:
		print >> zone_handles[zone], header

	for data in lh_contents:
		zone_id, year, month, day = data[:4]
		for hour in HOURS:
			load = data[3 + hour].replace(',', '')
			if not load and datetime.date(int(year), int(month), int(day)) < datetime.date(2008, 6, 30):
				load = backcasted_dates[(zone_id, year, month, day, str(hour))]
			print >> zone_handles[int(zone_id)], \
				','.join([zone_id, year, month, day, str(hour), load])

	for zone in zone_handles:
		zone_handles[zone].close()

with open(TEMPERATURE_HISTORY, 'r') as th_contents:
	# station_id,year,month,day,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,h21,h22,h23,h24
	th_contents = csv.reader(th_contents, delimiter=',', quotechar='"')
	next(th_contents)	# clear header
	header = ','.join(['station_id','year', 'month', 'day', 'hour', 'temperature'])

	stations = range(1, 12)
	station_handles = dict((station, open(os.path.join(TEMPERATURE_HISTORY_FOLDER, str(station)), 'w')) 
					  for station in stations)

	for station in station_handles:
		print >> station_handles[station], header

	for data in th_contents:
		station_id, year, month, day = data[:4]
		for hour in HOURS:
			print >> station_handles[int(station_id)], \
				','.join([station_id, year, month, day, str(hour), data[3 + hour].replace(',', '')])

	for station in station_handles:
		station_handles[station].close()