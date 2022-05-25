from pokemon_class import Pokemon
from move import Move

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            "Charmander",
            "Fire",
            hp=7,
            attack=9,
            defence=5
        )
        self.moves.append(Move("Scratch", "Normal", 10))
        self.moves.append(Move("Growl", "Normal", 0))

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu",
                         "Electric",
                         hp=6,
                         attack=6,
                         defence=6
        )
        self.moves.append(Move("Thundershock", "Electric", 20))
        self.moves.append(Move("Tail Whip", "Normal", 0))


if __name__ == "__main__":
    char = Charmander()
    print(char.moves)