"""This code replicates an example of events with different times, locations and events and uses a left/right system where if the user doesnt like the event,
they would type left and it will show another event. if the user likes the event and types right, the next time the same event pops up, the status will show recommended.
New events that the user hasnt seen before will show up as new. 
This aims to filter events that the elderly dont like so they spend less time looking or remembering events and they just have to look at the status of the event such as "New" or "recommended"""
import random

#'location' list stores the locations for all the events
location = ['Tampines CC', 'Zoom', 'Choa Chu Kang', 'Zumba Rock 2024', 'Zoom', 'Bukit Gombak CC']

#initialise current date
date = '12/09/2024'
year = int(date[6:])
month = int(date[3:5])
currentday = int(date[:2])


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return True
        else:
            return False
    else:
        return False
    
#initialise 'notifStatus' dictionary which stores event types. change line 19 and 25
notifStatus= {
    'Zumba Rock 2024' : '* new *',
    'How to Handbell' : '* new *',
    'Tai Chi' : '* new *',
    'Crochet Workshop' : '* new *',
    'Groceries Online' : '* new *'
}

notifType = ['Groceries Online', 'Crochet Workshop', 'Tai Chi','How to Handbell', 'Zumba Rock 2024']
notification = []

# lines 30 - 60 is to randomise date and time such that it will only be after chosen date and not in an awkward time
for i in range(10):
    if is_leap_year(year):
        leapYearcheck = True

    if month % 2 == 1 and month < 8 or month >=8 and month % 2 == 0 :
        finalday = 31
    else:
        finalday = 30

    if month == 2:
        finalday = 28
        if leapYearcheck:
            finalday = 29

    displayDay = random.randint(currentday, finalday)
    try:
        if displayDay <= 10:
            appdate = "0{:>1}/{:>2}/{:>4}".format(displayDay, date[3:5], year)
        else:
            appdate = "{:>2}/{:>2}/{:>4}".format(displayDay, date[3:5], year)
    except:
        appdate = date


    time = random.randint(1,12)
    temp =['am','pm']
    if 1 <= time <= 6 or time == 12:
        timeType = temp[1]
    else:
        timeType= temp[0]

    time = str(time)


    # the thing that is going to be displayed
    card = {
        "date" : appdate,
        "time" : time + timeType,
        "location" : random.choice(location),
        "type" : random.choice(notifType)
    }
    notification.append(card)


    # displaying the notif
    print("+-------------------------------------------------------------+")
    print("| Event: {:<53}|".format(card['type']))
    print("| Date: {:<38}                |".format(card['date']))
    print("| Time: {:<38}                |".format(card['time']))
    print("| Location: {:<50}|".format(card['location']))
    print("| {:^60}|".format(notifStatus[card['type']]))
    print("+-------------------------------------------------------------+")


    #if user swipes right, the event will be saved. It will appear as a recommended event in followiing notifications
    #if user swipes left, the event is 
    if notifStatus[card['type']] == "* new *":
        notifStatus[card['type']] = ''
    print('Choose Right if you are interested in this event!')
    direction = input("Right/Left: ")
    direction = direction.lower()

    if direction == "right":
        notifStatus[card['type']] = 'recommended'
    if direction == "left":
        notifStatus[card['type']] = ''