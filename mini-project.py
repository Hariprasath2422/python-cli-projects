# Mini Calculator Program

print("............Mini Calculator..................")

# Get user input for two numbers
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

# Display the menu for operations
print("\nPress 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")

# Get the user choice
select_option = int(input("\nEnter a number between 1-4: "))

# Perform the  arithematic operation based on the user choice
# The f before the string tells Python to evaluate the expressions inside the curly braces {} and insert their values into the string.
if select_option == 1:
    result = num1 + num2
    print(f"The addition of {num1} and {num2}  numbers is: {result}")
elif select_option == 2:
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} numbers is: {result}")
elif select_option == 3:
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} numbers is: {result}")
elif select_option == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} and {num2} numbers is: {result}")
    else:
        print("You can't divide by zero.")
else:
    print("Invalid choice. Please enter a number between 1-4.")



