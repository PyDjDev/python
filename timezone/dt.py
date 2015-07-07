from datetime import datetime, timedelta, timezone
import time

td = timedelta(hours=6)
tz = timezone(td)

'''
debug:
print('datetime: {}'.format(dt.strftime('%d.%m.%Y %X')))
print('timedelta: {}, timezone {}'.format(td,tz))
'''

ltz = [timezone(timedelta(hours=hrs)) for hrs in range(-12,13)]
# debug - print('list range: {}'.format(ltz))

while True:
	dt = datetime.now(tz)
	for i_tz in ltz:	
		dt = dt.astimezone(i_tz)
		print('{} {}'.format(dt.tzname(),dt.strftime('%d.%m.%Y %X')))
	time.sleep(1)
	print('='*30)