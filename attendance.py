__author__ = 'student'

import time

while True:
    try:
        s_id = input('Scan student id or enter Q to quit: ')
        if s_id in ['q', 'Q']:
            break
        else:
    	    print('%s checked in - %s' % (student_info[s_id], time.strftime("%I:%M %p")))
    except KeyError:
        print("Invalid ID number")
