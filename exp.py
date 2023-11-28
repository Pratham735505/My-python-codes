import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import font

# Create a themed Tkinter window
root = ThemedTk(theme="equilux")
root.title("Login and Registration")
root.geometry('800x800')

font = font.nametofont("TkDefaultFont")
font.configure(family="Helvetica", size=12)

# Create a SQLite database connection
import sqlite3
connection = sqlite3.connect(database="Predictor.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEger auto increment, name TEXT, email text,password text,contact integer)")
#cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("John", 30))

# Function to clear widgets on a frame
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to animate a button's background color
def animate_login_button(widget, color1, color2, delay_ms=100):
    widget.configure(bg=color1)
    widget.update()
    widget.after(delay_ms, lambda: animate_login_button(widget, color2, color1, delay_ms))
def forgot_password():
    clear_widgets(main_frame)  # Clear widgets on the main frame

    def pass_reset():
        global window
        #clear_widgets(main_frame)
        id = entry.get()
        mob = mob_entry.get()
        email = email_entry.get()
        def reset():
            clear_widgets(main_frame)
            #window.destroy()
            pass1=pass1_entry.get()
            pass2=pass2_entry.get()
            if len(pass1)<8:
                messagebox.showwarning('Error', 'Password should be equal or greater than 8 characters')
            if pass1 != pass2:
                messagebox.showerror('Error', 'Passwords do not match')
            else:
                # Add code here to save the registration data to a database or perform any other actions.

                messagebox.showinfo('', 'Password changed successfully successful')
                clear_widgets(main_frame)

        reset_frame=tk.Frame(window)
        reset_frame.pack()
        label_pass1=tk.Label(reset_frame,text="Password:")
        label_pass1.grid(row=0,column=0)

        pass1_entry = tk.Entry(reset_frame, width=30)  # Set the width of the entry widget
        pass1_entry.grid(row=0, column=1)

        label_pass2 = tk.Label(reset_frame, text="Retype Password:")
        label_pass2.grid(row=1, column=0)

        pass2_entry = tk.Entry(reset_frame, width=30)  # Set the width of the entry widget
        pass2_entry.grid(row=1, column=1)

        reset_button = tk.Button(reset_frame, text="Reset", command=reset)  # Set the button size
        reset_button.grid(row=3, columnspan=2)

    forgot_password_frame = tk.Frame(window)
    forgot_password_frame.pack()

    label_id = tk.Label(forgot_password_frame, text="ID:")
    label_id.grid(row=0, column=0)

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

    back_button = tk.Button(forgot_password_frame, text="Back", command=lambda: go_back(forgot_password_frame))  # Set the button size
    back_button.grid(row=4, columnspan=2)
def registration():
    clear_widgets(main_frame)  # Clear widgets on the main frame

    def register():
        email = id_entry.get()
        password = password_entry.get()
        repass = repass_entry.get()
        name=name_entry.get()
        contact=contact_entry.get()
        if email=='' or email[len(email)-10:len(email)]!='@gmail.com':
            messagebox.showwarning('Error','Invalid Email')
        elif len(contact)!=10 and contact.isdigit():
            messagebox.showerror('Error','Invalid Contact')
        elif len(password)<8:
            messagebox.showwarning('Error','Password should be equal or greater than 8 characters')
        elif password != repass:
            messagebox.showerror('Error', 'Passwords do not match')
        else:
            # Insert the registration data into the database
            contact=int(contact)
            query = "INSERT INTO users (name,contact,email, password) VALUES (?, ?,?,?)"
            values = (name,contact,email, password)
            cursor.execute(query, values)
            connection.commit()  # Commit the transaction
            query="select id from users where email=? and password=?"
            values=(email,password)
            cursor.execute(query,values)
            user=cursor.fetchone()
            messagebox.showinfo('Registration', f'Registration successful{name}! Your id is:{user[0]}')


    registration_frame = tk.Frame(window)
    registration_frame.pack()

    label_id = tk.Label(registration_frame, text="Email:")
    id_entry = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    id_entry.grid(row=0, column=1)  # Use grid method to specify position

    label_name = tk.Label(registration_frame, text="Name:")
    name_entry = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    name_entry.grid(row=1, column=1)  # Use grid method to specify position

    label_contact = tk.Label(registration_frame, text="Contact:")
    contact_entry = tk.Entry(registration_frame, width=30)  # Set the width of the entry widget
    contact_entry.grid(row=2, column=1)  # Use grid method to specify position

    label_password = tk.Label(registration_frame, text="Password:")
    password_entry = tk.Entry(registration_frame, show="*", width=30)  # Set the width and hide password
    password_entry.grid(row=3, column=1)  # Use grid method to specify position

    label_repass = tk.Label(registration_frame, text="Confirm Password:")
    repass_entry = tk.Entry(registration_frame, show="*", width=30)  # Set the width and hide password
    repass_entry.grid(row=4, column=1)  # Use grid method to specify position

    email_button = tk.Button(registration_frame, text="Register", command=register)  # Set the button size
    email_button.grid(row=5, columnspan=2)  # Use grid method to specify position

    label_id.grid(row=0, column=0)
    label_name.grid(row=1,column=0)
    label_contact.grid(row=2,column=0)
    label_password.grid(row=3, column=0)
    label_repass.grid(row=4, column=0)

    back_button = tk.Button(registration_frame, text="Back", command=lambda: go_back(registration_frame))  # Set the button size
    back_button.grid(row=6, columnspan=2)  # Use grid method to specify position

