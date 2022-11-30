class BankAccount:
    # Class attributes
    number = 1
    all_accounts = []

    # Constructor
    def __init__(self, int_rate=0.05, balance=0, acc_id=number):
        self.int_rate = int_rate
        self.balance = balance
        self.id = acc_id
        BankAccount.all_accounts.append(self)
        BankAccount.number += 1

    # Deposit method to add to the instance/variable balance
    def deposit(self, amount):
        self.balance += amount
        return self

    # Withdraw Mthod to take money out with the condition its there
    # otherwise a fee is charged
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


class User:
    # Class attributes
    users_accounts = {}

    # Constructor
    def __init__(self, name, email, account_name, deposit=0):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=deposit)
        User.users_accounts.update({f"{account_name}": self.account})
    
    def make_deposit(self, account_name, amount):
        self.users_accounts[account_name].deposit(amount)

    def make_withdraw(self, account_name, amount):
        self.users_accounts[account_name].withdraw(amount)
    
    def display_user_balance(self, account_name):
        self.users_accounts[account_name].display_account_info()

    def transfer_money(self, account_name, amount, other_user, ou_account_name):
        self.users_accounts[account_name].withdraw(amount)
        other_user.make_deposit(f"{ou_account_name}", amount)

    @classmethod
    def add_account(cls, account_name, deposit=0):
        User.users_accounts.update({f"{account_name}": BankAccount(int_rate=0.02, balance=deposit)})

SomeGuy = User("Jeffry","guy@gmail.com","Account1")
Person2 = User("Jane", "jane.doe@gmail.com", "Monniiesss", 150)

SomeGuy.display_user_balance("Account1")
print("---------Depositing--------")
SomeGuy.make_deposit("Account1", 300)
print("---------Finished--------")
SomeGuy.display_user_balance("Account1")

print("---------Withdrawing--------")
SomeGuy.make_withdraw("Account1", 30)
SomeGuy.display_user_balance("Account1")

print("---------Before Transfer--------")
SomeGuy.display_user_balance("Account1")
Person2.display_user_balance("Monniiesss")

SomeGuy.transfer_money("Account1", 100, Person2, "Monniiesss")
print("---------After Transfer--------")
SomeGuy.display_user_balance("Account1")
Person2.display_user_balance("Monniiesss")




