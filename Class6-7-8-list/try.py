# Problem Description
# The program takes a list and puts the even and odd elements in it into two separate lists.
#
# Problem Solution
# 1. Take in the number of elements and store it in a variable.
# 2. Take in the elements of the list one by one.
# 3. Use a for loop to traverse through the elements of the list and an if statement to check if the element is even or odd.
# 4. If the element is even, append it to a separate list and if it is odd, append it to a different one.
# 5. Display the elements in both the lists.
my_empty_list=[]
i=int(input("Enter number of elements: "))
for num in range(0,i):
    j=int(input("Enter a number: "))
    my_empty_list.append(j)
print(my_empty_list)
even=[]
odd=[]

for k in my_empty_list:
    if k%2==0:
        even.append(k)
    else:
        odd.append(k)
print(even)
print(odd)