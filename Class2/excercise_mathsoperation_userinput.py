# Task 3 - Take 2 numbers as input from  user .
# Convert to int & perform mathmatical operation
#Create sentence for results using f string
#Using boolean show number1 greater than 100 by returning true or false



##Solution
num1=int(input("Enter num1:\t"))
num2=int(input("Enter num2:\t"))
print("add",num1+num2)
print("subtract",num1*num2)
print("divide",num1/num2)
print("remainder",num1%num2)
print("quotient",num1//num2)
print("power",num1**num2)

#fstring example
print(f"sum of numbers is {num1+num2}")

#boolean usage
print(num1>=100)