def login():
    id = id_entry.get()
    password = password_entry.get()
    # You can add code here to process the login data
    if id == '' or id[len(id) - 10:len(id)] != '@gmail.com':
        messagebox.showwarning('Error', 'Invalid Email')
    elif len(password)<8:
        messagebox.showwarning('Error', 'Invalid Password')
    else:
        query = "SELECT * FROM users WHERE email = ? or id=? AND password = ?"
        values = (id, id, password)
        cursor.execute(query, values)

        user = cursor.fetchone()  # Fetch the user if found
        if user[2] == None:
            messagebox.showwarning('Error', 'Invalid id or email')
        elif user[3] == None or user[3] == '':
            messagebox.showwarning('Error', 'Invalid password')
        else:
            if user:
                messagebox.showinfo("Login", f"Login Successful! Welcome {user[1]}")
                open_data_page()
            else:
                messagebox.showerror("Login Error", "Invalid Email or Password")

# Create and place widgets in the main window
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack()

label_id = tk.Label(main_frame, text="ID or Email:")
label_id.grid(row=0, column=0)

label_password = tk.Label(main_frame, text="Password")
label_password.grid(row=1, column=0)

id_entry = tk.Entry(main_frame, width=30)
id_entry.grid(row=0, column=1)

password_entry = tk.Entry(main_frame, show="*", width=30)
password_entry.grid(row=1, column=1)

login_button = tk.Button(main_frame, text="Login", command=login)
login_button.grid(row=3, columnspan=2)
animate_login_button(login_button, "green", "blue")

forgot_password_button = tk.Button(main_frame, text="Forgot Password", command=forgot_password)
forgot_password_button.grid(row=5, columnspan=2)

registration_button = tk.Button(main_frame, text="Register for New User", command=registration)
registration_button.grid(row=7, columnspan=2)

# Function to open the data page
def open_data_page():
    root.withdraw()  # Hide the main login window
    data_window = ThemedTk(theme="plastik")
    data_window.title("Data Page")
    data_window.geometry('800x600')

    def fetch():
        data_window = ThemedTk(theme="blue")
        data_window.title("Fetch Page")
        data_window.geometry('800x600')

        def enter_data():
            # Add your code for entering data here
            pass

        def fetch_data():
            # Add your code for fetching data here
            pass

        enter_data_button = tk.Button(data_window, text="Enter Data", command=enter)
        enter_data_button.grid(row=0, column=0)

        fetch_data_button = tk.Button(data_window, text="Fetch Data", command=fetch_data)
        fetch_data_button.grid(row=1, column=0)

    data_window.protocol("WM_DELETE_WINDOW", root.destroy)  # Close the app when this window is closed
    fetch_button = tk.Button(data_window, text="Fetch Data", command=fetch)
    fetch_button.grid(row=0, column=0)

# Function to handle login button click
def login():
    email = id_entry.get()
    password = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login", f"Login Successful! Welcome {user[1]}")
        open_data_page()
    else:
        messagebox.showerror("Login Error", "Invalid Email or Password")

