class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")


dog1 = Animal("Buddy", "Dog", "Woof")
cat1 = Animal("Whiskers", "Cat", "Meow")

dog1.make_sound()
cat1.make_sound()

#OUTPUT
"""
Buddy the Dog says Woof!
Whiskers the Cat says Meow!
"""
