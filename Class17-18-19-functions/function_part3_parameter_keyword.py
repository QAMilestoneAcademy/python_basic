# function parameters are the ones passed to function while defining function
def about(name,age,likes):
    sentence="Meet {}!They are {} years old and they like {}".format(name,age,likes)
    return sentence
# my_sentence=about("anu",10,"coding") #arguments
# print(my_sentence)
#
# # #With the help of keyword argument we can also do like below, ordering will not matter anymore
# my_sentence=about(age=23,name="Jack",likes="Python")#keyword argument
# print(my_sentence)

# # #We can also define default value of parameter so that it is not cumpolsory to pass the value while calling
# # #default parameter always needs to be at the end
# def about(name,age,likes="Python"):
#     sentence="Meet {}!They are {} years old and they like {}".format(name,age,likes)
#     return sentence
# # #
# my_sentence=about(age=23,name="Jack")
# print(my_sentence)
#
# my_sentence=about(age=23,name="Jack",likes="Reading")
# print(my_sentence)
