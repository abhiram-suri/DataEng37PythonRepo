shopping_list = ["bread", "bananas", "biscuits", "oat milk"]
#
# print(shopping_list, type(shopping_list))
#
# # indexing and slicing
#
# print(shopping_list[0])
# print(shopping_list[-1])
# print(shopping_list[::-1])

# # Lists and Mutable
#
# shopping_list[0] = "sugar"
# print(shopping_list)

shopping_list.append("cereal")
print(shopping_list)
shopping_list.append("chocolate")
print(shopping_list)

print(len(shopping_list))

shopping_list.remove("oat milk")
print(shopping_list)

# hi = "Hello"
# print(hi.upper()) # a method that RETURNS something
# print(hi)

print(shopping_list.pop(2))
print(shopping_list)

mixed_list = [1, 2, 3.0, 4+5j, "greatings", True, False, None]
print(mixed_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][-1])
# print(nested_list[1[-1]]) Do Not Do This!

print(shopping_list.count("bananas"))
print(shopping_list.index("chocolate"))