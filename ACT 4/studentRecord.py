# Function to calculate the final grade based on class standing (60%) and major exam (40%)
def calculate_final_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

# Function to load student records from a file
def load_records(filename):
    records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                records.append((parts[0], (parts[1], parts[2]), float(parts[3]), float(parts[4])))
    except FileNotFoundError:
        print('File not found. Starting with an empty record.')
    return records

# Function to save student records to a file
def save_records(records, filename):
    with open(filename, 'w') as file:
        for record in records:
            file.write(f'{record[0]},{record[1][0]},{record[1][1]},{record[2]},{record[3]}\n')

# Function to save records with a new filename
def save_as_file(records):
    filename = input('Enter filename: ')
    save_records(records, filename)
    print(f'Records saved as {filename}')

# Function to sort records by last name
def order_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

# Function to sort records by calculated final grade
def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_final_grade(x[2], x[3]), reverse=True)

# Function to display all student records with sorting options
def display_records(records):
    if not records:
        print("No student records available.")
        return

    print("\nHow would you like to display the records?")
    print("1. Order by Last Name")
    print("2. Order by Grade")
    choice = input("Enter your choice: ")

    if choice == '1':
        records = order_by_last_name(records)
    elif choice == '2':
        records = order_by_grade(records)
    else:
        print("Invalid choice. Displaying records ordered by last name by default.")
        records = order_by_last_name(records)

    # Display formatted records
    print(f"\n{'ID':<10}{'Name':<25}{'Class Standing':<15}{'Major Exam':<12}{'Final Grade':<12}")
    print("-" * 70)

    for record in records:
        student_id, (first_name, last_name), class_standing, major_exam = record
        final_grade = calculate_final_grade(class_standing, major_exam)
        print(f"{student_id:<10}{first_name + ' ' + last_name:<25}{class_standing:<15.2f}{major_exam:<12.2f}{final_grade:<12.2f}")

# Function to add a new student record
def add_record(records):
    student_id = input('Enter Student ID (6 digits): ')
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    class_standing = float(input("Class Standing: "))
    major_exam = float(input("Major Exam: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))

# Function to edit an existing student record
def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input(f"New First Name ({record[1][0]}): ").strip() or record[1][0]
            last_name = input(f"New Last Name ({record[1][1]}): ").strip() or record[1][1]
            class_standing = float(input(f"New Class Standing ({record[2]}): ") or record[2])
            major_exam = float(input(f"New Major Exam ({record[3]}): ") or record[3])
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated.")
            return
    print("Record not found.")

# Function to delete a student record
def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted.")
            return
    print("Record not found.")

# Function to show a specific student's record
def show_student_record(records):
    student_id = input("Enter Student ID: ")
    for record in records:
        if record[0] == student_id:
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Final Grade: {calculate_final_grade(record[2], record[3]):.2f}")
            return
    print("Record not found.")

# Main menu function
def main():
    filename = "students.txt"
    records = load_records(filename)

    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Records")  
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            records = load_records(filename)
            print("File opened.")
        elif choice == '2':
            save_records(records, filename)
            print("Records saved.")
        elif choice == '3':
            save_as_file(records)
        elif choice == '4':
            display_records(records)  
        elif choice == '5':
            show_student_record(records)
        elif choice == '6':
            add_record(records)
        elif choice == '7':
            edit_record(records)
        elif choice == '8':
            delete_record(records)
        elif choice == '9':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()