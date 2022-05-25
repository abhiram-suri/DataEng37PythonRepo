# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"location(latitude={self.latitude}, longitude={self.longitude}"
#
#     def __str__(self):
#         return f"({self.latitude}, {self.longitude})"
#
# bham_academy = Location(52.488647, -1.887249)
#
# print(f"The Birmingham Academy is located at {bham_academy}")

class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age *7} dog-years old dog"
        else:
            return self.__str__()
# n = 0.006454
# print(f"Fixed point: {n:f}")
# print(f"2dp: {n:.2f}")
# print(f"Exponential: {n:e}")
# print(f"Percentage: {n:%}")


fido = Dog(5)
print(f"Fido is {fido:dog}")








