import sqlite3
db = sqlite3.connect('Conference.db')
cursor = db.cursor()
print('Welcome to The blackhats signup process')
def PersonEnter(type):
    if type == 1:
        table = 'Participant'
    elif type == 2:
        table = 'Presenter'

    Name = inputvalidation(str(input('What is your name? (e.g John Person)')), 50)
    Firstname, Lastname = namesplit(Name)
    Address = inputvalidation(str(input('What is your address? ')),50)
    PhoneNumber = inputvalidation(int(input('What is your phone number? ')),10)
    Email = inputvalidation(str(input('What is your email address? ')),50)
    Organisation = 'None'
    if type == 1:
        if input("are you part of an organisation? (y/n) ") == 'y':
            Organisation = inputvalidation(str(input('What is your organisation? ')),50)
    elif type == 2:
        Organisation = inputvalidation(str(input('What is your organisation? ')), 50)
    SecurityRating=1
    print(f"Your details are:\n Type {table}\n Name {Firstname} {Lastname}\n Address {Address}\n Phone Number {PhoneNumber}\n Email {Email}")
    Proceed = input(f'Do You wish to continue y/n ')
    if Proceed == 'y' and Organisation == 'None':
        statement = f'insert into {table}(FirstName, LastName, Address, PhoneNumber, Email, SecurityRating) values ("{Firstname}", "{Lastname}", "{Address}", {PhoneNumber}, "{Email}", {SecurityRating});'

    elif Proceed == 'y' and Organisation != "None":
        statement = f'insert into {table} (FirstName, LastName, Address, PhoneNumber, Email, SecurityRating, Organisation) values ("{Firstname}", "{Lastname}", "{Address}", {PhoneNumber}, "{Email}", {SecurityRating}, "{Organisation}")'
    else:
        print('nope')
        modeselect()
    cursor.execute(statement)
    db.commit()
def EventSignup():
    cont = False
    print('The events available:')
    events = cursor.execute('select * from Event;')
    for x in events:
        print(x)
    Eventid = int(inputvalidation(input('Enter the Event ID of the event that you wish to signup: '), 2))
    events = cursor.execute('select * from Event;')
    for x in events:
        if x[0] == Eventid:
            cont = True

    if cont == False:
        print('The event does not exist')
        input('Press Enter to continue')
        modeselect()
    Name = inputvalidation(str(input('What is your name? (e.g John Person): ')), 50)
    Firstname, Lastname = namesplit(Name)

    Userid = cursor.execute(f'select ParticipantID from Participant where Firstname = "{Firstname}" and LastName = "{Lastname}" ;').fetchall()
    Userid = Userid[0][0]

    try:
        exists = cursor.execute(f' select * from EventParticipants where ParticipantID = {Userid} and EventID = {Eventid};').fetchall()
        exists = exists[0]
        print(exists)
        print('You have already signed up!')
    except:
        cursor.execute(f'insert into EventParticipants values ("{Userid}", "{Eventid}",0)')
        print('Signup complete')
        db.commit()

def modeselect():
    mode = int(input('Are you either a Participant(1), a presenter(2), a stall(3), or an Event(4)'))
    if mode == 1:
        temp = input('Do you want to sign up as a new participant?(1) Or sign up for an event?(2)')
        if temp == '1':
            PersonEnter(1)
        elif temp == '2':
            EventSignup()
    elif mode == 2:
        PersonEnter(2)
    else:
        print('Please enter a number between 1 and 4')
def namesplit(name):
    try:
        firstname,lastname = name.split(' ')
    except ValueError:
        firstname, throwaway, lastname = name.split(' ')
    try:
        return firstname,lastname
    except ValueError:
        print('Please enter a valid firstname and lastname')
        input()
        modeselect()
def inputvalidation(userinput, max):
    #if type(userinput) == int:
     #   if userinput > max:
      #      print("Not a valid phone number")
       # else:
        #    return userinput

    #else:
     #   if len(userinput) > max:
      #      print('Too long')
       #     return(0)
        #else:
    return(userinput)

while True:

    modeselect()
#why the fuck wont this commit
