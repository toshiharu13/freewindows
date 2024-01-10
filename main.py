from operator import itemgetter
from datetime import datetime, timedelta

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]
free_time = []
free_windows = []
time_format = '%H:%M'
time_30_minutes_delta = timedelta(minutes=30)

newlist = sorted(busy, key=itemgetter('start'))
newlist.append({'start': '21:00'})
newlist.insert(0, {'stop': '09:00'})
#print(newlist)

for i in range(1, len(newlist)):
    element = {
        'start': newlist[i-1]['stop'],
        'stop': newlist[i]['start']
    }
    free_time.append(element)
#print(free_time)

for free_window in free_time:
    start = datetime.strptime(free_window['start'], time_format)
    stop = datetime.strptime(free_window['stop'], time_format)
    while True:
        if start + time_30_minutes_delta <= stop:
            element = {
                'start': start,
                'stop': start + time_30_minutes_delta
            }
            free_windows.append(element)
            start = start + time_30_minutes_delta
        else:
            break
#print(free_windows)

print('Свободные 30-минутные окна:')
for window in free_windows:
    print(f'start: {window["start"].time()} stop: {window["stop"].time()}')