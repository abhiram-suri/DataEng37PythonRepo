h = "Hello world!"
#
# double = "Double Quotes"
# single = 'Single Quotes'
#
# print(double, single)
#
# # failure = "I said "Oh no!""
# double_in_single = 'I said "Oh no!"'
#
# both = 'I said "Oh No! David\'s in trouble!"'
# print(both)

# string_block = """
# Everything here
# is part of the string
#
# Up until
# The last 3 quotes
# """
# print(string_block)

h = "hello world!. greetings. something else."
# print(h[-3])
#
# print(h[2:7])
# print(h[7])
#
# print(h[3:8])
#
print(h[3:])
#
# print(h[1:-1:3])
print(h[4::2])
print(h[::-1])

# String Methods

# print(type(h))
# print(h. lower())
# print(h.upper())
# print(h. capitalize())
# print(h. strip("hell"))
# print(h. count("l"))
# print(h. replace("l","g").capitalize())

# string_list = h.split(". ")
# print(string_list)
#
# new_sentence = ". ".join(s.capitalize() for s in h.split(". "))
# print(new_sentence)
#
# ThisWillWork = 6
# print(ThisWillWork)


# Concatenation

a = "Mr"
b = "Blue"
c = "Sky"

print (a + " " + b + " " + c)

d = "Mambo"
e = "Number"
f = 5

print(d + " " + e + " " + str(f))

my_int = 50
print(int(f) + my_int)

# F string

print(f"{d} {e} {f}")

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years + 7} years old in dog years and {height_cm:.2f}cm tall")

score = 16
max_Score = 26

print(f"You scored {score/max_Score:.2f}")
print(f"You scored {score/max_Score:%}")
print(f"You scored {score/max_Score:.2%}")
print(f"You scored {score/max_Score:.0%}")


