# Asking for user input
Fname = input("Enter First Name: ")
Lname = input("Enter Last Name: ")
age = input("Enter Age: ")
num = input("Enter Contact Number: ")
course = input("Enter Course: ")

# Store student information in a list for easy formatting
StudInfo = f"Last Name: {Lname}\nFirst Name: {Fname}\nAge: {age}\nContact Number: {num}\nCourse: {course}"


# Open a file named students.txt in append mode and write the formatted info to the file
with open("students.txt", "a") as f:
    f.write(StudInfo)

# Display a confirmation message to the user
print("\nStudent information has been saved to 'students.txt'.")