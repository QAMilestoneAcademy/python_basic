#Statement following if condition are indented within if
#indented statements excute if condition within if bracket meets
if(10>5):
    print("10 is greater then 5")

#will execute in any condition
print("program ended")

#Let's guess the output:
spam = 7
if spam > 5:
   print("five")
if spam > 8:
   print("eight")

# An else statement follows an if statement, and contains code that is called when the if statement evaluates to False.
# As with if statements, the code inside the block should be indented.
x = 10
y = 20

if x > y:
 print("if statement")
else:
 print("else statement")
# The elif (short for else if) statement is a shortcut to use when chaining if and else statements.
# A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.

if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")

#boolean comparison if or else

age = 15
money = 500
if (age > 18 or money > 100):
 print("Welcome")

#Find out the result:

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")




