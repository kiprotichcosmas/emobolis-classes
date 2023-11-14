# Inheritance Override
class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance, you can only withdraw, {self.balance}")
        else:
            self.balance -= amount

    def __str__(self):
        return f"name: {self.name}, acc_no: {self.account_number}, balance: {self.balance}"


class DollarAccount(Account):
    def rates(self):
        return 153.89

    def deposit(self, amount):
        usd = amount / 153.89
        self.balance += usd


dc1 = DollarAccount("Cosii", "d-0001", 5000)
dc1.deposit(15389)
print(dc1.balance)
print(dc1.rates())

account_one = Account("Cosmas", "0001", 10000)
account_one.deposit(5000)
print(account_one.balance)
print(account_one)
