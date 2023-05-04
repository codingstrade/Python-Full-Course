while True:
    num1 = input("Enter the first number or press Type 'q' to quit: ")
    if num1 == 'q':
        break
    num1 = float(num1)
    operator = input("Enter an operator (+, -, * or /) or press Type 'q' to quit: ")
    if operator == 'q':
        break
    num2 = input("Enter the second number or press Type 'q' to quit: ")
    if num2 == 'q':
        break
    num2 = float(num2)

    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print('you cant divid a digit by zero')
            continue
        else:
            result = num1 / num2
    else:
        print("Invalid Operator")

    print("The result is: ", result)