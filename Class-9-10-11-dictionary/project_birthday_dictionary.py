Birthdays ={
    "Albert Einstein": "14/3/1889",
    "Bill Gates": "28/10/1955",
    "Steve Jobs": "24/2/1955",
}
print("Welcome to the Birthday game ! We have the birthdays to:")
for x in Birthdays:
    print(x)

choice= input("\nWho's birthday do you want to look up?")

if choice in Birthdays:
    print("The birthday of {} is: ".format(choice))
    print(Birthdays[choice])
else:
    print("We do not have that birthday information.")
    add_birthday=input("Would you like to add Birthday in the list?")
    if add_birthday in "Yes" or "yes":
        name_friend=input("Add name of your friend \t")
        birth_date=input("Add birthday date\t")
        Birthdays.update({name_friend: birth_date})
        print("updated dict:\t", Birthdays)
    else:
        print("Have a gud day !!")

