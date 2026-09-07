import sqlite3
db = sqlite3.connect('Conference.db')
cursor = db.cursor()
print('Welcome to The blackhats signup process')
def PersonEnter(type):
    if type == 1:
        table = 'Participant'
    elif type == 2:
        table = 'Presenter'
    Name = inputvalidation(str(input('What is your name? ')), 50)
    Address = inputvalidation(str(input('What is your address? ')),50)
    PhoneNumber = inputvalidation(int(input('What is your phone number? ')),10)
    Email = inputvalidation(input('What is your email address? '))
    if input("are you part of an orginisation? (y/n) ") == 'y' or type == 2:
        Orginisation = inputvalidation(str(input('What is your orginisation? ')),50)
    SecurityRating=1
    if input(f'Your details are: Type {table}\n Name {Name}\n, Address {Address}, Phone Number {PhoneNumber}\n, Email {Email}\n Do You wish to continue y/n').lower == 'y':
        print('yippe')
    else:
        modeselect()

def modeselect():
    try:

        mode = int(input('Are you either a Participant(1), a presenter(2), a stall(3), or an Event(4)'))
        if mode == 1:
            PersonEnter(1)
        elif mode == 2:
            PersonEnter(2)
        else:
            print('Please enter a number between 1 and 4')


    except:
        print('Please enter a number between 1 and 4')

def inputvalidation(userinput, len):
    if len(userinput) > len:
        print('Too long')
        return(0)
    else:
        return(userinput)

while True:
   modeselect()