# Asking for user input
Fname = input("Enter Your First Name: ")
Lname = input("Enter Your Last Name: ")
age = input("Enter Your Age: ")

# Displaying the input details
# String Concatenation 
FulName = Fname + " " + Lname
print("\nFull Name: ", FulName)

# String Slicing
print("Sliced Name: ", Fname[:4])

# String Formatting
GreetMsg = "Greeting Message: Hello, {}! Welcome. You are {} years old."
print(GreetMsg.format(Fname[:4], age))
