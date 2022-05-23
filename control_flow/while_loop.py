# x = 1
#
# while x <= 100:
#     print(f"{x}")
#     x += 1
#     if x % 3 == 0 and x % 5 != 0:
#         print("Fizz!")
#     if x % 5 == 0 and x % 3 != 0:
#         print("Buzz!")
#     if x % 5 == 0 and x % 3 == 0:
#         print("Fizz Buzz!")
#
#
# print("Fizz Buzz completed!")

keep_asking = True
age_int = None

while keep_asking:
    age = input("What is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Please enter a valid number in digits")

print(f"Your age is {age_int}")