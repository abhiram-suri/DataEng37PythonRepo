class Mammal:
    def __init__(self, name):
        self.name = name

    def give_birth(self):
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self):
        super().__init__("Platypus")

    def give_birth(self):
        print("laying eggs...")

    def give_birth(self, number_of_eggs):
        print(f"Laying {number_of_eggs} eggs...")


perry = Platypus()
perry.give_birth()
perry.give_birth(3)