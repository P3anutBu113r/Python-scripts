class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.spells = []
    def add_spell(self, spell):
        self.spells.append(spell)
    def show_spells(self):
        for spell in self.spells:
            print(spell)
class Wizard(Student):
    def set_wand(self, wand):
        self.wand = wand

harry = Wizard("Harry", "Gryffindor")
harry.add_spell("Expelliarmus")
harry.add_spell("Stupify")
harry.set_wand('Holly')
harry.show_spells()