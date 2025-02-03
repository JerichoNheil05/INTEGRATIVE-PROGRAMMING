# Ask the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the highest number using nested if..elif..else conditions
if num1 >= num2:
    if num1 >= num3:
        highest = num1
    else:
        highest = num3
else:
    if num2 >= num3:
        highest = num2
    else:
        highest = num3

# Display the highest number
print(f"The highest number is: {highest}")
