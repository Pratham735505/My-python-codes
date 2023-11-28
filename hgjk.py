import tkinter as tk
from tkinter import messagebox
from ttkthemes import *
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from tkinter import ttk
email=''

connection = sqlite3.connect("Predictor.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER AUTO INCREMENT, name TEXT,email text,password text, contact INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS Score (email text,Runs float, wickets int,overs float) ")

cursor = connection.cursor()

# Create the main window
window = tk.Tk()
window.title("Login and Registration")
window.geometry('800x800')
main_frame = tk.Frame(window, bg='light blue', padx=50, pady=30)
def cui():
    model = LinearRegression()
    runs = float(input("Enter runs:"))
    wickets = int(input("Enter wickets:"))
    overs = float("Enter overs:")
    input_data = np.array([runs, wickets, overs]).reshape(1, -1)
    predicted_score = model.predict(input_data)
    print(f"Predicted score: {predicted_score[0]:.2f}")

def guii():
    def fetch_data():
        email = email_entry.get()

        # Fetch data from the database based on the email
        cursor.execute("SELECT runs, wickets, overs FROM users WHERE email=?", (email,))
        data = cursor.fetchone()

        if data:
            runs_entry.delete(0, tk.END)
            runs_entry.insert(0, data[0])
            wickets_entry.delete(0, tk.END)
            wickets_entry.insert(0, data[1])
            overs_entry.delete(0, tk.END)
            overs_entry.insert(0, data[2])
        else:
            result_label.config(text="No data found for this email.")

    # Create a function to predict the score
    def predict_score():
        runs = float(runs_entry.get())
        wickets = int(wickets_entry.get())
        overs = float(overs_entry.get())

        input_data = np.array([runs, wickets, overs]).reshape(1, -1)
        predicted_score = model.predict(input_data)

        result_label.config(text=f"Predicted score: {predicted_score[0]:.2f}")

    # Initialize the main application
    window = tk.Tk()
    window.title("Cricket Score Predictor")
    window.geometry('400x300')

    data = {
        'Runs': [200, 250, 280, 300, 320, 350, 370],
        'Wickets': [2, 3, 4, 2, 1, 3, 5],
        'Overs': [40, 45, 50, 35, 38, 42, 49]
    }

    df = pd.DataFrame(data)

    # Split the dataset into features and labels
    X = df[['Runs', 'Wickets', 'Overs']]
    y = df['Runs']

    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    # Create and place widgets in the main window
    frame = ttk.Frame(window)
    frame.grid(column=0, row=0, padx=10, pady=10)

    email_label = ttk.Label(frame, text="Email:")
    email_label.grid(row=0, column=0)
    email_entry = ttk.Entry(frame, width=30)
    email_entry.grid(row=0, column=1)

    fetch_button = ttk.Button(frame, text="Fetch Data", command=fetch_data)
    fetch_button.grid(row=1, column=0, columnspan=2)

    runs_label = ttk.Label(frame, text="Runs:")
    runs_label.grid(row=2, column=0)
    runs_entry = ttk.Entry(frame, width=30)
    runs_entry.grid(row=2, column=1)

    wickets_label = ttk.Label(frame, text="Wickets:")
    wickets_label.grid(row=3, column=0)
    wickets_entry = ttk.Entry(frame, width=30)
    wickets_entry.grid(row=3, column=1)

    overs_label = ttk.Label(frame, text="Overs:")
    overs_label.grid(row=4, column=0)
    overs_entry = ttk.Entry(frame, width=30)
    overs_entry.grid(row=4, column=1)

    predict_button = ttk.Button(frame, text="Predict Score", command=predict_score)
    predict_button.grid(row=5, column=0, columnspan=2)

    result_label = ttk.Label(frame, text="")
    result_label.grid(row=6, column=0, columnspan=2)

    window.mainloop()


def enter():
    e = tk.Tk()
    e.title('Entering')
    e.geometry('400x400')
    f = tk.Frame(e,bg='light blue', padx=50, pady=30)

    labelr=tk.Label(f,text="Runs")
    entry_r=tk.Entry(f,width=30)
    #entry_r.grid(row=0,column=1)
    entry_r.pack()
    #labelr.grid(row=0,column=0)
    labelr.pack()

    labelw=tk.Label(f,text="Wickets:")
    entry_w = tk.Entry(f, width=30)
    #entry_w.grid(row=0, column=1)
    entry_w.pack()
    #labelw.grid(row=1,column=0)
    labelw.pack()

    labelo=tk.Label(f,text="Overs:")
    entry_o = tk.Entry(f, width=30)
    #entry_o.grid(row=0, column=1)
    entry_o.pack()
    #labelo.grid(row=2,column=0)
    labelo.pack()
    def en():
        global email
        runs=entry_r.get()
        wickets=entry_w.get()
        overs=entry_o.get()
        q="Insert into score(email,runs,wickets,overs) values(?,?,?,?)"
        w=(email,runs,wickets,overs)
        cursor.execute(q,w)
        messagebox.showinfo('Successful','Values stored')
        reset_button1 = tk.Button(f, text="Store", command=guii)  # Set the button size
        reset_button1.grid(row=3, columnspan=1)
        reset_button1.pack()
    en()
    f.pack()
    e.mainloop()


