# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

no_classes_held = input("Number of classes held")
no_classes_attended = input("Number of classes attended")
perc_attendance = (no_classes_attended/no_classes_held)*100
print("Attendence is",perc_attendance)
if perc_attendance >= 75:
  print("You are allowed to sit in exam")
else:
  print("Sorry, you are not allowed. Attend more classes from next time.")
