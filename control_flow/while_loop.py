x = 1

while x <= 100:
    print(f"{x}")
    x += 1
    if x % 3 == 0 and x % 5 != 0:
        print("Fizz!")
    if x % 5 == 0 and x % 3 != 0:
        print("Buzz!")
    if x % 5 == 0 and x % 3 == 0:
        print("Fizz Buzz!")


print("Fizz Buzz completed!")