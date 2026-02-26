# Chapter 8: Simple Calculator Program

### 📚 What You'll Learn
Build a functional calculator that performs basic mathematical operations!

### 🎯 Learning Objectives
- Combine user input with conditional statements
- Create a menu-driven program
- Handle different mathematical operations
- Validate user input
- Build a complete, useful program

---

### 📖 Concept Explanation

#### What is a Calculator Program?
A **calculator** program:
  1. Asks the user what operation they want to perform
  2. Gets the numbers to calculate
  3. Performs the requested operation
  4. Displays the result

### Program Flow
```
1. Display available operators 
    → 2. Get operator choice 
    → 3. Get numbers 
    → 4. Check operator and calculate → 5. Display result
```
---

## 💡 Complete Program Breakdown

### Step 1: Get Operator

### Step 2: Get Numbers

### Step 3: Calculate Based on Operator

---

## ✍️ Practice Exercises

### Exercise 1: Add Division by Zero Check
```python
elif operator == "/":
    if number2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"{number1} / {number2} = {number1 / number2}")
```
### Exercise 2: Add More Operations
Add these operators:
- `**` for exponentiation (power)
- `//` for floor division
- `sqrt` for square root

### Exercise 3: Continuous Calculator
Make the calculator run in a loop until user chooses to exit:
```python
while True:
    #! --- calculator code - start here ---

    # 1.display menu
    # 2.user input - choose operator
    # 3.user input - get data (numbers)
    # 4. perform the requested operation
    # 5. display the result
    print("# Selected operator:", opr)
    print(f"=> Result: {num1} {opr} {num2} = {result}")

    #! --- calculator code - end here ---
    print()

    # 6. ask user if they want to continue
    continue_calc = input("Another calculation? (yes/no): ")
    if continue_calc.lower() != "yes":  # if user input is not 'Y'
        print("Goodbye!")
        break
```

### Exercise 4: Calculator with Memory
Store the last result and allow using it in next calculation:
```python
memory = 0
# Allow user to type "M" to use memory value
```

---

## 🔍 Enhancements

### Enhancement 1: Better Output Formatting
```python
if operator == "+":
    result = number1 + number2
    print(f"\n{number1} + {number2} = {result}")
    print(f"Result: {result:.2f}")  # 2 decimal places
```

### Enhancement 2: Input Validation
```python
valid_operators = ['+', '-', '*', '/', '%']

if operator not in valid_operators:
    print("Invalid operator!")
```

### Enhancement 3: Try-Except for Error Handling
```python
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numbers!")
```

---

## 🎮 Advanced Calculator Features

### Feat 1: Scientific Calculator
```python
import math

if operator == "sqrt":
    result = math.sqrt(number1)
elif operator == "sin":
    result = math.sin(math.radians(number1))
elif operator == "cos":
    result = math.cos(math.radians(number1))
```

### Feat 2: Calculator with History
```python
history = []

# After each calculation:
history.append(f"{number1} {operator} {number2} = {result}")

# Display history:
for calc in history:
    print(calc)
```

## 📝 Common Operators Explained

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 2` | `3.0` |
| `%` | Modulus | `7 % 2` | `1` |
| `**` | Power | `2 ** 3` | `8` |
| `//` | Floor Division | `7 // 2` | `3` |

---

## 🚀 Challenge Projects

### Challenge 1: Multi-Step Calculator
```python
# Allow: 5 + 3 * 2 - 1
# Parse and calculate following order of operations
```

### Challenge 2: Unit Converter
Add conversions:
- Temperature (C to F, F to C)
- Length (miles to km, km to miles)
- Weight (lbs to kg, kg to lbs)

### Challenge 3: Percentage Calculator
```python
# Calculate:
# - What is X% of Y?
# - X is what % of Y?
# - Percentage increase/decrease
```

### Challenge 4: GUI Calculator
Use tkinter to create a calculator with buttons:
```python
import tkinter as tk
# Create calculator with button interface
```

## 💻 Complete Enhanced Calculator
```python
def calculator():
    print("=== Simple Calculator ===")
    print("Operations: +, -, *, /, %, **, //")
    
    operator = input("\nEnter operator: ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        elif operator == "%":
            result = num1 % num2
        elif operator == "**":
            result = num1 ** num2
        elif operator == "//":
            result = num1 // num2
        else:
            print("Invalid operator!")
            return
        
        print(f"\n{num1} {operator} {num2} = {result}")
        print(f"Result: {result:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run calculator
calculator()
```

## 🔗 Next Chapter
Continue to [Chapter 9: Weight Converter](../9-weight/) to build another practical conversion program!
