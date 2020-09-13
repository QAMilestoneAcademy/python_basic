# # Iterate over dictionaries using for loops
d = {'x': 10, 'y': 20, 'z': 30}

for element in d.items():
    print(element)
#
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)
#
# # Generate and print a dictionary that contains a number in the form (x, x*x)
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print("dictionary for first {} number & squares".format(n),d)
#
# # Python Program to multiply all the items in a dictionary.
#
d={'A':10,'B':10,'C':239}
tot=1
for i in d:
    tot=tot*d[i]
print(tot)