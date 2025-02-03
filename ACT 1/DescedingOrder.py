# Ask the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the order of the numbers using nested if..elif..else conditions
if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            order = [num1, num2, num3]
        else:
            order = [num1, num3, num2]
    else:
        order = [num3, num1, num2]
else:
    if num2 >= num3:
        if num1 >= num3:
            order = [num2, num1, num3]
        else:
            order = [num2, num3, num1]
    else:
        order = [num3, num2, num1]

# Display's the numbers in descending order
print(f"The numbers in descending order are: {order}")
