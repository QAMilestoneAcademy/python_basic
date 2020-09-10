#Create list with range function
my_list=list(range(1,10))
print(my_list)

#List of even numbers
my_list=list(range(0,21,2))
print(my_list)

#iterating through list
my_list=["banana","apple","guava"]
for fruit in my_list:
    print("I love to eat " + fruit)

#iterating through list created with range function
for number in list(range(1,5)):
    print("number is",number)
    print("square of number is", number**2)

#iterating through list -performing operation on each number & creating new list by apending to an empty list
my_empty_list=[]
for number in list(range(1,5)):
    square=number**2
    my_empty_list.append(square)
print(my_empty_list)

