name = "Bro Code"
age = 21
gpa = 3.2
is_student = True

print("--Data Types--")
print("type(name): ",type(name))      # type(name):  <class 'str'> 
print("type(age): ",type(age))       # type(age):  <class 'int'> 
print("type(gpa): ",type(gpa))       # type(gpa):  <class 'float'>
print("type(is_student): ",type(is_student))  # type(is_student):  <class 'bool'>

print("--Casting--")
print("Name: " + name)       # printing str > Name: Bro Code

print("Age: ",float(age))  # casting int to float > Age:  21.0
print("Age: " + str(age))  # casting int to str > Age:  21
print("Age: " + str(float(age)))  # casting int to float to str > Age:  21.0

print("GPA: " + str(gpa))    # casting float to str > GPA:  3.2
print("GPA: ",int(gpa))    # casting float to int > GPA:  3

print("Student: " + str(is_student))  # casting bool to str
print("")

#TODO: Exercise 0 - user input and casting
#! NOTE: input() returns a str - so we need to cast it to the desired type
print("--Exercise 0: User Input and Casting--")
name = input("Enter your name: ")  # input() returns a str
age = int(input("Enter your age: "))  # casting str to intArkan
# age = int(age)  # casting str to int
age = age + 1  # after casting (str > int), NOW we can do MATH operations

#! Different ways to print the output
print("Hello " + name + "! Next year, you will be " + str(age) + " years old.")
print(f"Hello {name}! Next year, you will be {age} years old.")  # using f-strings  
print("Hello {}! Next year, you will be {} years old.".format(name, age))  # using str.format() method
print("Hello %s! Next year, you will be %d years old." % (name, age))  # using str.format() method  
print("")

print("--Exercise 1: Rectangle Area Calc--")
#! NB: input() returns a str - need to cast it to the 'int' / 'float' for MATH operations
length = float(input("Enter length: "))  # casting str to float 
width = float(input("Enter width: "))  # casting str to float

area = length * width
print("Total Area: " + str(area))  # casting float to str
print("")

print("--Exercise 2: Shopping Cart Program--")
item1 = input("Enter item 1: ")
price1 = float(input("Enter price of item 1: "))  # casting str to float
quantity1 = int(input("Enter quantity of item 1: "))  # casting str to int

Total_cost1 = price1 * quantity1
print("Total payment for " + item1 + " => $" + str(Total_cost1))  # casting float to str
print(f"You have bought {quantity1} x {item1}(s) => Total payment: ${Total_cost1}")
print("")

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