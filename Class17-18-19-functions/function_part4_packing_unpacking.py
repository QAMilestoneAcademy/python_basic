# #example 1
# print(1,2,3,4,5)
# numbers=[1,2,3,4,5]
# #below is called unpacking arguments
# print(*numbers)
# print("abc")
# # #below is called unpacking
# print(*"abc")
# # #is same as
# print("a","b","c")
# # #below is limited by number of arguments
# def add(x,y):
#     return x+y
#
# my_sum=add(67,78)
# print(my_sum)
#
# numbers=[1,2,3,4]
# sum=0
# for number in numbers:
#     sum=sum+number
# print(sum)
# numbers=[1,2,3,4,5]
# sum=0
# for number in numbers:
#     sum=sum+number
# print(sum)

# #to add any number of numbers

#
# def add(*numbers):
#     sum=0
#     for number in numbers:
#         sum+=number
#     return sum
# # # #add any numbers
# my_sum=add(1,2,3,4,5,6,89,78)
# print(my_sum)
#
# def multiply(*numbers):
#     multiple=1
#     for number in numbers:
#         multiple=multiple*number
#     return multiple
# # # #add any numbers
# my_sum=add(1,2,3,4,5,6,89,78)
# print(my_sum)
# my_multiple=multiply(1,2,3,4,5,6,89,78)
# print(my_multiple)
# #
# # ##How packing/unpacking works with keyword argument
# #
def about(name,age,likes):
    sentence="Meet {}!He/She is {} years old and like {}".format(name,age,likes)
    return sentence
# my_dict={"name":"anu","age":"10","likes":"python"}
# print(about(**my_dict))
# for key,val in my_dict.items:
#     print(key, val)
#
# #define with kwargs
def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


my_dict = {"fruit1": "orange", "fruit2": "apple", "fruit3": "guava"}
foo(fruit1="orange",fruit2="apple",fruit3="guava")

