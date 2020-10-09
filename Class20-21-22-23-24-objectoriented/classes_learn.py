#in the factory coins are produced
#there is a template for 1 p coin, 10p coin,1 pound coin
#on the basis of this template multiple coins are produced
#these coins are physical copies of templates
#in python lets call these templates as classes and physical copies as objects /instance
#classes are made of states(variables) which define the property & behavviour(methods)
class Account:
    def _init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
         self.balance+=amount

    def withdraw(self,amount):

        if self.balance-amount>=self.min_balance:
         self.balance-=amount
        else:
         print("sorry not enough funds!")

    def statement(self):
        print("account balance: -> £{}".format(self.balance))


class CurrentAccount(Account):
    pass
class SavingAccount(Account):
    pass


