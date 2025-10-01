# Simple Calculator

print("---- Simple Calculator ----")

# Take input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (+, -, *, /): ")

# Perform calculation
if choice == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "*":
    result = num1 * num2
    print(f"\nResult: {num1} × {num2} = {result}")

elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} ÷ {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

else:
    print("\nInvalid operation choice.")