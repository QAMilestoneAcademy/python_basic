# #Global -Local -two types- only functions can create local scope
a = 100  #global

def f1():
    global a
    print(a+50)

def f2():
    a=20 #local
    print(a)

f1()
f2()

# #Move a inside function 1
#

# def f1():
#     a = 100 #a becomes local variable & f2 can't see a and hence error would be there
#     print(a)
#
# def f2():
#     print(a)
#
# f1()
# f2()
#
# #Define a inside function 1 & function 2 - both get there local variable
# def f1():
#     a = 100#local
#     print(a)
#
# def f2():
#     a=50#local
#     print(a)
#
# f1()
# f2()
#
# #Define a inside function 1 & function 2 - both get there local variable and also define a globally
#
# a=70 #global
#
# def f1():
#     a = 100#local
#     print(a)
#
# def f2():
#     a=50#local
#     print(a)
# # # # # #Each function by default pick there local variable & not global one
# f1()
# f2()

# # # print(a)#this prints global variable
# a=70
# def f1():
#     global a
#     sum=a+10
#     print(sum)
#
# def f2():
#     a=50
#     print(a)
# # # #Each function by default pick there local variable & not global one
# f1()
# f2()
# # print(a)#this prints global variable
