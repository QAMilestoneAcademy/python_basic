#Define following variables & take them as user input
# name
# product
# unitprice
# totalMoney
# Find out the value of total quantities of product that can be brought with total money using : totalMoney//unitprice
# Find out the money which would be left using : totalMoney%unitprice
# Make sure you convert numbers from inputstring to datatype int.
# print the output like below using string format:
# Hi anu.Your product is sofa.Price of each product is 200.You have total money 700.Hence you can bring 3 number of product sofa.You will be left with money 100

name=input("Please enter your name: ")
product=input("Please enter product you want to buy: ")
unitprice = input("Please enter unit price of product: ")
totalMoney = input("Please enter how much money you have: ")
quantity = int(totalMoney)//int(unitprice)
money_left=int(totalMoney)%int(unitprice)

print("Hi {}.Your product is {}."
     "Price of each product is {}."
     "You have total money {}."
     "Hence you can bring {} number of product {}.You will be left with money {} ".format(name,product,unitprice,totalMoney,quantity,product,money_left))