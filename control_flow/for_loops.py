# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print("The next letter is:")
#     print(letter.lower())
#     if letter == "D":
#         print("Oh no!")
# else:
#     print("Hooray")

# letter = alphabet[0]
# print(letter.lower())
# letter = alphabet[1]
# print(letter.lower())
# letter = alphabet[2]
# print(letter.lower())

# nest = [[1, 2, 3], [4, 5, 5], [6, 7, 8, 9]]
#
# for sublist in nest:
#     print(sublist)
#     for number in sublist:
#         print(number)

# hi = "Hello World!"
#
# print(hi)
# for c in hi:
#     print(c)


favourite_tv_show = {
    "show_name": "My Wife and Kids",
    "genre": "Sitcom",
    "main_actor": {
        "name": "Damon Wayans",
        "character_name": "Michael Kyle Sr.",
        "age": 61
    },
    "number_of_series": 5,
    "production": {
        "current_name": "ABC",
        "previous_name": "Touchstone"
           },
    "start_year": 2005
    }

# for element (we assign) in iterable (title of set of data)
# for key, value in favourite_tv_show.items():
#     print(f"The {key} is {value}")

# t = (10, 50)
# a, b = t
# print(a)
# print(b)

r = range(5)
print(r)

for i in range(5):
    print(f"This is line number: {i + 1}")

for i, key in enumerate(film):
    print(f"")