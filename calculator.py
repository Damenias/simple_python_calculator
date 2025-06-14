# Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print("Welcome to the simple calculator")
print("Operations you can perform: + (adding), - (subtracting), * (multiplying), / (dividing)")
print("Note: After 3 operations, you will unlock operand 'P'. Let's check what it does!")

operation_count = 0

while True:
    try:
        if operation_count >= 3:
            print("\n🎉 You've unlocked the secret operator! 🎉")
            operator = input("Enter 'P' to reveal your surprise")
            if operator == 'P':
                print(r"""
         ____
        / . .\
       \  ---<
        \  /
   ______/ /
  <______/  
  Ssssss... I'm a friendly snake! 
  Thank you for visiting me :3
                """)
                choice = input("Do you want to return to the calculator? (yes/no): ").strip().lower()
                if choice == "yes":
                    continue  # Go back to the start of the loop
                else:
                    print("Thanks for using the calculator! Goodbye 🐍💖")
                    break
            elif operator not in ['+', '-', '*', '/']:
                print("Invalid operator.")
                continue
        else:
            operator = input("\nEnter operation (+, -, *, /): ").strip()

            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator.")
                continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        print("Result:", result)
        operation_count += 1

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
