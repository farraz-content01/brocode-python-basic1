# %%
import math

pi = math.pi # Accessing the value of pi from the math module
print("Value of pi:", pi)

print("\n--Example 1: Using various Built-in math functions--")
# using f-string to print math function results => to avoid multiple print statements

print(f"Square root of 16: {math.sqrt(16)}") # Square root of 16: 4.0
print(f"Sine of 90 degrees: {math.sin(pi / 2)}") # sine of 90 degrees (pi/2 radians)
print(f"Logarithm base 10 of 100: {math.log(100, 10)}") # logarithm base 10 of 100: 2.0 => log10(100)
print(f"Factorial of 5: {math.factorial(5)}") # factorial of 5: 120 => 5*4*3*2*1
print(f"Floor value of 4.7: {math.floor(4.7)}") # floor value of 4.7: 4 => largest integer less than or equal to 4.7
print(f"Ceiling value of 4.3: {math.ceil(4.3)}") # ceiling value of 4.3: 5 => smallest integer greater than or equal to 4.3
print(f"Power of 2 raised to 3: {math.pow(2, 3)}") # 2 raised to the power of 3: 8.0 => 2*2*2
print(f"Absolute value of -10: {math.fabs(-10)}") # absolute value of -10: 10.0 
print(f"Greatest common divisor of 48 and 18: {math.gcd(48, 18)}") # GCD of 48 and 18: 6
print(f"Least common multiple of 4 and 5: {math.lcm(4, 5)}") # LCM of 4 and 5: 20
print(f"Radians of 180 degrees: {math.radians(180)}") # converting degrees to radians: 3.141592653589793
print(f"Degrees of pi radians: {math.degrees(pi)}") # converting radians to degrees: 180.0
print(f"Exponential of 2: {math.exp(2)}") # exponential of 2: 7.38905609893065 => e^2

# %%
import math

print("--Example 2: Using math constants--")
print(f"Value of Euler's number (e): {math.e}") # Value of Euler's number (e): 2.718281828459045
print(f"Value of Golden Ratio (phi): {math.pi}") # Value of Golden Ratio (phi): 1.618033988749895
print(f"Value of Tau (τ): {math.tau}") # Value of Tau (τ): 6.283185307179586

# %% 
print("--Example 3: Caculate the circumference and area of a circle--")
# circumference = 2 * pi * r
# area = pi * r^2
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * pi * radius
area = pi * math.pow(radius, 2)
print(f"Circumference of the circle with radius {radius}: {circumference}")
print(f"Area of the circle with radius {radius}: {area}")

# %%
print("--Example 4: Caculate the side of triangle--")
# Using the Pythagorean theorem: a^2 + b^2 = c^2
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = math.hypot(side_a, side_b)  # Calculate hypotenuse
print(f"Length of hypotenuse (side c): {side_c}")

# %%