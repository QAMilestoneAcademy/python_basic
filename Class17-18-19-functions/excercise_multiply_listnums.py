# https://www.w3resource.com/python-exercises/python-functions-exercise-3.php
# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply(([8, 2, 3, -1, 7])))