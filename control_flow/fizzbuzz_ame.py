#
# keep_asking = True
# input_a = none

# while keep_asking:
# response = input("Would you like to play Fizz Buzz?\n")
#(
# if


# x = 0
#
# input_num = input("What number would you like to play Fizz Buzz until?\n")
#
# while x < int(input_num):
#     x += 1
#     if x % 3 == 0 and x % 5 != 0:
#         print("Fizz!")
#     elif x % 5 == 0 and x % 3 != 0:
#         print("Buzz!")
#     elif x % 5 == 0 and x % 3 == 0:
#         print("Fizz Buzz!")
#     else:
#         print(f"{x}")
#
# print("Thank you for playing Fizz Buzz!")

while True:
    continue_input = "no"

    if continue_input.lower() in ("no", "n"):
        break

play = input("Press f to play Fizz Buzz\n")
while play == 'f':
    input_num = ''
    while not input_num.isdigit():
        input_num = input("What number would you like to play Fizz Buzz until?\n")
for x in range(1, int(input_num) + 1):
        if x % 3 == 0 and x % 5 != 0:
            print("Fizz!")
        elif x % 5 == 0 and x % 3 != 0:
            print("Buzz!")
        elif x % 5 == 0 and x % 3 == 0:
            print("Fizz Buzz!")
        else:
            print(f"{x}")

play = input("\nPress p to play again, or q to quit: ")

print("Fizz Buzz Completed")

