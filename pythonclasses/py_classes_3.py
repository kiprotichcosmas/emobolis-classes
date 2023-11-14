class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def printing_balance(self):
        print(f"Balance For Accoount {self.acc_no} is Ksh {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("YOu are poor, you cant make any withdrawals")
        else:
            self.balance -= amount


acc1 = Account("Cosmas", "000023", 90000)
acc2 = Account("Kiprotich", "000026457", 70000)

acc1.deposit(10000)
acc1.printing_balance()

acc2.withdraw(70000)
acc2.printing_balance()
