class Account:
    def _init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance


    #method to deposit money in account
    def deposit(self,amount):
        self.balance+=amount

    #method to withdraw money from account provided you have sufficient money
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
         self.balance-=amount
        else:
         print("sorry not enough funds!")


    def statement(self):
        print("account balance: -> £{}".format(self.balance))
#
#
class CurrentAccount(Account):
    def __init__(self,name,balance):
     super()._init__(name,balance,min_balance=200)

    def __str__(self):
        return "{}'s current account £{}".format(self.name,self.balance)
#
#
# class SavingAccount(Account):
#     def __init__(self,name,balance):
#      super()._init__(name,balance,min_balance=0)
#
#
#     def __str__(self):
#         return "{}'s saving account £{}".format(self.name,self.balance)
#
# daiwik_account=CurrentAccount("Daiwik",800)
# daiwik_account.deposit(300)
# daiwik_account.statement()
# daiwik_account.withdraw(400)
# daiwik_account.statement()
#
#
#
anu_account=CurrentAccount("anu",500)
anu_account.deposit(300)
anu_account.statement()
anu_account.withdraw(400)
anu_account.statement()
print(anu_account)
# #
# # sia__account= SavingAccount("Sia",200)
# # print(sia__account)

