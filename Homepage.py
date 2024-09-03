""" This code asks for user and extracts info from an excel sheet to filter the events based on language for each user. 
 When the date of the event is coming up in 3 days, it will apear in the notifications tab where user can sign up for the event.
 1 day after the event is done, the status will show up completed and the next day, it will be removed from the homepage"""

import pandas as pd

#read the Excel file (make sure the file path is correct)
file_path = "C:\\Users\\sarav\\OneDrive\\Documents\\youthXHacks_database.xlsx"
df = pd.read_excel(file_path)

#initialise dictionary to store names based on their preferred languages
language_groups = {}
nameGroup = {}

#iterate over each row in the spreadsheet
for index, row in df.iterrows():
    name = row['Name'].strip()
    #splits languages by ',' and stores into list
    preferred_languages = row['Preferred Languages'].split(', ')
    nameGroup[name] = preferred_languages

#appends names into 'language_groups' dictionary under the languages' key
for language in preferred_languages:
    if language not in language_groups:
        language_groups[language] = []
    language_groups[language].append(name)
#print(nameGroup)



while True:
    #prompts user for username
    User = input("What is your username? ")
    if User in nameGroup:
        break

#List of filtered events
eventCheck = []
#List for event to remove after its deadline
removed = []
#List of events in notification tab
notif = []
#current date
date = "20/10/24"

# to check if the year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return True
        else:
            return False
    else:
        return False
    
# events
event = {
        "Crochet Workshop" : {
                              'location' : 'Tampanies CC',
                              'date' : '27/10/24',
                              'language' : ["Tamil","English","Malay","Chinese"],
                              'status' : ''},
        "Groceries Online" : {
                              'location' : 'Zoom',
                              'date' : '23/10/24',
                              'language' : ['English'],
                              'status' : ''},
        "Tai Chi" : {
                             'location' : 'Choa Chu Kang Park',
                              'date' : '26/10/24',
                              'language' : ['Tamil','English','Malay','Chinese'],
                              'status' : ''}, 
        "Zumba Rock 2024" : {
                              'location' : 'Bukit Batok CC',
                              'date' : '20/11/24',
                              'language' : ['English'],
                              'status' : ''},
        "How to Handbell" : {
                              'location' : 'Bukit Gombak CC',
                              'date' : '19/09/24',
                              'language' : ['Tamil'],
                              'status' : ''},
        }

while True:
    count = 0

    #used for the notification tab prompt
    notifFlag = False

    #converts the string (date) to day, month and time
    year = int(date[6:])
    month = int(date[3:5])
    day = int(date[:2])

    #checks the final day for each month of the year
    if month % 2 == 1 and month < 8 or month >=8 and month % 2 == 0 :
        finalday = 31
    else:
        finalday = 30

    #Checks if month february and if a leap year, change last day to 29
    if month == 2:
        finalday = 28
        if is_leap_year(year):
            finalday = 29

    for i in event:
        for j in nameGroup[User]:

            #if the user prefered language is in the event
            if j in event[i]['language'] and event[i] not in eventCheck:
                displayLanguage = ''
                count += 1

                #adds event to the filtered events list
                eventCheck.append(event[i])

                # checks if event date is nearing
                if int(event[i]['date'][:2]) - 3 == int(date[:2]) and month == int(event[i]['date'][3:5]) :
                    # add event to notif list
                    if i not in notif:
                        notif.append(i)

                # checks if event day is over
                if int(event[i]['date'][:2]) + 1 == int(date[:2]) and month == int(event[i]['date'][3:5]):
                    # removes event from notif list
                    notif.remove(i)
                    # adds event to the removed list
                    removed.append(i)
                    # changes status for event to completed
                    event[i]['status'] = "Completed"

                #Displays the number corresponding to each event
                print(f"{count})")

                print("     +-------------------------------------------------------------+")

                #Displays events with required details
                print("     | {:^60}|".format(i))
                print("     | Location: {:<50}|".format(event[i]['location']))
                print("     | Date: {:<54}|".format(event[i]['date']))

                #used to display the language on the event card
                for l in event[i]['language']:
                    displayLanguage += l
                    displayLanguage += '/'
                displayLanguage = displayLanguage[:-1]

                #if all languages display "All Langauges" instead of English/Malay/Chinese/Tamil
                if event[i]['language'] == ['Tamil','English','Malay','Chinese']:
                    displayLanguage = "All Languages"
                
                #Displays Langauge
                print("     | Language: {:<50}|".format(displayLanguage))

                #Displays status if any
                if event[i]['status'] != '':
                    print("     | {:^60}|".format(event[i]['status']))

                print("     +-------------------------------------------------------------+")
                print()

    #List of filtered events
    eventCheck = []

    #Displays current date
    print(date)

    # Flag for notif tab appearing in menu and accessing the notif tab from menu
    if notif != None:
        notifFlag = True

    #Displays notification tab prompt
    if notifFlag:
        print("0) change to notifications tab ({})".format(len(notif)))

    #Displays next day prompt
    print("1) next day")

    #Asks for user input
    Menu = input("Select your option (1/0): ")

    if Menu == "1":

        #Changes removed list back to None and removes from the Event dictionary
        if len(removed) > 0:
            del event[removed[0]]
            removed = []

        #increases day count by 1
        day += 1

        # if day passess last day of month then reset day and add 1 to month
        if day > finalday:
            month += 1
            day = 1

        # change date to the new date (next day)
        date = f"{day:02}/{month:02}/{year}"

    if Menu == "0" and notifFlag:
        count = 0

        for i in notif:
            count += 1
    
            #Displays the number corresponding to each event
            print(f"{count})")

            print("     +-------------------------------------------------------------+")

            # only prints whatever event is supposed to be in the notif tab with its required details
            print("     | {:^60}|".format(i))
            print("     | Location: {:<50}|".format(event[i]['location']))
            print("     | Date: {:<54}|".format(event[i]['date']))

            #used to display the language on the event card
            for l in event[i]['language']:
                displayLanguage += l
                displayLanguage += '/'
            displayLanguage = displayLanguage[:-1]

            #if all languages display "All Langauges" instead of English/Malay/Chinese/Tamil
            if event[i]['language'] == ['Tamil','English','Malay','chinese']:
                displayLanguage = "All Languages"

            #Displays Langauge
            print("     | Language: {:<50}|".format(displayLanguage))

            # checks if have status and prints if 
            if event[i]['status'] != '':
                print("     | {:^60}|".format(event[i]['status']))

            print("     +-------------------------------------------------------------+")
            print()
        try:
            #Prompts user to sign up for any one of the events
            SignUp = int(input("These events are upcoming, Which one would you like to sign up for? "))

            #Changes status to Signed up
            event[notif[SignUp-1]]['status'] = "Signed Up"
        except:
            print("Please enter a valid integer shown on screen")
