def genTimeFormat(t0, t1):
    dict = {}
    dict['AM/PM'] = t1
    temp = t0.split(':')
    dict['HH'] = int(temp[0])
    if dict['AM/PM'] == 'AM' and dict['HH'] == 12:
        dict['HH'] = 0
    if dict['AM/PM'] == 'PM' and dict['HH'] != 12:
        dict['HH'] += 12
    dict['MM'] = int(temp[1])
    return dict

T = int(input())
for _ in range(T):
    t = input().split()
    P = genTimeFormat(t[0], t[1])
    numOfFriends = int(input())
    start = []
    end = []
    attendees = []
    for i in range(numOfFriends):
        time = input().split()
        start.append(genTimeFormat(time[0], time[1]))
        end.append(genTimeFormat(time[2], time[3]))
        if P['AM/PM'] == 'AM' and start[i]['AM/PM'] == 'PM':
            attendees.append(0)
            continue
        if P['AM/PM'] == 'PM' and end[i]['AM/PM'] == 'AM':
            attendees.append(0)
            continue
        if start[i]['HH'] < P['HH'] or start[i]['HH'] == P['HH'] and start[i]['MM'] <= P['MM']:
            if end[i]['HH'] > P['HH']:
               attendees.append(1)
            elif end[i]['HH'] == P['HH'] and end[i]['MM'] >= P['MM']:
                attendees.append(1)
            else:
                attendees.append(0)
        else:
            attendees.append(0)
    for i in range(numOfFriends):
        if i == numOfFriends - 1:
            print(attendees[i])
        else:
            print(attendees[i], end = "")