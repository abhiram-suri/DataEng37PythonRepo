
with open("drinks_menu.txt", "r") as file:
    drinks = file.read().split('\n')

def order_take(order):
    with open("drinks_order.txt", "a") as file:
        if order in drinks:
            file.write(f"{order}\n")
        else:
            print("Error - Drink Is Not Available")


order_take('Diet Coke')