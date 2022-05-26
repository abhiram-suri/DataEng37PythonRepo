# Create a Budget class that can keep track of different budget categories like food, clothing, and entertainment.
# These should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories

class Budget:
    def __init__(self, category):
        self.category = category
        self.amount = 0


    def deposit(self, deposit_add):
        self.amount = self.amount + deposit_add

    def withdraw(self, withdraw_subtract):
        if withdraw_subtract > 0 and self.amount > withdraw_subtract:
            self.amount -= withdraw_subtract
        else:
            print("Insufficient balance for withdrawal")

    def transfer(self, transfer_funds, category):
        if transfer_funds > 0 and self.amount > transfer_funds:
            self.withdraw(transfer_funds)
            category.deposit(transfer_funds)
        else:
            print("Insufficient balance for transfer")

    def balance(self):
        return self.amount


class Food(Budget):
    def __init__(self):
        super().__init__("Food")


class Entertainment(Budget):
    def __init__(self):
        super().__init__("Entertainment")

class Clothing(Budget):
    def __init__(self):
        super().__init__("Clothing")


food_budget = Food()
ent_budget = Entertainment()
cloth_budget = Clothing()

cloth_budget.withdraw(40)
cloth_budget.deposit(50)
food_budget.deposit(60)
cloth_budget.balance()
cloth_budget.transfer(20, food_budget)
cloth_budget.transfer(100, food_budget)

print("The current balance for food is £" + str(food_budget.amount))
print("The current balance for clothes is £" + str(cloth_budget.amount))
print("The current balance for entertainment is £" + str(ent_budget.amount))

