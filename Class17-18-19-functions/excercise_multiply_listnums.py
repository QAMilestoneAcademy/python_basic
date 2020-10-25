# https://www.w3resource.com/python-exercises/python-functions-exercise-3.php
# Write a Python function to multiply all the numbers in a list.
# my_list=[1,2,3,4,56,7]
# multiple=1
# for num in my_list:
#     multiple=multiple*num
# print(multiple)

def multiply(any_list):
    multiple = 1
    for num in any_list:
        multiple = multiple * num
    return multiple

my_list=[2345,56,67,89]
print(multiply(my_list))
