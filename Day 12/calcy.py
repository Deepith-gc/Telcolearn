num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")

match op:
    case '+':
        print("Result:", num1 + num2)

    case '-':
        print("Result:", num1 - num2)

    case '*':
        print("Result:", num1 * num2)

    case '/':
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

    case _:
        print("Invalid operator")
