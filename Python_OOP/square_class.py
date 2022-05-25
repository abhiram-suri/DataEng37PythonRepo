class Square:
    def __init__(self, length):
        self.length = length

    def get_perimeter(self):
        return 4 * self.length

    def get_area(self):
        return self.length * self.length

    def __repr__(self):
        return f"(length = {self.length})"

    def __str__(self):
        return f"({self.length})"

square_class = Square(5)

print("The perimeter is", square_class.get_perimeter(), "cm")
print("The area is", square_class.get_area(), "cm^2")

