# Function to check if a number is prime
def is_prime(number):
    # A prime number must be greater than 1
    if number <= 1:
        return False
    
    # Check for factors from 2 to the square root
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

#enter a number
input_number = int(input("Enter a number: "))

# Check if the input number is prime and display the result
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")
