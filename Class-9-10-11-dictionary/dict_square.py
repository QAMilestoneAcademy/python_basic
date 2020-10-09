# # # Generate and print a dictionary that contains a number in the form (x, x*x)
n=int(input("Input a number "))
d = {}

for i in range(1,n+1):
   d[i]=i*i

print(d)
