class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def get_area(self):
        return self.width * self.height

    def __repr__(self):
        return f"(length = {self.width}, width = {self.height})"

    def __str__(self):
        return f"({self.width})({self.height})"

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)


rectangle_class = Rectangle(4,3)
square_class = Square(5)

print("The perimeter of the rectangle is", rectangle_class.get_perimeter(), "cm")
print("The area of the rectangle is", rectangle_class.get_area(), "cm^2")
print("The perimeter of the square is", square_class.get_perimeter(), "cm")
print("The area is of the square is", square_class.get_area(), "cm^2")
