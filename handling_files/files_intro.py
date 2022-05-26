# with open("order.txt") as file:
#     orders = file.read().split('\n')
#
# # print(orders, type(orders))
# # order_list = orders.split('\n')
# # print(order_list)
#
# print(orders)
# print(file)

colours = ["red\n", "yellow\n", "green\n"]

with open("order.txt", "a") as file:
    file.write("New string to write\n")
    file.writelines(colours)