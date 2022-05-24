# print()
# input()
# type()

# DRY - DON'T REPEAT YOURSELF

# def greeting(name):
#     print("Hello " + name)
#
# # Call the function
# greeting("Konrad")
# greeting("Harry")
# greeting("Dan")

    # def product(*nums):
    #     if len(nums) == 0:
    #         return None
    #     result = 1
    #     for num in nums:
    #         result *= num
    #     return result
#
# print(product(1, 4, 8, 9))
# print(product(5))

# def kwargs_demo(**kwargs):
#     print(kwargs, type(kwargs))
#
# print(kwargs_demo(a="One", b="Two"))

# def calculate_tip(list_of_meals, total_cost, tip_pc):
#     print("You had:")
#     for meal in list_of_meals:
#         print(f"- {meal}")
#     print(f"Your subtotal is: £{total_cost:.2f}")
#     print(f"With a {tip_pc:.0%} tip, the total is £{total_cost * (1 + tip_pc):.2f}")
#
# calculate_tip(["Burger", "Pizza"], 18.50, 0.1)

# def calculate_total_cost(**meal_prices):
#     cost = 0
#     for price in meal_prices.values():
#         cost += price
#     return cost
#
# print(calculate_total_cost(
#     Pizza=8.50,
#     Burger=9.00,
#     Hot_Dog=9.20
# ))

# def greeting(name: str):
#     print("Hello " + name)
#
# greeting("David")

# def division(denom: int, num: int) -> float:
#     return denom / num
#
# a = division(12,6)

# Good functions
# - Name them clearly, lowercase_with_underscores
# - Clear argument names
# - Functions don't RETURN something return None
# - Keep them small
# - Use comments
# - Consider type hints

def fizzbuzz_line(num: int):
    if num % 15 == 0:
        return "Fizzbuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)

def fizzbuzz_game():
    for i in range(1, 101):
        print(fizzbuzz_line(i))

fizzbuzz_game()