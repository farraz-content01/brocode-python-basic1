# %% Try It Yourself 6.1: Temperature Converter
#! --------------------------------------------------------------------------
print("--TIY - 6.1: Temperature Converter--")
celsius = float(input("Enter temperature in Celsius: "))  # casting str to float
print(f"input(celsius): {celsius}")
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: " + str(fahrenheit))  # casting float to str
print("")

# %% Try It Yourself 6.2: Simple Interest Calculator
#! --------------------------------------------------------------------------
print("--Exercise 4: Simple Interest Calculator--")
principal = float(input("Enter principal amount ($): "))  # casting str to float
print(f"input(principal): {principal} $")
interest_rate = float(input("Enter interest rate (%): "))  # casting str to float
print(f"input(interest_rate): {interest_rate} %")
years = int(input("Enter number of years: "))  # casting str to int
simple_interest = (principal * interest_rate * years) / 100
print("Calculated Simple Interest: " + str(simple_interest))  # casting float to str
print("")

# %% Try It Yourself 6.3: Body Mass Index (BMI) Calculator
#! --------------------------------------------------------------------------
print("--Exercise 5: Body Mass Index (BMI) Calculator--")
weight = float(input("Enter weight (kg): "))  # casting str to float
print(f"input(weight): {weight} kg")
height = float(input("Enter height (meters): "))  # casting str to float
print(f"input(height): {height} meters")
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))  # casting float to str
print("")

# %%