# ============================================
# Chapter 8: Simple Calculator Program - Revision 1
# ============================================

# %%
# Create a menu-driven program for continuous calculation - use while loop
while True:
    #! --- calculator code - start here ---

    # 1.display menu
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # 2.user input - choose operator
    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("=> Goodbye!")
        break    #TODO: exit the loop

    # 3.user input - get data (numbers)
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue    #TODO: back to step 2

    # 4. perform the requested operation
    if choice == 1:
        opr = "+"
        result = num1 + num2
    elif choice == 2:
        opr = "-"
        result = num1 - num2
    elif choice == 3:
        opr = "*"
        result = num1 * num2
    elif choice == 4:
        opr = "/"
        result = num1 / num2
    else:
        print("Invalid choice. Please try again.")
        continue    #TODO: back to step 2

    # 5. display the result
    print("# Selected operator:", opr)
    print(f"=> Result: {num1} {opr} {num2} = {result}")

    #! --- calculator code - end here ---
    print()

    # 6. ask user if they want to continue
    continue_calc = input("Do you want to continue? (Y/N): ")
    if continue_calc.lower() != "y":   # if user input is not 'Y'
        print("Goodbye!")
        break    #TODO: exit the loop

    #NOTE: use lower() to handle both 'Y' and 'y'
# %%
