import tkinter as tk
from tkinter import messagebox
import pyodbc

# Define the connection string
connection_string = 'Driver={SQL Server};Server=PRATHAM;Database=housingprices;Trusted_Connection=yes;'

# Establish a connection
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

def register():
    name = name_entry.get()
    password = password_entry.get()

    # You can add your registration logic and validation here
    # For this basic example, it just prints the entered values
    cursor.execute("insert into users(username,password) values(?,?)",(name,password))
    messagebox.showinfo("Registration", "Registration successful!")
    cursor.commit()
# Create the main window
root = tk.Tk()
root.title("House Price Prediction - Login")

# Set the window size
root.geometry("500x350")

# Registration form
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")  # To hide the password

register_button = tk.Button(root, text="Register", command=register)

# Layout the widgets
name_label.pack()
name_entry.pack()

password_label.pack()
password_entry.pack()

register_button.pack()

# Start the application
root.mainloop()