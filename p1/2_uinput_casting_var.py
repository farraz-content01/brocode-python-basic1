# %% P1.3. Type Casting
# Type Casting is the process of converting one data type to another data type
name = "Bro Code"
age = 21
gpa = 3.2
is_student = True

print("--Example 1: display 'Data Types'--")
print("type(name): ",type(name))      # type(name):  <class 'str'> 
print("type(age): ",type(age))       # type(age):  <class 'int'> 
print("type(gpa): ",type(gpa))       # type(gpa):  <class 'float'>
print("type(is_student): ",type(is_student))  # type(is_student):  <class 'bool'>

print("\n--Example 2: use Type Casting--")
print("Name: " + name)       # output: Name: Bro Code

print("Cast: int-to-float => float(age): ",float(age)) 
print("Cast: int-to-str => str(age): " + str(age)) 
print("Cast: int-to-float-to-str => str(float(age)): " + str(float(age)))

print("Cast: float-to-str => str(gpa): " + str(gpa))
print("Cast: float-to-int => int(gpa): ",int(gpa))

print("Cast: bool-to-str => str(is_student): " + str(is_student))  # casting bool to str
print("")

# %% P1.4. User Input
#! NOTE: input() returns a str - so we need to cast it to the desired type
print("--Example 3: User Input and Casting--")
name = input("Enter your name: ")  #? input() returns a str
age = int(input("Enter your age: "))  # casting str to int
# age = int(age)  # casting str to int
age = age + 1  # after casting (str > int), NOW we can do MATH operations

#! Different ways to print the output
print("Hello " + name + "! Next year, you will be " + str(age) + " years old.")
print(f"Hello {name}! Next year, you will be {age} years old.")  # using f-strings  
#? f-strings -- available in Python 3.6+ > used for STRING interpolation
print("Hello {}! Next year, you will be {} years old.".format(name, age))  # using str.format() method
print("Hello %s! Next year, you will be %d years old." % (name, age))  # using str.format() method  
print("") # New line for better readability

# %%
print("--Example 4: Input > (length + width) > Rectangle Area--")
#! NB: input() returns a str - need to cast it to the 'int' / 'float' for MATH operations
length = float(input("Enter length: "))  # casting str to float 
width = float(input("Enter width: "))  # casting str to float
print(f"input(length): {length}, input(width): {width}")

area = length * width
print("Total Area: length x width => str(area): " + str(area))  # casting float to str

# %%
print("--Example 5: Input > (item name + price + quantity) > Total Payment--")
item1 = input("Enter item 1: ")
price1 = float(input("Enter price of item 1: "))  # casting str to float
quantity1 = int(input("Enter quantity of item 1: "))  # casting str to int

Total_cost1 = price1 * quantity1 #? float * int = float
print("Total payment for " + item1 + " => $" + str(Total_cost1))  # casting float to str
print(f"You have bought {quantity1} x {item1}(s) => Total payment: ${Total_cost1}")
print("")

# %%
""""
print("--Exercise 3: Temperature Converter--")
celsius = float(input("Enter temperature in Celsius: "))  # casting str to float
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: " + str(fahrenheit))  # casting float to str
print("")

print("--Exercise 4: Simple Interest Calculator--")
principal = float(input("Enter principal amount: "))  # casting str to float
interest_rate = float(input("Enter interest rate: "))  # casting str to float
years = int(input("Enter number of years: "))  # casting str to int
simple_interest = (principal * interest_rate * years) / 100
print("Simple Interest: " + str(simple_interest))  # casting float to str
print("")

print("--Exercise 5: Body Mass Index (BMI) Calculator--")
weight = float(input("Enter weight in kg: "))  # casting str to float
height = float(input("Enter height in meters: "))  # casting str to float
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))  # casting float to str
print("")
"""
# %%
