#create a list with elements 1, 2,3,4
#ask from user a number
# if the number is even add that number to list using append
#else do not add-print- number is odd
my_list=[1,2,3]
ur_number=int(input("enter your number "))
if ur_number%2==0:
    my_list.append(ur_number)
    print(my_list)
else:
    print("number is odd")