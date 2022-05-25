# class Spartans:
#     def __init__(self, name, course, trainer):
#         self.name = name
#         self.course = course
#         self.trainer = trainer
#
# abhiram = Spartans("Abhiram", "Data Eng", "David Harvey")
# print(abhiram.name)
# print(abhiram.course)
# print(abhiram.trainer)



class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self._speed = 0

    def accelerate(self, speed_add):
        self._speed = min(self._speed + speed_add, self.top_speed)

    def brake(self, speed_subtract):
        self._speed = max(self._speed - speed_subtract, 0)

my_car = Car("Toyota", "Yaris", 108)


print("My car's make is " + my_car.make)
print("My car's model is " + my_car.model)
print("My car's top speed is " + str(my_car.top_speed) + " mph")
my_car.accelerate(200)
my_car.brake(0)
print("The car's current speed is " + str(my_car._speed) + " mph")

