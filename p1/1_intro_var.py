# using Nested if statements
is_student = False
for_sale = False
is_online = True

print("--using Nested if statements--")
if for_sale:
    print("This item is for sale.")
elif is_student:
    print("This item is for students.")
elif is_online:
    print("This item is available online.")
else:
    print("This item is not available.")

print("\n--using Logical Operators--")
if for_sale or is_student or is_online:
    print("This item is available.")
else:
    print("This item is not available.")

