class account: 
    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    def debit(self, amount):
            self.balance -= amount
            print("Rs.", amount, "debited from account", self.accountno)
            print("Current balance is Rs.", self.get_balance())
        

    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "credited from account", self.accountno)
            print("Current balance is Rs.", self.get_balance())
        

    def get_balance(self):
            return self.balance

a1 = account(10000, 12345)
# print(a1.balance)
# print(a1.accountno)   
a1.credit(1000)