def open_data_page():
    # Destroy the main login window
    window.destroy()

    # Create a new window for data operations
    data_window = tk.Tk()

    data_window.title("Data Page")
    data_window.geometry('800x600')

    def fetch():
        data_window1 = tk.Tk()
        data_window1.title("Fetch Page")
        data_window1.geometry('800x600')

        enter_data_button1 = tk.Button(data_window1, text="CUI FORM",command=cui)
        enter_data_button1.grid(row=0, column=0)
        enter_data_button1.pack()

        fetch_data_button1 = tk.Button(data_window1, text="GUI FORM",command=lambda: guii())
#       fetch_data_button.grid(row=1, column=0)
        fetch_data_button1.pack()
    # Add buttons for data operations

    enter_data_button = tk.Button(data_window, text="Enter Data", command=enter)
    enter_data_button.grid(row=0, column=0)
    enter_data_button.pack()

    fetch_data_button = tk.Button(data_window, text="Fetch Data", command=fetch)
#    fetch_data_button.grid(row=1,column=0)
    fetch_data_button.pack()
# Create a function to clear widgets on a frame


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Create a function to go back to the previous page


def go_back(frame):
    frame.pack_forget()
    main()
    main_frame.pack()

# Function to handle login button click


def login():
    global id_entry,password_entry,email
    lid = id_entry.get()

    password = password_entry.get()
    # You can add code here to process the login data
    if lid == '' or lid[len(lid) - 10:len(lid)] != '@gmail.com':
        messagebox.showwarning('Error', 'Invalid Email')
    elif len(password) < 8:
        messagebox.showwarning('Error', 'Invalid Password')
    else:
        query = "SELECT * FROM users WHERE email = ? or id=? AND password = ?"
        values = (lid, lid, password)
        email=lid
        cursor.execute(query, values)

        user = cursor.fetchone()
        # Fetch the user if found
        if user[2] == 'None':
            messagebox.showwarning('Error', 'Invalid id or email')
        elif user[3] == 'None' or user[3] == '':
            messagebox.showwarning('Error', 'Invalid password')
        else:
            if user:
                messagebox.showinfo("Login", f"Login Successful! Welcome {user[1]}")
                open_data_page()
            else:
                messagebox.showerror("Login Error", "Invalid Email or Password")


# Function to handle registration button click
def registration():
    #clear_widgets(main_frame)  # Clear widgets on the main frame
    main_frame.destroy()
    def register():
        email = id_entry1.get()
        password = password_entry1.get()
        repass = repass_entry.get()
        name = name_entry.get()
        contact = contact_entry.get()
        if email == '' or email[len(email)-10:len(email)] != '@gmail.com':
            messagebox.showwarning('Error', 'Invalid Email')
        elif len(contact) != 10 and contact.isdigit():
            messagebox.showerror('Error', 'Invalid Contact')
        elif len(password) < 8:
            messagebox.showwarning('Error', 'Password should be equal or greater than 8 characters')
        elif password != repass:
            messagebox.showerror('Error', 'Passwords do not match')
        else:
            # Insert the registration data into the database
            contact = int(contact)
            query = "INSERT INTO users (name,contact,email, password) VALUES (?, ?,?,?)"
            values = (name, contact, email, password)
            cursor.execute(query, values)
            connection.commit()  # Commit the transaction
            query = "select id from users where email=? and password=?"
            values = (email, password)
            cursor.execute(query, values)
            user = cursor.fetchone()
            messagebox.showinfo('Registration', f'Registration successful{name}! Your id is:{user[0]}')
            #clear_widgets(main_frame)
            open_data_page()

    registration_frame = tk.Frame(window,bg='light blue', padx=50, pady=30)
    registration_frame.pack(padx=110, pady=50)

    label_id1 = tk.Label(registration_frame, text="Email:")
    id_entry1 = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    id_entry1.grid(row=0, column=1)  # Use grid method to specify position

    label_name = tk.Label(registration_frame, text="Name:")
    name_entry = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    name_entry.grid(row=2, column=1)  # Use grid method to specify position

    label_contact = tk.Label(registration_frame, text="Contact:")
    contact_entry = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    contact_entry.grid(row=4, column=1)  # Use grid method to specify position

    label_password1 = tk.Label(registration_frame, text="Password:")
    password_entry1 = tk.Entry(registration_frame, show="*", width=30)  # Set the width and hide password
    password_entry1.grid(row=6, column=1)  # Use grid method to specify position

    label_repass = tk.Label(registration_frame, text="Confirm Password:")
    repass_entry = tk.Entry(registration_frame, show="*", width=30)  # Set the width and hide password
    repass_entry.grid(row=8, column=1)  # Use grid method to specify position

    email_button = tk.Button(registration_frame, text="Register", command=register)  # Set the button size
    email_button.grid(row=10, columnspan=2)  # Use grid method to specify position

    label_id1.grid(row=0, column=0)
    label_name.grid(row=2, column=0)
    label_contact.grid(row=4, column=0)
    label_password1.grid(row=6, column=0)
    label_repass.grid(row=8, column=0)

    back_button = tk.Button(registration_frame, text="Back", command=lambda: go_back(registration_frame))
    # Set the button size
    back_button.grid(row=12, columnspan=2)  # Use grid method to specify position

