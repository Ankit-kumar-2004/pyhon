class Bank:
    def __init__(self, balance):
        self.balance = balance   

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

b1 = Bank(1000)
b1.deposit(500)

print(b1.get_balance())