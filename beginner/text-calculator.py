# Simple Python Calculator with Error Handling

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mutiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."
    
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please ener a number.")
            
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if the choice is valid
if choice in ['1','2','3','4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {mutiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input. Please restart the program and select a valid operation.")