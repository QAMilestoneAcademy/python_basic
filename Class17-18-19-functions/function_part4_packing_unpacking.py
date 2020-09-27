#example 1
# print(1,2,3,4,5)
# numbers=[1,2,3,4,5]
# # #below is called unpacking
# print(*numbers)
# print("abc")
# #below is called unpacking
# print(*"abc")
# #is same as
# print("a","b","c")
# #below is limited by number of arguments
# def add(x,y):
#     return x+y
#
# numbers=[1,2,3,4]
# sum=0
# for number in numbers:
#     sum=sum+number
# print(sum)
# #to add any number of numbers
def add(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum
# #add any numbers
my_sum=add(1,2,3,4,5,6)
print(my_sum)
#
# ##How packing/unpacking works with keyword argument
#
def about(name,age,likes):
    sentence="Meet {}!They are {} years old and they like {}".format(name,age,likes)
    return sentence
my_dict={"name":"anu","age":"10","likes":"python"}
print(about(**my_dict))
#
# #define with kwargs
# def foo(**kwargs):
#     for key,value in kwargs.items():
#         print("{}:{}".format(key,value))
#
#
# my_dict = {"fruit1": "orange", "fruit2": "apple", "fruit3": "guava"}
# foo(fruit1="orange",fruit2="apple",fruit3="guava")
#
