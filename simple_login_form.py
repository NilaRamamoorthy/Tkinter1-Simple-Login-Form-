import tkinter as tk
from tkinter import messagebox

def submit():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}")
    print(f"Password: {password}")
    messagebox.showinfo("Login Info", f"Username: {username}\nPassword: {password}")

def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")  # Set window size

# Create Labels
username_label = tk.Label(root, text="Username:", font=("Arial", 12))
password_label = tk.Label(root, text="Password:", font=("Arial", 12))

# Create Entry widgets
username_entry = tk.Entry(root, width=25)
password_entry = tk.Entry(root, width=25, show="*")  # hides password input

# Create Buttons
submit_button = tk.Button(root, text="Submit", command=submit, bg="lightblue")
reset_button = tk.Button(root, text="Reset", command=reset, bg="lightgray")

# Place widgets using grid layout
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button.grid(row=2, column=0, padx=10, pady=20)
reset_button.grid(row=2, column=1, padx=10, pady=20)

# Start Tkinter event loop
root.mainloop()
