class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def set_habitat(self, habitat):
        self.habitat = habitat
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')
        print(f'Habitat: {self.habitat}')
class Bird(Animal):
    def wingspan (self, wingspan):
        self.wingspan = wingspan
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')
        print(f'Habitat: {self.habitat}')
        print(f'Wingspan: {self.wingspan}')

Jeff = Bird('Jeff', 'Parrot')
Jeff.set_habitat("Tropical House")
Jeff.wingspan(100)
Jeff.show_info()