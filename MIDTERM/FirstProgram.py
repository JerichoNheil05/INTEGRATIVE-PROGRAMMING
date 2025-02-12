def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename) as file:
            for i, line in enumerate(file, 1):
                numbers = list(map(int, line.strip().split(',')))
                total = sum(numbers)
                print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {'Palindrome' if is_palindrome(total) else 'Not a palindrome'}")
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data format.")

process_file(r"C:\Users\colin\OneDrive\Documents\TSA1-1\MIDTERM\numbers.txt")