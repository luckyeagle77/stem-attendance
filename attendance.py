__author__ = 'student'

import time
import shelve

s = shelve.open('students', writeback=True)
present = []

while True:
	try:
		s_id = input('Scan student id or enter Q to quit: ')
		if s_id in ['q', 'Q']:
			mark_absent = input('Mark missing students absent? (y/[n]) ')
			if mark_absent in ['y', 'Y']:
				for key, data in s.items():
					if data['name'] not in present:
						s[key]['absent'].append(time.strftime("%m/%d"))
			s.close()
			break
		else:
			present.append(s[s_id]['name'])
			s[s_id]['present'].append(time.strftime("%m/%d at %I/%M"))
			print('%s checked in on %s' % (s[s_id]['name'], time.strftime("%m/%d at %I:%M")))
	except KeyError:
		print("Invalid ID number")