# Function to handle forgot password button click


def forgot_password():
    clear_widgets(main_frame)  # Clear widgets on the main frame

    def pass_reset():
        #       clear_widgets(main_frame)

        did = entry.get()
        mob = mob_entry.get()
        email = email_entry.get()

        def reset():
            clear_widgets(main_frame)
#            window.destroy()
            pass1 = pass1_entry.get()
            pass2 = pass2_entry.get()
            if len(pass1) < 8:
                messagebox.showwarning('Error', 'Password should be equal or greater than 8 characters')
            elif pass1 != pass2:
                messagebox.showerror('Error', 'Passwords do not match')
            else:
                # Add code here to save the registration data to a database or perform any other actions.

                messagebox.showinfo('', 'Password changed successfully successful')
                reset_frame.destroy()
                main()
                clear_widgets(main_frame)

        reset_frame = tk.Frame(window,bg='light blue', padx=50, pady=30)
        reset_frame.pack()
        label_pass1 = tk.Label(reset_frame, text="Password:")
        label_pass1.grid(row=0, column=0)

        pass1_entry = tk.Entry(reset_frame, width=30)  # Set the width of the entry widget
        pass1_entry.grid(row=0, column=1)

        label_pass2 = tk.Label(reset_frame, text="Retype Password:")
        label_pass2.grid(row=1, column=0)

        pass2_entry = tk.Entry(reset_frame, width=30)  # Set the width of the entry widget
        pass2_entry.grid(row=1, column=1)

        reset_button1 = tk.Button(reset_frame, text="Reset", command=reset)  # Set the button size
        reset_button1.grid(row=3, columnspan=2)

    forgot_password_frame = tk.Frame(window,bg='light blue', padx=50, pady=30)
    forgot_password_frame.pack()

    label_id1 = tk.Label(forgot_password_frame, text="ID:")
    label_id1.grid(row=0, column=0)

    entry = tk.Entry(forgot_password_frame, width=30)  # Set the width of the entry widget
    entry.grid(row=0, column=1)

    label_email = tk.Label(forgot_password_frame, text="Email:")
    label_email.grid(row=1, column=0)

    email_entry = tk.Entry(forgot_password_frame, width=30)  # Set the width of the entry widget
    email_entry.grid(row=1, column=1)

    label_no = tk.Label(forgot_password_frame, text="Mobile Number:")
    label_no.grid(row=2, column=0)

    mob_entry = tk.Entry(forgot_password_frame, width=30)  # Set the width of the entry widget
    mob_entry.grid(row=2, column=1)

    reset_button = tk.Button(forgot_password_frame, text="Proceed", command=pass_reset)  # Set the button size
    reset_button.grid(row=3, columnspan=2)

    back_button = tk.Button(forgot_password_frame, text="Back", command=lambda: go_back(forgot_password_frame))
    # Set the button size
    back_button.grid(row=4, columnspan=2)

# Create and place widgets in the main window
id_entry = tk.Entry(main_frame, width=30)  # Set the width of the entry widget
id_entry.grid(row=1, column=1, padx=10, pady=20)
password_entry = tk.Entry(main_frame, show="*", width=30)  # Set the width and hide password
password_entry.grid(row=2, column=1, padx=10, pady=20)
def main():
    global window
    global main_frame

    label = tk.Label(main_frame, text="Score Predictor")
    #label.grid(row=0, column=1, padx=10, pady=20)
    label.place(x=100, y=-10, width=100, height=25)

    label_id = tk.Label(main_frame, text="ID or Email:")
    label_id.grid(row=1, column=0, padx=10, pady=20)

    label_password = tk.Label(main_frame, text="Password")
    label_password.grid(row=2, column=0, padx=10, pady=20)

    login_button = tk.Button(main_frame, text="Login", command=login)  # Set the button size
    login_button.grid(row=3, columnspan=2)
    forgot_password_button = tk.Button(main_frame, text="Forgot Password:", command=forgot_password)  # Set the button size
    forgot_password_button.grid(row=5, columnspan=2)

    registration_button = tk.Button(main_frame, text="Register for New User",command=registration)  # Set the button size
    registration_button.grid(row=7, columnspan=2)

main()

main_frame.pack(padx=110, pady=50)

# Start the Tkinter main loop
window.mainloop()
