def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

while True:
    print("\nOptions: + - * /")
    choice = input("Enter operation (or 'q' to quit): ")

    if choice == 'q':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print("Result:", add(num1, num2))
    elif choice == '-':
        print("Result:", subtract(num1, num2))
    elif choice == '*':
        print("Result:", multiply(num1, num2))
    elif choice == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

