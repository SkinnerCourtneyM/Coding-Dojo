class Bank_Account():
    all_instances = []

    # 1. Create a bank account with instret rate and balence.
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_instances.append(self)
    #2. Make a deposit method.
    def deposit(self, amount):
        self.balance += amount
        return self
    #3. Make a withdrawl method.
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(
                f'Transaction Declined. Your balance: {self.balance}')
        return self
    #4. Display account balance.
    def display_account_info(self):
        print(self.balance)
        return self
    #5.  Yeild intrest.
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('Your account balance is negative')
        return self

    @classmethod
    def print_instances(cls):
        for i in cls.all_instances:
            print(i.display_account_info())
#6. Create two acc.

MokubaKaiba = Bank_Account(.2, 100)
SetoKaiba = Bank_Account(0.5, 200)

Bank_Account.print_instances()


MokubaKaiba.deposit(100).deposit(100).deposit(100).withdraw(
    200).yield_interest().display_account_info()
SetoKaiba.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(
    20).withdraw(20).yield_interest().display_account_info()
