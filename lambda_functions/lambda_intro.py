def add_plus_one(num1, num2):
    return num1 + num2 + 1

print(add_plus_one(3,7))

# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map

savings = [234.00, 555.00, 647.25, 839.00]
# bonus = savings with 10% added on
# bonus = []
# for saving in savings:
#     bonus.append(saving * 1.1)
# print(bonus)

def apply_bonus(saving):
    return saving * 1.1

bonus_map = list(map(apply_bonus, savings))
print(bonus_map)

bonus_lambda = list(map(lambda x: x * 1.1, savings))
print(list(f"{bl:.2f}" for bl in bonus_lambda))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use map and lambda to create a list of each number squared plus 3

numbers_alt = (map(lambda n: (n ** 2) + 3, numbers))
# print(list(numbers_alt))
evens = filter(lambda n: n % 2 == 0, numbers_alt)
print(list(evens))

jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]
data = filter(lambda j: 'Data' in j, jobs)
data_map = map(lambda j: j[5:], data)
print(list(data_map))