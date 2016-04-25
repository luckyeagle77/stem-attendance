__author__ = 'student'
# Comments look like this
import time
import pickle

present = []

with open('students.p', 'rb') as p_file:
        roster = pickle.load(p_file)
        
while True:
    try:
        s_id = input('Scan student id or enter Q to quit: ')
        if s_id in ['q', 'Q']:
            mark_absent = input('Mark missing students absent? (y/[n]) ')
            if mark_absent in ['y', 'Y']:
                for key, data in roster.items():
                    if data['name'] not in present:
                        roster[key]['absent'].append(time.strftime("%m/%d"))
                with open('students.p', 'wb') as p_file:
                    pickle.dump(roster, p_file)
            break

        else:
            present.append(roster[s_id]['name'])
            roster[s_id]['present'].append(time.strftime("%m/%d at %I/%M"))
            print('%s checked in on %s' % (roster[s_id]['name'], time.strftime("%m/%d at %I:%M")))
    except KeyError:
        print("Invalid ID number")
