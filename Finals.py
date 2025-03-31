# Module 01. Intro to Python Programming
import tkinter as tk
from tkinter import ttk, messagebox

# Module 02. Python Programming Fundamentals
# Global list to store records
records = []

from tkinter import ttk
import tkinter as tk

from tkinter import ttk, Canvas
import tkinter as tk

from tkinter import ttk, Canvas
import tkinter as tk

def set_theme():
    style = ttk.Style()
    style.theme_use("clam")  # Modern look

    # Monochromatic Shades of Blue-Gray
    bg_color = "#2C3E50"  # Dark blue-gray
    light_gray = "#34495E"  # Medium shade
    highlight_color = "#5D6D7E"  # Light accent
    text_color = "#ECF0F1"  # Off-white for readability

    # Background and text color
    style.configure("TFrame", background=bg_color)
    style.configure("TLabel", background=bg_color, foreground=text_color, font=("Poppins", 12))
    style.configure("TEntry", font=("Poppins", 12), fieldbackground=light_gray, foreground=text_color)

    # Buttons (Rounded)
    style.configure("Rounded.TButton",
                    font=("Poppins", 12, "bold"),
                    background=light_gray,
                    foreground=text_color,
                    borderwidth=0,
                    relief="flat")

    style.map("Rounded.TButton", background=[("active", highlight_color)])

    # Navigation (TMenubutton)
    style.configure("TMenubutton",
                    font=("Poppins", 12),
                    background=bg_color,
                    foreground=text_color,
                    borderwidth=0,
                    padding=0)  # Removed padding

    # Custom Circular Tabs for Notebook
    style.configure("TNotebook", background=bg_color, borderwidth=0)
    style.configure("TNotebook.Tab",
                    padding=[10, 5],
                    borderwidth=0,
                    background=light_gray,
                    foreground=text_color,
                    font=("Poppins", 12, "bold"))

    # Remove highlight effect on tab text
    style.map("TNotebook.Tab",
              background=[("selected", highlight_color), ("active", light_gray)],
              foreground=[("selected", text_color), ("active", text_color)])

def create_circular_tab(parent, notebook, title, frame):
    """Creates a circular tab using a Canvas and places it in the notebook."""
    canvas = Canvas(parent, width=80, height=30, bg="#2C3E50", highlightthickness=0)
    canvas.create_oval(5, 5, 75, 30, fill="#34495E", outline="#34495E")
    notebook.add(frame, text=title)




# Module 03. String and File Handling
# Function to handle sign-up and add new records
def sign_up():
    def save_record():
        first_name = entry_first_name.get().strip()
        middle_name = entry_middle_name.get().strip()
        last_name = entry_last_name.get().strip()
        birthday = entry_birthday.get().strip()
        gender = gender_var.get()

        # Simple validation
        if not first_name or not last_name or not birthday or not gender:
            messagebox.showerror("Error", "All fields are required")
            return
        
        record = {
            'First Name': first_name,
            'Middle Name': middle_name,
            'Last Name': last_name,
            'Birthday': birthday,
            'Gender': gender
        }

        records.append(record)
        messagebox.showinfo("Success", "Record added successfully!")
        sign_up_window.destroy()

    # Moodule 04. Collections
    # Creating the sign-up form window
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x350")
    sign_up_window.configure(bg="#2E2E2E")

    frame = ttk.Frame(sign_up_window, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="First Name:").grid(row=0, column=0, sticky="w")
    ttk.Label(frame, text="Middle Name:").grid(row=1, column=0, sticky="w")
    ttk.Label(frame, text="Last Name:").grid(row=2, column=0, sticky="w")
    ttk.Label(frame, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0, sticky="w")
    ttk.Label(frame, text="Gender:").grid(row=4, column=0, sticky="w")

    entry_first_name = ttk.Entry(frame, width=40)
    entry_middle_name = ttk.Entry(frame, width=40)
    entry_last_name = ttk.Entry(frame, width=40)
    entry_birthday = ttk.Entry(frame, width=40)

    gender_var = tk.StringVar()
    gender_male = ttk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
    gender_female = ttk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")

    entry_first_name.grid(row=0, column=1, pady=5)
    entry_middle_name.grid(row=1, column=1, pady=5)
    entry_last_name.grid(row=2, column=1, pady=5)
    entry_birthday.grid(row=3, column=1, pady=5)
    gender_male.grid(row=4, column=1, sticky="w")
    gender_female.grid(row=5, column=1, sticky="w")

    save_button = ttk.Button(frame, text="Save", command=save_record)
    save_button.grid(row=6, column=0, columnspan=2, pady=15)

# Module 05. Functions
# Function to view all records
def view_records():
    records_window = tk.Toplevel(root)
    records_window.title("View Records")
    records_window.geometry("500x350")
    records_window.configure(bg="#2E2E2E")

    frame = ttk.Frame(records_window, padding=10)
    frame.pack(fill="both", expand=True)

    if not records:
        ttk.Label(frame, text="No records available", foreground="red").pack()
        return

    canvas = tk.Canvas(frame, bg="#2E2E2E")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for record in records:
        ttk.Label(scrollable_frame, text=f"{record['First Name']} {record['Middle Name']} {record['Last Name']} - {record['Birthday']} - {record['Gender']}", background="#2E2E2E", foreground="white").pack(pady=2)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

# Module 06. Object-Oriented Programming (OOP)
# Function to search a record
def search_record():
    def perform_search():
        search_term = search_entry.get().strip().lower()
        results = [record for record in records if search_term in record['First Name'].lower() or search_term in record['Last Name'].lower()]

        if not results:
            messagebox.showinfo("No Results", "No records found.")
            return

        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.geometry("400x300")
        result_window.configure(bg="#2E2E2E")

        frame = ttk.Frame(result_window, padding=10)
        frame.pack(fill="both", expand=True)

        for record in results:
            ttk.Label(frame, text=f"{record['First Name']} {record['Middle Name']} {record['Last Name']} - {record['Birthday']} - {record['Gender']}", background="#2E2E2E", foreground="white").pack(pady=2)

    # Creating the search window
    search_window = tk.Toplevel(root)
    search_window.title("Search Record")
    search_window.geometry("350x150")
    search_window.configure(bg="#2E2E2E")

    frame = ttk.Frame(search_window, padding=10)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Enter First or Last Name:").pack()
    search_entry = ttk.Entry(frame, width=30)
    search_entry.pack(pady=5)
    
    search_button = ttk.Button(frame, text="Search", command=perform_search)
    search_button.pack(pady=10)

# Module 07. Graphics and Image Processing
# Function to exit the program
def exit_program():
    root.quit()

# Module 08. Graphical User Interface (GUI)
# Main Window
root = tk.Tk()
root.title("Record Management System")
root.geometry("450x300")
root.configure(bg="#2E2E2E")

set_theme()

# Title Section
title_label = ttk.Label(root, text="Record Management System", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Operations Frame
operations_frame = ttk.Frame(root, padding=10)
operations_frame.pack()

ttk.Button(operations_frame, text="Sign Up", command=sign_up, width=40).grid(row=0, column=0, pady=5, padx=5)
ttk.Button(operations_frame, text="View All Records", command=view_records, width=40).grid(row=1, column=0, pady=5, padx=5)
ttk.Button(operations_frame, text="Search Record", command=search_record, width=40).grid(row=2, column=0, pady=5, padx=5)
ttk.Button(operations_frame, text="Exit", command=exit_program, width=40).grid(row=3, column=0, pady=5, padx=5)

# Start main loop
root.mainloop()