class BankAccount:
    # Class attributes
    all_accounts = []

    # Constructor for each account
    def __init__(self, int_rate=0.05, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def get_account_info(cls):
        for inst in cls.all_accounts:
            inst.display_account_info()

account1 = BankAccount()
account2 = BankAccount()
account3 = BankAccount(balance=150)
account1.deposit(10).deposit(20).deposit(1000).withdraw(75).yield_interest()
account2.deposit(300).deposit(150).withdraw(25).withdraw(5).withdraw(255).withdraw(2).yield_interest()
BankAccount.get_account_info()