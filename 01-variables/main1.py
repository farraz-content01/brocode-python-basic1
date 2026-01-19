# %% P1.2. Variable - Introduction
# Variable is a named container that holds a value of a certain data type:
# - type: str, int, float, bool, etc
# - Python is a "dynamically typed" language

name = "Bro Code"   # type: str
age = 21    # type: int
gpa = 3.2   # type: float
is_student = True   # type: bool

# %% P1.2.1 Using variables - in Nested "if" statements
is_student = False
for_sale = False
is_online = True

print("--Example 1: using Nested if statements--")
if for_sale: # if for_sale == True
    print("This item is for sale.")
elif is_student:
    print("This item is for students.")
elif is_online:
    print("This item is available online.")
else:
    print("This item is not available.")

print("\n--Example 2: using Logical Operators--")
if for_sale or is_student or is_online:
    print("This item is available.")
else:
    print("This item is not available.")

# %% P1.2.2 Using variables - with type declaration
first_name: str = "Bro Code"
age: int = 21
gpa: float = 3.2
is_student: bool = True
email: str = "VtXbG@example.com"

print("--Example 3: using type declaration--")
print("first_name: str => ", first_name)
print("age: int => ", age)
print("gpa: float => ", gpa)
print("is_student: bool => ", is_student)
print("email: str => ", email)

# %%
