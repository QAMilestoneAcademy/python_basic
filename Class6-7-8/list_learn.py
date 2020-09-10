my_list=["paper","pen",2,"pencil"]
# # print(my_list)
print("length of list", len(my_list))

last_element=my_list[len(my_list)-1]

print(last_element)
new_element="eraser"
my_list.append(new_element)
print(my_list)

thislist = ["apple", "banana", "cherry"]


# #len of list
# print("length of list", len(thislist))

# #access element
first_element=thislist[0]
print("my " + first_element)

second_element=thislist[1]
print("my " + second_element)

last_element=thislist[len(thislist)-1]
print("my " + last_element)


#
##Add element to the list

new_element="orange"
thislist.append(new_element)
print(thislist)
if "apple" in thislist:
    print("I am apple")
else:
    print("apple not there")

##remove element to the list
thislist.remove("banana")
print(thislist)

my_empty_list=[]
my_empty_list.append("tazine")

##add a number to empty lis
my_empty_list.append(32)
print(my_empty_list)
my_empty_list.append(23)
print(my_empty_list)
#remove 23 from the list
my_empty_list.remove(23)
print(my_empty_list)

thislist_new = ["apple", "banana", "cherry"]

if "apple" in thislist_new and "banana" in thislist_new:
    print("apple and banana is there")
else:
    print("what is ")

# #splitting string to listt
student_grade=input("enter number of 4 students separated by ,")
print(student_grade)
student_grade_list=student_grade.split(",")
print(student_grade_list)
