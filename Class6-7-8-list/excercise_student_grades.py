student_grade = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
total_num_grades=sum(student_grade)
print(total_num_grades)
count_grades=len(student_grade)
avge_student_grade=total_num_grades/count_grades
print("average",avge_student_grade)
print("maxim", max(student_grade))