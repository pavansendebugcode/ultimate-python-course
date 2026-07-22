
# Question 1: Create a simple calculator 

a = int(input('Enter your first number = '))
b = int(input('Enter your second number = '))
c = input('What do you want to do (+, -, *, /, %) = ')

if c == "+" :
    print("The addition is", a + b)

elif c == "-":
    print("The subtraction is", a - b)

elif c == "*":
    print("The multiplication is", a * b)

elif c == "/":
    if b != 0:
        print("The division is", a / b)
    else:
        print("Error: Division by zero is not allowed.")

elif c == "%":
    if b != 0:
        print("The remainder is", a % b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. ")

    print("Try again next time")

    89