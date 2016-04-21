__author__ = 'student'

import time
import shelve

s = shelve.open('students', writeback=True)

while True:
	try:
		s_id = input('Scan student id or enter Q to quit: ')
		if s_id in ['q', 'Q']:
			s.close()
			break
		else:
			s[s_id]['present'].append(time.strftime("%m/%d at %I/%M"))
			print('%s checked in on %s' % (s[s_id]['name'], time.strftime("%m/%d at %I:%M")))
	except KeyError:
		print("Invalid ID number")