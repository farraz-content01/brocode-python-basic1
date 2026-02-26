# ============================================
# Chapter 8: Simple Calculator Program
# ============================================
# This program demonstrates how to build a 'basic calculator'
# using user input and conditional statements

# %%
#TODO: 1.Get the operator from user
# Ask user which mathematical operation they want to perform
operator = input("Enter an operator (+, -, *, /, %, //): ")

#TODO: 2.Get the numbers from user
# Get two numbers and convert them to floats (to handle decimals)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#TODO: 3.Perform the requested operation
# Use if-elif-else to determine which operation to perform
if operator == "+":     # Addition
    print("Selected operation: addition")
    result = num1 + num2
elif operator == "-":   # Subtraction
    print("Selected operation: subtraction")
    result = num1 - num2
elif operator == "*":   # Multiplication
    print("Selected operation: multiplication")
    result = num1 * num2
elif operator == "/":   # Division
    print("Selected operation: division")
    result = num1 / num2
elif operator == "%":   # Modulo (remainder) = modulus
    print("Selected operation: modulo")
    result = num1 % num2
elif operator == "//":  # Integer division = floor division (rounds down)
    print("Selected operation: integer division")
    result = num1 // num2
else:
    print(f"Invalid operator: {operator}")
    exit()

#TODO: 4.Print the result
print(f"- Running calc: {num1} {operator} {num2} = {result}")   

# %%

# NOTE: 
# We use float() instead of int() to handle both 'whole numbers' (int) and 'decimals'