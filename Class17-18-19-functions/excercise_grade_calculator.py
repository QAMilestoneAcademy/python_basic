# Given different scored marks of students. We need to find grades. The test score is an average of the respective marks scored in assignments, tests and lab-works. The final test score is assigned using below formula.
#
# 10 % of marks scored from submission of Assignments
# 70 % of marks scored from Test
# 20 % of marks scored in Lab-Works
# total_marks=0.1 * assignment + 0.7 * test + 0.2 * lab
# Grade will be calculated according to :
#
# 1. score >= 90 : "A"
# 2. score >= 80 : "B"
# 3. score >= 70 : "C"
# 4. score >= 60 : "D"
# Also, calculate the total class average and letter grade of class.

student_dict = {"student01":{"name": "Anuradha Agarwal",
                 "assignment": [80, 50, 40, 20],
                 "test": [75, 75],
                 "lab": [78.20, 77.20]
                 }
    , "student02":{"name": "Saurabh Agarwal",
       "assignment": [82, 56, 44, 30],
       "test": [80, 80],
       "lab": [67.90, 78.72]
       }
    , "student03":{"name": "Ankita Garg",
       "assignment": [77, 82, 23, 39],
       "test": [78, 77],
       "lab": [80, 80]
       }
    ,  "student04":{"name": "Priyank Garg",
       "assignment": [67, 55, 77, 21],
       "test": [40, 50],
       "lab": [69, 44.56]
       }
    , "student05":{"name": "Abhijeet Srivastava",
       "assignment": [29, 89, 60, 56],
       "test": [65, 86],
       "lab": [50, 40.6]
       },
        "student06":{"name": "Neha Srivastava",
       "assignment": [29, 89, 60, 96],
       "test": [85, 56],
       "lab": [50, 40.6]
       }
                }
# Function calculates average
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return round(total_sum / len(marks))


# Function calculates total average
def calculate_total_average(studentid):
    assignment = get_average(student_dict[studentid]["assignment"])
    test = get_average(student_dict[studentid]["test"])
    lab = get_average(student_dict[studentid]["lab"])
    # Return the result based on weightage supplied 10 % from assignments 70 % from test 20 % from lab-works
    weighted_marks_student= 0.1 * assignment +  0.7 * test + 0.2 * lab
    return weighted_marks_student

# Calculate letter grade of each student
# Grade will be calculated according to :
#
# 1. score >= 90 : "A"
# 2. score >= 80 : "B"
# 3. score >= 70 : "C"
# 4. score >= 60 : "D"
def assign_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"

#
# # Function to calculate the total average marks of the whole class
# def class_average_is(student_list):
#     result_list = []
#     for studentid in student_list:
#         stud_avg = calculate_total_average(studentid)
#         result_list.append(stud_avg)
#         return get_average(result_list)

# Student list consist the name of students
studentids=[]
# studentids = [key for key in student_dict.keys()]
for key in student_dict.keys():
    studentids.append(key)
# Iterate through the students list
# and calculate their respective
# average marks and letter grade

for i in studentids:
    print(student_dict[i]["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of {} is : {} " .format(student_dict[i]["name"],
                                            calculate_total_average(i)))
    print("Letter Grade of {} is : {} " .format(student_dict[i]["name"],
                                            assign_letter_grade(calculate_total_average(i))))

    print()
# # Calculate the average of whole class
# class_av = class_average_is(studentids)
# print("************************************************")
# print("Class Average is {}".format(class_av))
# print("Letter Grade of the class is {} "
#       .format(assign_letter_grade(class_av)))
# print("************************************************")