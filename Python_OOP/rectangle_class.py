class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def get_perimeter(self):
        return (2 * self.height) + (2 * self.length)

    def get_area(self):
        return self.length * self.height

    def __repr__(self):
        return f"(length = {self.length}, width = {self.height})"

    def __str__(self):
        return f"({self.length})({self.height})"

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


rectangle_class = Rectangle(4,3)
square_class = Square(5)

print("The perimeter of the rectangle is", rectangle_class.get_perimeter(), "cm")
print("The area of the rectangle is", rectangle_class.get_area(), "cm^2")
print("The perimeter of the square is", square_class.get_perimeter(), "cm")
print("The area is of the square is", square_class.get_area(), "cm^2")
