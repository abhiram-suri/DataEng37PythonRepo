class Bird:
    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = can_fly
        self._age = 0

    def reproduce(self):
        if self._age < 2:
            return "Too young"
        else:
            return "Egg"

    def age_up(self, years=1):
        self._age += years

    def get_age(self):
        return self._age # Encapsulation

# Instantiate an object
# bird = Bird("Sparrow", "Brown")
#
# # Calling methods
# bird.age_up()
# bird.age_up()
# bird.age_up()
# egg = bird.reproduce()
# print(egg)

class Penguin(Bird):   # Inheritance
    def __init__(self, subspecies, colour=("Black", "Yellow", "White")):
        super().__init__("Penguin", colour, False)
        self.subspecies = subspecies

    def hunt_for_fish(self):
        print("Splash")



class KingPenguin(Penguin):
    def __init__(self):
        super().__init__("King Penguin", "Black, White, Yellow")

penguin = KingPenguin()
print(penguin.colour)
