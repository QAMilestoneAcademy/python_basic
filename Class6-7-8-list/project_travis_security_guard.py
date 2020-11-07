known_users = ["Shrek", "Donkey", "Fiona", "Patrick", "Bob", "Joe"]
print("Hi my name Travis")
name = input("What is your name? ")

name=name.strip().capitalize()
print(name)

if name in known_users:
    print("Hello {}.How are you".format(name))
    stay=input("Would you like to stay in the list-Yes/No: ")
    stay=stay.strip().capitalize()
    print(stay)
    if stay=="No":
     known_users.remove(name)
     print(known_users)
#
# elif name not in known_users:
#     print("Sorry {} you are not in the list ".format(name))
#     enter = input("Would you like to enter the system? ")
#     enter=enter.strip().capitalize()
#
#     if enter == "Yes":
#      known_users.append(name)
#      print("Welcome to the system! \t")
#      print(known_users)
#     else:
#      print("have a good day \t")
