known_users = ["Shrek", "Donkey", "Fiona", "Patrick", "Bob", "Joe"]


while True:
    print("Hi my name Travis")
    name = input("What is your name? \t ")
    name = name.strip().capitalize()
    print(name)
    if name in known_users:
        print("Hello {}".format(name))
        stay = input("Would you like to stay? \t")
        stay = stay.strip().capitalize()
        if stay == "No":
            known_users.remove(name)
            print("You are not in the system anymore \t")
            print(known_users)
    elif name not in known_users:
        print("Sorry {} you are not in the list ".format(name))
        enter = input("Would you like to enter the system? \t")
        enter=enter.strip().capitalize()

        if enter == "Yes":
         known_users.append(name)
         print("Welcome to the system! \t")
         print(known_users)
        else:
         print("have a good day \t")