# Function to handle registration button click
def registration():
    clear_widgets(main_frame)

    def register():
        email = id_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        contact = contact_entry.get()
        if email == '' or email[-10:] != '@gmail.com':
            messagebox.showwarning('Error', 'Invalid Email')
        elif len(contact) != 10 or not contact.isdigit():
            messagebox.showerror('Error', 'Invalid Contact')
        elif len(password) < 8:
            messagebox.showwarning('Error', 'Password should be at least 8 characters')
        elif password != repass_entry.get():
            messagebox.showerror('Error', 'Passwords do not match')
        else:
            contact = int(contact)
            cursor.execute("INSERT INTO users (name, contact, email, password) VALUES (?, ?, ?, ?)",
                           (name, contact, email, password))
            connection.commit()
            cursor.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
            user = cursor.fetchone()
            messagebox.showinfo('Registration', f'Registration successful {name}! Your ID is: {user[0]}')

    registration_frame = tk.Frame(root, bg="lightblue")
    registration_frame.pack()

    labels = ["Email:", "Name:", "Contact:", "Password:", "Confirm Password:"]
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(registration_frame, text=label_text)
        label.grid(row=i, column=0)
        entry = tk.Entry(registration_frame, width=30)
        entry.grid(row=i, column=1)
        entries.append(entry)

    email_button = tk.Button(registration_frame, text="Register", command=register)
    email_button.grid(row=len(labels), columnspan=2)

    back_button = tk.Button(registration_frame, text="Back", command=lambda: clear_widgets(registration_frame))
    back_button.grid(row=len(labels) + 1, columnspan=2)

# Function to handle forgot password button click
def forgot_password():
    clear_widgets(main_frame)

    def pass_reset():
        id = entry.get()
        mob = mob_entry.get()
        email = email_entry.get()
        def reset():
            pass1 = pass1_entry.get()
            pass2 = pass2_entry.get()
            if len(pass1) < 8:
                messagebox.showwarning('Error', 'Password should be at least 8 characters')
            if pass1 != pass2:
                messagebox.showerror('Error', 'Passwords do not match')
            else:
                # Add code here to save the registration data to a database or perform any other actions.
                messagebox.showinfo('', 'Password changed successfully')

        reset_frame = tk.Frame(root, bg="lightblue")
        reset_frame.pack()
        labels = ["Password:", "Retype Password:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(reset_frame, text=label_text)
            label.grid(row=i, column=0)
            entry = tk.Entry(reset_frame, width=30)
            entry.grid(row=i, column=1)
            entries.append(entry)

        reset_button = tk.Button(reset_frame, text="Reset", command=reset)
        reset_button.grid(row=len(labels), columnspan=2)

    forgot_password_frame = tk.Frame(root, bg="lightblue")
    forgot_password_frame.pack()
    labels = ["ID:", "Email:", "Mobile Number:"]
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(forgot_password_frame, text=label_text)
        label.grid(row=i, column=0)
        entry = tk.Entry(forgot_password_frame, width=30)
        entry.grid(row=i, column=1)
        entries.append(entry)

    reset_button = tk.Button(forgot_password_frame, text="Proceed", command=pass_reset)
    reset_button.grid(row=len(labels), columnspan=2)

    back_button = tk.Button(forgot_password_frame, text="Back", command=lambda: clear_widgets(forgot_password_frame))
    back_button.grid(row=len(labels) + 1, columnspan=2)

# Create and place widgets in the main window
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack()

label_id = tk.Label(main_frame, text="ID or Email:")
label_id.grid(row=0, column=0)

label_password = tk.Label(main_frame, text="Password")
label_password.grid(row=1, column=0)

id_entry = tk.Entry(main_frame, width=30)
id_entry.grid(row=0, column=1)

password_entry = tk.Entry(main_frame, show="*", width=30)
password_entry.grid(row=1, column=1)

login_button = tk.Button(main_frame, text="Login", command=login)
login_button.grid(row=3, columnspan=2)
animate_login_button(login_button, "green", "blue")

forgot_password_button = tk.Button(main_frame, text="Forgot Password", command=forgot_password)
forgot_password_button.grid(row=5, columnspan=2)

registration_button = tk.Button(main_frame, text="Register for New User", command=registration)
registration_button.grid(row=7, columnspan=2)

if __name__ == "__main__":
    root.mainloop()
