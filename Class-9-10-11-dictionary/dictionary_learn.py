# dictionary with integer keys
student_grade={"Sid":7,"mahi":8,"aarav":10,"anay":9}
# sid_grades=student_grade["Sid"]
# print(sid_grades)

# # # # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# # #
# # # # using dict()
# my_dict = dict({1:'apple', 2:'ball'})
# # #
# # # # from sequence having each item as a pair
# my_dict = dict([(1,'apple'), (2,'ball')])
#
#
# #Access element
# student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
# mahi_grades=student_grade["mahi"]
# print(mahi_grades)

# # get vs [] for retrieving elements
# person_detail = {'name': 'Jack', 'age': 26,'city':"Dubai"}
#
# # Output: Jack
# print(person_detail['name'])
# print(person_detail['age'])
# print(person_detail['city'])
# # #
# person_detail['age']=27
# print(person_detail)

# # #remove element
# student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
# print(student_grade.pop("mahi"))
# print(student_grade)
# # #
# # # ##add key value pair to the dictionary
country_capital_dict={}
country_capital_dict.update({"India":"Delhi"})
# print(country_capital_dict)
country_capital_dict.update({"UAE":"Abudhabi"})
print(country_capital_dict)
country_capital_dict["a"]="b"
print(country_capital_dict)
#
# # # #Find if key is in the dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

if 3 in d:
  print('Key is present in the dictionary')
else:
  print('Key is not present in the dictionary')
student_grade={"anu":7,"mahi":8,"aarav":10,"anay":9}
# if "anu" in student_grade:dictionary_learn
#   print('Key is present in the dictionary')
# else:
#   print('Key is not present in the dictionary')
# d={}
# d[1]="anu"
# print(d)