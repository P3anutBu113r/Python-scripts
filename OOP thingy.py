
loadfile = input("Do You wish to load past people y/n")
loadfile = loadfile.lower()
if loadfile == "y":
    people = []
    with open(r'C:\Users\JonPC\Python-scripts\data.txt', 'r') as fp:
        for line in fp:

            x = line[:-1]
            print(x)


            people.append(x)

else:
    people = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
class PersonCreator:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Person is {self.name} and is {self.age} years old'

while True:
    print("Welcome to the person creator")
    while True:
        continuecreation = input(f'Do You want to create a person y/n')
        if continuecreation == 'y':
            PersonNum = int(input("What Number person is this?"))
            continuecreation = input(f'{PersonNum} selected continuing will overwrite any previous person stored at this number continue? y/n')
            if continuecreation == 'y':
                name = input("What is person's name?")
                age = input("What is person's age?")
                people[PersonNum] = (PersonCreator(name, age))
                break
            elif continuecreation == 'n':
                break
        else:
            break

    Personchoice = int(input('What person number do you want to print'))
    print(people[Personchoice].__str__())
    with open(r'C:\Users\JonPC\Python-scripts\data.txt', 'w') as fp:
        for item in people:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')






