import csv
import datetime

backcasted_dates = dict()
with open('MLR_results.csv', 'r') as f_m:
    f_m_contents = csv.reader(f_m, delimiter=',', quotechar='"')
    header = next(f_m_contents)
    for data in f_m_contents:
        day, hour, load, month, year, zone_id = data
        backcasted_dates[(zone_id, year, month, day, hour)] = load

with open('formatted_load_history.csv', 'r') as f_lh, open('formatted_full_load_history.csv', 'w') as f_flh:
    f_lh_contents = csv.reader(f_lh, delimiter=',', quotechar='"')
    header = next(f_lh_contents)
    print >> f_flh, ','.join(header)
    for data in f_lh_contents:
        zone_id, year, month, day, hour, load = data
        if not load and datetime.date(int(year), int(month), int(day)) < datetime.date(2008, 6, 30):
            load = backcasted_dates[(zone_id, year, month, day, hour)]
        print >> f_flh, ','.join([zone_id, year, month, day, hour, load])
        