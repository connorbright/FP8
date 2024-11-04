import sqlite3

# Create a database file and table
def create_database():
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (name TEXT, email TEXT, message TEXT)''')
    conn.commit()
    conn.close()

# Insert feedback into the database
def insert_feedback(name, email, message):
    conn = sqlite3.connect('customer_feedback.db')
    c = conn.cursor()
    c.execute('''INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)''', (name, email, message))
    conn.commit()
    conn.close()
import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get("1.0", "end-1c")

    if name and email and message:
        insert_feedback(name, email, message)
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_message.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def display_feedback():
    password = input("Enter password to access feedback: ")
    if password == "secretpassword":  # Replace "secretpassword" with your actual password
        conn = sqlite3.connect('customer_feedback.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM feedback''')
        all_feedback = c.fetchall()
        for entry in all_feedback:
            print(f"Name: {entry[0]}, Email: {entry[1]}, Message: {entry[2]}")
        conn.close()
    else:
        print("Access Denied!")

create_database()

# Create the main application window
root = tk.Tk()
root.title("Customer Feedback")

# Create input fields
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Feedback:").grid(row=2, column=0)
entry_message = tk.Text(root, height=5, width=30)
entry_message.grid(row=2, column=1)

# Create buttons
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=1)

display_button = tk.Button(root, text="Display Feedback", command=display_feedback)
display_button.grid(row=4, column=1)

# Start the main event loop
root.mainloop()
