while True:
    num1 = int(input("Enter num1: \t"))
    num2 = int(input("Enter num2: \t"))
    math_operation = input("Enter operation between - add, multiply, divide, diff,remainder, quotient:\t ")
    if math_operation == "add":
        print(num1 + num2)
    elif math_operation=="multiply":
        print(num1*num2)
    elif(math_operation=="diff"):
        print(num1 - num2)
    elif(math_operation=="divide"):
        print(num1/num2)
    elif(math_operation=="remainder"):
        print(num1%num2)
    elif(math_operation=="quotient"):
        print(num1//num2)
    else:
        print("please enter correct option.bye!")
        break
