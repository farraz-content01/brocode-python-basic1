# Chapter 6: Arithmetic Operations & Math Functions

### 📚 What You'll Learn

Master mathematical operations in Python, from basic arithmetic to useful built-in functions!

### 🎯 Learning Objectives

- Understand basic `arithmetic` operators (+, -, \*, /, %, \*\*, //)
- Learn `augmented assignment` operators (+=, -=, \*=, etc.)
- Use built-in `math functions` (round, abs, pow, max, min)
- Apply mathematical operations to solve problems

---

### 📖 Concept Explanation

#### Basic Arithmetic Operators

| Operator | Name           | Example  | Result |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 3`  | `8`    |
| `-`      | Subtraction    | `5 - 3`  | `2`    |
| `*`      | Multiplication | `5 * 3`  | `15`   |
| `/`      | Division       | `6 / 2`  | `3.0`  |
| `//`     | Floor Division | `7 // 2` | `3`    |
| `%`      | Modulus        | `7 % 2`  | `1`    |
| `**`     | Exponentiation | `2 ** 3` | `8`    |

#### Augmented Assignment Operators

These combine an operation with assignmen

```python
x = 10

# Instead of: x = x + 5
x += 5  # Shorter way => x = 10 + 5 = 15 (use increment)

# Instead of: x = x - 3
x -= 3  # Shorter way => x = 15 -3 = 12 (use decrement)

# Instead of: x = x * 2
x *= 2  # Shorter way => x = 12 * 2 = 24

# Instead of: x = x / 4
x /= 4  # Shorter way (x is now 6.0)

# Instead of: x = x ** 2
x **= 2  # Shorter way (x is now 36.0)

# Instead of: x = x % 5
x %= 5  # Shorter way (x is now 1.0)
```

### Built-in Math Functions

#### `round(number)` - Round to Nearest Integer

```python
print(round(3.14))    # Output: 3
print(round(3.7))     # Output: 4
print(round(3.5))     # Output: 4 (rounds to nearest 'even')
print(round(4.5))     # Output: 4 (rounds to nearest 'even')
```

#### `abs(number)` - Absolute Value

```python
print(abs(-5))    # Output: 5
print(abs(5))     # Output: 5
print(abs(-3.14)) # Output: 3.14
```

#### `pow(base, exponent)` - Power

```python
print(pow(2, 3))   # Output: 8 (=2^3)
print(pow(5, 2))   # Output: 25 (=5^2)
print(2 ** 3)      # Output: 8 (alternative syntax)
```

#### `max()` - Maximum Value

```python
print(max(1, 5, 3))        # Output: 5
print(max(10, 20, 15, 8))  # Output: 20
```

#### `min()` - Minimum Value

```python
print(min(1, 5, 3))        # Output: 1
print(min(10, 20, 15, 8))  # Output: 8
```

### 🔍 Important Concepts

#### Division: / vs //

```python
print(7 / 2)   # Regular division: 3.5 (float)
print(7 // 2)  # Floor division: 3 (integer, rounded down)
```

#### Modulus (%) - Remainder

```python
print(10 % 3)  # 1 (10 ÷ 3 = 3 remainder 1)
print(17 % 5)  # 2 (17 ÷ 5 = 3 remainder 2)

# Useful for:
# - Checking even/odd: number % 2 == 0 (even) or 1 (odd)
# - Cycling through values: index % length
```

#### Order (priority) of Operations (PEMDAS)

Python follows mathematical order of operations:

1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication/Division `*`, `/`, `//`, `%`
4. **A**ddition/Subtraction `+`, `-`

```python
result = 2 + 3 * 4      # 14 (not 20) - multiplication first
result = (2 + 3) * 4    # 20 - parentheses first
```

### 📝 Common Use Cases

#### Incrementing/Decrementing

```python
counter = 0
counter += 1  # Increment by 1
counter -= 1  # Decrement by 1
```

#### Doubling/Halving

```python
value = 100
value *= 2  # Double (value = 200)
value /= 2  # Halve (value = 100.0)
```

#### Finding Remainders

```python
# Check if divisible
if number % 5 == 0:
    print("Divisible by 5")
```

### 🚀 Try It Yourself

1. Create a program that calculates `compound interest`
2. Build a `tip calculator` (meal cost + tip percentage)
3. Make a `BMI calculator` (weight / height²)
4. Create a program that finds the `max, min,` and `average` of 5 numbers

### 🔗 Next Chapter

Continue to [Chapter 7: If Statements](../07-if-elif-else/main7.py) to learn about conditional logic!
