# block of organized & reusable code action or give some results
# Function definition with parameters

def add(x,y):
     x+y
# #calling function with actual values

print(add(100,500))

#If we print this we will not get any output as function is not returning any value.For that we need to add return keyword
#
# def add(x,y):
#     return x+y
#
# print(add(23,56))
# sum=add(5,10)
# print(sum)
# def multiply(x,y):
#      return x*y
# my_multiple=multiply(13,14)
# print(multiply(13,14))
# print(my_multiple)
# #
#return is not same as printing

#
# def add(x,y):
#     return x+y

# def add(x,y):
#     print(x+y)
# #
# answer=add(100,10)
# print(answer)
# #It will return none
# print(type(answer))

# #another example
# a=print("hello")
# print(type(a))

# ##Excercise- Create a function to mutiply 2 numbers & return the answer
#

# #reverse a word
word="pen"
rev_word=word[::-1]
print(rev_word)

# #define a function- take any word & reverse it
def rev(word):
    return word[::-1]
# #
x=rev("python")
print(x)
#
# y=rev("srijan")
# print(y)