# Import os module for handling file paths
import os  

# Automatically locate the file in the same directory as the script
file_path = os.path.join(os.getcwd(), "students.txt")

# Open the "students.txt" file in read mode ("r")
f = open(file_path, "r")

# Read the entire contents of the file
StudDetails = f.read()

# Close the file after reading
f.close()

# Displaying notification-like message
print("Reading Student Information:")

# Display the student information to the user
print(StudDetails)