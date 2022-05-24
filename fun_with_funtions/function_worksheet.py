print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def divisors(num):
    div = []
    for i in range(1, num+1):
        if num % i == 0:
            div.append(i)
    return div

# Enter number below as num
num = 70
divisor_list = (divisors(num))

print("f" + "("+str(num)+")" + " " + "=" + " " + str(divisor_list))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def factor(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

print(factor(3, 10))


# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
# "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:

def letter_position(letter):

    alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    return alphabet.index(letter)

def name_index(name):
    index = []
    for char in name:
        ind = ((letter_position(char)))
        index.append(ind)
    return index

print(name_index("abhiram"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:
def letter_position(letter):

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    return alphabet.index(letter)

def name_index(name):
    index = []
    for char in name:
        ind = ((letter_position(char)))
        index.append(ind)
    return index

# Enter name here
name_string = "abhiram"
newstring = name_index(name_string)

id = "".join(map(str, newstring))


print("f" + "("+ "'" + name_string + "'" + ")" + " " + "=" + " " + id)

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:


a = int(id)

b = sum(newstring)

password_id = str(a - b)
print("password" + "("+ "'" + name_string + "'" + ")" + " " + "=" + " " + (password_id))


# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:

def prime(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    for n in range(2, x-1):
        if x % n == 0:
            return False
    else:
        return True

print(prime(5))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def prime(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    for n in range(2, x-1):
        if x % n == 0:
            return False
    else:
        return True

keep_asking = True
age_int = None

while keep_asking:
    digit = input("Enter a number\n")
    if digit.isdigit():
        digit_int = int(digit)
        keep_asking = False
    else:
        print("Please enter a valid number in digits")

prime_digit = prime(int(digit))
print(prime_digit)



# -------------------------------------------------------------------------------------- #