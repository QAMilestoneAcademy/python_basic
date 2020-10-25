# First, def a function called cube that takes an argument called number.
# Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
# Define a second function called by_
# three that takes an argument called number.
# if that number is divisible by 3,by_threeshould call cube(number) and return its result.
# Otherwise, by_three should return False. -Check if it works.

def cube(number):
    my_cube = number * number * number
    return my_cube

def by_three(number):
  if number %3 ==0:
    result=cube(number)
    return result
  else:
    return "remainder is not zero"

print(by_three(9))
print(by_three(7))