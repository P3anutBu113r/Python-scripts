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
    Firstname, Lastname = Name.split()
    Address = inputvalidation(str(input('What is your address? ')),50)
    PhoneNumber = inputvalidation(int(input('What is your phone number? ')),10)
    Email = inputvalidation(str(input('What is your email address? ')),50)
    Organisation = 'None'
    if input("are you part of an organisation? (y/n) ") == 'y' or type == 2:
        Organisation = inputvalidation(str(input('What is your organisation? ')),50)
    SecurityRating=1
    print(f"Your details are:\n Type {table}\n Name {Firstname} {Lastname}\n Address {Address}\n Phone Number {PhoneNumber}\n Email {Email}")
    Proceed = input(f'Do You wish to continue y/n ')
    if Proceed == 'y' and Organisation == 'None':
        cursor.execute(f'insert into {table} (Name, Address, PhoneNumber, Email, SecurityRating) values ("{Name}", "{Address}", {PhoneNumber}, "{Email}", {SecurityRating})')
        db.commit()
    elif Proceed == 'y' and Organisation != "None":
        cursor.execute(f'insert into {table} (Name, Address, PhoneNumber, Email, SecurityRating, Organisation) values ("{Name}", "{Address}", {PhoneNumber}, "{Email}", {SecurityRating}, "{Organisation}")')
        db.commit()
    else:
        print('nope')
        modeselect()


def modeselect():
    mode = int(input('Are you either a Participant(1), a presenter(2), a stall(3), or an Event(4)'))
    if mode == 1:
        PersonEnter(1)
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
    print( namesplit(input()))
    cursor.execute('')
    print(cursor.fetchall())
    modeselect()