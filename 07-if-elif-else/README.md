# Chapter 7: If-Elif-Else Statements

### 📚 What You'll Learn

Make your programs smart with conditional logic!
Learn how to make decisions based on different conditions.

### 🎯 Learning Objectives

- Understand `if, elif,` and `else` statements
- Use `comparison operators` (==, !=, >, <, >=, <=)
- Create programs that make `decisions`
- Chain `multiple conditions` together
- Understand the `flow` of conditional execution

### 📖 Concept Explanation

#### What are Conditional Statements?

Conditional statements let your program make decisions and execute different code based on whether conditions are True or False.

#### Syntax

##### Basic If Statement

```python
if condition:
    # This code runs if condition is True
    print("Condition is true!")
```

##### If-Else Statement

```python
if condition:
    # Runs if condition is True
else:
    # Runs if condition is False
```

##### If-Elif-Else Chain

```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False and condition2 is True
elif condition3:
    # Runs if condition1 and condition2 are False, and condition3 is True
else:
    # Runs if all conditions above are False
```

#### Comparison Operators

| Operator | Meaning               | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 3` | `True` |
| `>`      | Greater than          | `5 > 3`  | `True` |
| `<`      | Less than             | `3 < 5`  | `True` |
| `>=`     | Greater than or equal | `5 >= 5` | `True` |
| `<=`     | Less than or equal    | `3 <= 5` | `True` |

### Important: Indentation Matters!

```python
if age >= 18:
    print("Adult")      # Indented - part of if block
    print("Can vote")   # Indented - part of if block
print("Program ends")   # Not indented - always runs
```

## 💡 Examples

### Example 1: Simple If-Else

```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's nice weather!")
```

### Example 2: Multiple Conditions (Elif)

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Example 3: User Authentication

```python
password = input("Enter password: ")

if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")
```

### Example 4: Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```
