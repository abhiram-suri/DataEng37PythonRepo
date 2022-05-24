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

keep_asking = True
response = None

while keep_asking:
    play_again = input("Would you like to play?\n")
    if play_again : "Yes"
    x = 0
    input_num = input("What number would you like to play Fizz Buzz until?\n")
    while x < int(input_num):
            x += 1
            if x % 3 == 0 and x % 5 != 0:
                print("Fizz!")
            elif x % 5 == 0 and x % 3 != 0:
                print("Buzz!")
            elif x % 5 == 0 and x % 3 == 0:
                print("Fizz Buzz!")
            else: print(f"{x}")
            keep_asking = False
    else: play_again = "No"
    print("Fizz Buzz Completed")
