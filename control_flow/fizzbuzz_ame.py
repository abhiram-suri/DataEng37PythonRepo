x = 0

while x < 100:
    x += 1
    if x % 3 == 0 and x % 5 != 0:
        print("Fizz!")
    elif x % 5 == 0 and x % 3 != 0:
        print("Buzz!")
    elif x % 5 == 0 and x % 3 == 0:
        print("Fizz Buzz!")
    else:
        print(f"{x}")


print("Fizz Buzz completed!")