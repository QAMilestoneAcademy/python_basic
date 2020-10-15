# Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# Expected output:
#
# 15
# 55
# 75
# 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)