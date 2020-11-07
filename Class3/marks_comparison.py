# # passing marks are 35
marks=int(input("Enter your marks: "))
print(marks>=35)

if marks>=35 and marks<=100:
    print("you have passed")
elif marks>=0 and marks<35:
    print("you have failed")
else:
    print("please enter correct marks")
