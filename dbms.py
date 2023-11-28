# Importing modules
import customtkinter as tk
import sqlite3
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
from sklearn.linear_model import LinearRegression

# Creating database connection
conn = sqlite3.connect("predictor.db")
cur = conn.cursor()
eml = ''
# Creating table for storing login credentials
cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, contact int, password TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Score (email text,Runs text, wickets int,overs float) ")
cur.execute("CREATE TABLE IF NOT EXISTS admin (name TEXT, email TEXT, password TEXT)")
cur.execute("Insert into admin values('Pratham','gg@gmail.com','7355057737')")
# Creating main window
root = tk.CTk()
root.title("Login Page")
root.geometry("1280x1024")
root.configure(bg='light blue')
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

# Creating variables for storing user input
name_var = tk.StringVar()
email_var = tk.StringVar()
contact_var = tk.StringVar()
password_var = tk.StringVar()

# Creating labels and entries for login page
name_label = tk.CTkLabel(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.CTkEntry(root, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = tk.CTkLabel(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.CTkEntry(root, textvariable=email_var)
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.CTkLabel(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.CTkEntry(root, textvariable=password_var, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

cur = conn.cursor()

# Getting the data from the score table as a pandas dataframe
df = pd.read_sql_query("SELECT overs,wickets,runs FROM score", conn)

# Splitting the data into features and target
X = df[["overs", "wickets"]]  # Features are overs and wickets
y = df["Runs"]  # Target is runs

# Creating a linear regression model
model = LinearRegression()

# Fitting the model to the data
model.fit(X, y)

# Predicting the score for a given overs and wickets


def predict_score(overs, wickets):
    # Creating a 2D array with the input values
    dinput = [[overs, wickets]]

    # Predicting the score using the model
    score = model.predict(dinput)

    # Returning the predicted score as an integer
    return int(score[0])


e_entry=tk.StringVar()
pass_entry=tk.StringVar()
def admin_login():
    global pass_entry, e_entry
    global root, e
    wi = tk.CTkFrame(root)
    #wi.geometry('1280x1024')
    #wi.title('Admin Login')
    wi.configure(bg='light blue')

    my_image = tk.CTkImage(light_image=Image.open("imagewithtext.jpg"), dark_image=Image.open("imagewithtext.jpg"),
                           size=(300, 300))
    i = tk.CTkLabel(wi, image=my_image)
    i.grid(row=0, column=8)

    e_entry = tk.CTkEntry(wi, textvariable=email_var,placeholder_text="Email")
    e_entry.grid(row=4, column=8, padx=10, pady=10,)


    pass_entry = tk.CTkEntry(wi, textvariable=password_var, show="*",placeholder_text="Password")
    pass_entry.grid(row=5, column=8, padx=10, pady=10)
    # Creating button for login page
    login_button = tk.CTkButton(wi, text="Login", command=adlogin)
    login_button.grid(row=7, columnspan=10)
    wi.mainloop()


def adlogin():
    global e_entry,pass_entry
    e=e_entry.get()
    p=pass_entry.get()
    cur.execute("select * from admin")
    r=cur.fetchone()
    if r[1]==e and p==r[2]:
        def add_information():
            global eml
            # Opening a new window for adding information
            add_info_window = tk.CTkToplevel(root)
            add_info_window.configure(bg='light blue')
            add_info_window.title("Add Information")
            add_info_window.geometry('1280x1024')

            # Creating labels and entries for adding information
            score_label = tk.CTkLabel(add_info_window, text="Enter your score:")
            score_label.pack()
            score_entry = tk.CTkEntry(add_info_window)
            score_entry.pack()

            over_label = tk.CTkLabel(add_info_window, text="Enter the number of overs:")
            over_label.pack()
            over_entry = tk.CTkEntry(add_info_window)
            over_entry.pack()

            wicket_label = tk.CTkLabel(add_info_window, text="Enter the number of wickets:")
            wicket_label.pack()
            wicket_entry = tk.CTkEntry(add_info_window)
            wicket_entry.pack()
        add_information()
    else:
        tk.CTkLabel(root,text="Invalid admin_id")

# Creating function for dashboard page
def dashboard(name):
    # Creating a new window
    dashboard_window = tk.CTk()
    dashboard_window.configure(bg='light blue')
    dashboard_window.title("User Dashboard")
    dashboard_window.geometry('1280x1024')

    # Creating a welcome label with username
    welcome_label = tk.CTkLabel(dashboard_window, text=f"Welcome, {name}!", font=("Arial", 20))
    welcome_label.pack()

    # Creating a menu bar with logout and add information options
    menu_bar = tk.CTkOptionMenu(dashboard_window)
    dashboard_window.configure(menu=menu_bar)

    # Creating a logout command
    def logout():
        # Closing the current window
        dashboard_window.destroy()

        # Reopening the login page
        login_page()

    # Creating an add information command
    def add_information():
        global eml
        # Opening a new window for adding information
        add_info_window = tk.CTkToplevel(dashboard_window)
        add_info_window.configure(bg='light blue')
        add_info_window.title("Add Information")
        add_info_window.geometry('1280x1024')

        # Creating labels and entries for adding information
        score_label = tk.CTkLabel(add_info_window, text="Enter your score:")
        score_label.pack()
        score_entry = tk.CTkEntry(add_info_window)
        score_entry.pack()

        over_label = tk.CTkLabel(add_info_window, text="Enter the number of overs:")
        over_label.pack()
        over_entry = tk.CTkEntry(add_info_window)
        over_entry.pack()

        wicket_label = tk.CTkLabel(add_info_window, text="Enter the number of wickets:")
        wicket_label.pack()
        wicket_entry = tk.CTkEntry(add_info_window)
        wicket_entry.pack()

        # Creating a save button for adding information
        def save():
            # Getting the information from the entries
            score = score_entry.get()
            over = over_entry.get()
            wicket = wicket_entry.get()

            # Checking if the inputs are valid
            try:
                # Converting the inputs to integers
                score = int(score)
                over = float(over)
                wicket = int(wicket)

                # Applying constraints on overs and wickets
                if over < 0 or over > 50:
                    raise ValueError("Invalid number of overs. It should be between 0 and 50.")
                if wicket < 0 or wicket > 10:
                    raise ValueError("Invalid number of wickets. It should be between 0 and 10.")

                # Saving the information in the database table named score
                cur.execute("INSERT INTO Score(runs,Overs,wickets,email) VALUES (?,?,?,?)", (score, over, wicket, eml))
                conn.commit()

                # Showing a success message
                success_label = tk.CTkLabel(add_info_window, text="Information saved successfully.")
                success_label.pack()

                # Closing the current window after 3 seconds
                add_info_window.after(3000, lambda: add_info_window.destroy())

            except ValueError as e:
                # Showing an error message if the inputs are invalid
                error_label = tk.CTkLabel(add_info_window, text=str(e), fg="red")
                error_label.pack()

        save_button = tk.CTkButton(add_info_window, text="Save", command=save)
        save_button.pack()

    # Adding the options to the menu bar
    # Creating a frame for buttons
    button_frame = tk.CTkFrame(dashboard_window)
    button_frame.pack()

    # Creating a fetch data button
    def fetch_data():
        # Opening a new window for fetching data
        fetch_data_window = tk.CTkToplevel(dashboard_window)
        fetch_data_window.configure(bg='light blue')
        fetch_data_window.title("Fetch Data")
        fetch_data_window.geometry('1280x1024')

        # Creating labels and entries for fetching data
        data_label = tk.CTkLabel(fetch_data_window, text="Enter over:")
        data_label.pack()
        data_entry = tk.CTkEntry(fetch_data_window)
        data_entry.pack()

        # Creating a fetch button for fetching data
        def fetch():
            global eml
            # Getting the data from the entry
            data = data_entry.get()
            cur.execute('select overs,runs,wickets from score where overs=? and email=?', (data, eml))
            # Fetching the data from some source (dummy code)
            fetched_data = cur.fetchone()
            lo = tk.CTkLabel(fetch_data_window, text=f"Over :{fetched_data[0]}")
            lo.pack()
            lr = tk.CTkLabel(fetch_data_window, text=f"Runs scored :{fetched_data[1]}")
            lr.pack()
            lw = tk.CTkLabel(fetch_data_window, text=f"Wickets lost :{fetched_data[2]}")
            lw.pack()

            # Showing a success message
            success_label = tk.CTkLabel(fetch_data_window, text="Data fetched successfully.", fg="green")
            success_label.pack()

            # Closing the current window after 3 seconds
            fetch_data_window.after(3000, lambda: fetch_data_window.destroy())

            # Returning the fetched data
            return fetched_data

        fetch_button = tk.CTkButton(fetch_data_window, text="Fetch", command=fetch)
        fetch_button.pack()

    fetch_data_button = tk.CTkButton(button_frame, text="Fetch Data", command=fetch_data)
    fetch_data_button.grid(row=0, column=0)


    def plot_score():
        global eml
        # Predicting the score using the function
        cur.execute('Select overs,wickets from score where email=?', (eml,))
        g = cur.fetchone()
        overs = g[0]
        wickets = g[1]
        score = predict_score(overs, wickets)

        # Creating a figure and an axis object
        fig, ax = plt.subplots()

        # Plotting the actual runs as a line chart
        ax.plot(df["overs"], df["Runs"], label="Actual")

        # Plotting the predicted score as a red dot on the chart
        ax.scatter(overs, score, color="red", label="Predicted")

        # Setting the labels for the axes and the title
        ax.set_xlabel("Overs")
        ax.set_ylabel("Runs")
        ax.set_title(f"Predicted score for {overs} overs and {wickets} wickets")

        # Adding a legend to the chart
        ax.legend()

        # Showing the chart
        plt.show()

    display_data_button = tk.CTkButton(button_frame, text="Predict Score", command=plot_score)
    display_data_button.grid(row=0, column=1)
    log = tk.CTkButton(button_frame, text="Logout", command=logout)
    add = tk.CTkButton(button_frame, text="Add Information", command=add_information)
    add.grid()
    log.grid()

    # Running the main loop
    dashboard_window.mainloop()

# Creating function for logout button


def logout(window):
    # Closing the current window
    window.destroy()

    # Reopening the login page
    login_page()

# Creating function for forgot password button


def forgot_password():
    global name_label, name_entry, email_label, email_entry
    # Clearing the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Creating labels and entries for forgot password page
    name_label = tk.CTkLabel(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.CTkEntry(root, textvariable=name_var)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = tk.CTkLabel(root, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=10)
    email_entry = tk.CTkEntry(root, textvariable=email_var)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    # Insert the registration data into the database
    contact_label = tk.CTkLabel(root, text="Contact:")
    contact_label.grid(row=2, column=0, padx=10, pady=10)
    contact_entry = tk.CTkEntry(root, textvariable=contact_var)
    contact_entry.grid(row=2, column=1, padx=10, pady=10)

    # Creating function for reset password button
    def reset_password():
        nonlocal widget
        # Getting user input
        name = name_var.get()
        email = email_var.get()
        contact = contact_var.get()

        # Checking if user exists in database
        cur.execute("SELECT * FROM users WHERE name=? AND email=? AND contact=?", (name, email, contact))
        result = cur.fetchone()

        # If user exists, open a new window for changing password
        if result:
            # Clearing the main window
            for widget in root.winfo_children():
                widget.forget()

            # Creating a new window
            new_window = tk.CTkToplevel(root)
            new_window.title("Reset Password")
            new_window.geometry('1280x1024')

            # Creating variables for storing new password
            new_password_var = tk.StringVar()
            confirm_password_var = tk.StringVar()

            # Creating labels and entries for reset password page
            new_password_label = tk.CTkLabel(new_window, text="New Password:")
            new_password_label.grid(row=0, column=0, padx=10, pady=10)
            new_password_entry = tk.CTkEntry(new_window, textvariable=new_password_var, show="*")
            new_password_entry.grid(row=0, column=1, padx=10, pady=10)

            confirm_password_label = tk.CTkLabel(new_window, text="Confirm Password:")
            confirm_password_label.grid(row=1, column=0, padx=10, pady=10)
            confirm_password_entry = tk.CTkEntry(new_window, textvariable=confirm_password_var, show="*")
            confirm_password_entry.grid(row=1, column=1, padx=10, pady=10)

            # Creating function for save password button
            def save_password():
                # Getting new password
                nonlocal error_label
                new_password = new_password_var.get()
                confirm_password = confirm_password_var.get()

                # Checking if passwords match
                if new_password == confirm_password and len(new_password)>=8:
                    # Updating the password in database
                    cur.execute("UPDATE users SET password=? WHERE name=? AND email=? AND contact=?", (new_password, name, email, contact))
                    conn.commit()

                    # Showing a success message
                    success_label = tk.CTkLabel(new_window, text="Password changed successfully.", fg="green")
                    success_label.grid(row=3, columnspan=2)

                    # Closing the current window after 3 seconds
                    new_window.after(3000, lambda: new_window.destroy())

                    # Reopening the login page after 3 seconds
                    root.after(3000, login_page)

                # If passwords do not match, show an error message
                else:
                    error_label = tk.CTkLabel(new_window, text="Passwords do not match. Please try again.", fg="red")
                    error_label.grid(row=3, columnspan=2)

            # Creating button for save password page
            save_password_button = tk.CTkButton(new_window, text="Save Password", command=save_password)
            save_password_button.grid(row=2, columnspan=2)

        # If user does not exist, show an error message
        else:
            error_label = tk.CTkLabel(root, text="Invalid name, email or contact. Please try again.", fg="red")
            error_label.grid(row=4, columnspan=2)

    # Creating button for reset password page
    reset_password_button = tk.CTkButton(root, text="Reset Password", command=reset_password)
    reset_password_button.grid(row=3, columnspan=2)
# Creating function for registration button


def registration():
    global name_label, name_entry, email_label, email_entry, email_var, password_label, password_entry
    # Clearing the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Creating labels and entries for registration page
    name_label = tk.CTkLabel(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.CTkEntry(root, textvariable=name_var)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = tk.CTkLabel(root, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=10)
    email_entry = tk.CTkEntry(root, textvariable=email_var)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    contact_label = tk.CTkLabel(root, text="Contact:")
    contact_label.grid(row=2, column=0, padx=10, pady=10)
    contact_entry = tk.CTkEntry(root, textvariable=contact_var)
    contact_entry.grid(row=2, column=1, padx=10, pady=10)

    password_label = tk.CTkLabel(root, text="Password:")
    password_label.grid(row=3, column=0, padx=10, pady=10)
    password_entry = tk.CTkEntry(root, textvariable=password_var, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=10)

    # Creating function for register button
    def register():
        # Getting user input
        name = name_var.get()
        email = email_var.get()
        contact = contact_var.get()
        password = password_var.get()
        if email == '' or email[len(email)-10:len(email)] != '@gmail.com':
            tk.CTkLabel(root, text='Invalid Email',fg_color="red").grid(row=10,column=1)
            root.configure()
        elif len(contact) != 10 and contact.isdigit():
            tk.CTkLabel(root, text='Invalid Contact',fg_color="red").grid(row=10,column=1)
        elif len(password) < 8:
            tk.CTkLabel(root, text='Password should be equal or greater than 8 characters',fg_color="red").grid(row=10, column=1)
        else:
            contact = int(contact)
            query = "INSERT INTO users (name,contact,email, password) VALUES (?, ?,?,?)"
            values = (name, contact, email, password)
            cur.execute(query, values)
            conn.commit()  # Commit the transaction
            tk.CTkLabel(root, text=f'Registration successful{name}!')
            # Checking if user already exists in database
            cur.execute("SELECT * FROM users WHERE name=? AND email=? AND contact=?", (name, email, contact))
            result = cur.fetchone()

            # If user does not exist, insert the user details in database
            if not result:
                '''cur.execute("INSERT INTO users(name,email,contact,password) VALUES (?,?,?,?)",
                            (name, email, contact, password))
                conn.commit()
'''
                # Showing a success message
                success_label = tk.CTkLabel(root, text="Registration successful.", fg_color="green")
                success_label.grid(row=5, columnspan=2)

                # Closing the main window after 3 seconds
                root.after(30000, lambda: root.configure())

                # Reopening the login page after 3 seconds
                login_page()

            # If user already exists, show an error message
            else:
                error_label = tk.CTkLabel(root,
                                          text="User already exists. Please try a different name, email or contact.",
                                          fg_color="red")
                error_label.grid(row=5, columnspan=2)

    # Creating button for register page
    register_button = tk.CTkButton(root, text="Register", command=register)
    register_button.grid(row=4, columnspan=2)

# Creating function for login page


def login_page():
    # Clearing the main window
    global  email_entry, password_entry
    for widget in root.winfo_children():
        widget.destroy()

    # Creating labels and entries for login page
    my_image = tk.CTkImage(light_image=Image.open("imagewithtext.jpg"), dark_image=Image.open("imagewithtext.jpg") ,size= (300,300))
    i = tk.CTkLabel(root, image= my_image)
    i.grid(row=0, column=8)

    label = tk.CTkLabel(master=root, width=120, height=32, text="Login System")
    label.grid(row=7,column=8,pady=12, padx=10)

    email_entry = tk.CTkEntry(master=root, width=240, height=32, placeholder_text="Username")
    email_entry.grid(row=8,column=8,pady=12, padx=10)

    password_entry = tk.CTkEntry(master=root, width=240, height=32, placeholder_text="Password", show="*")
    password_entry.grid(row=9,column=8,pady=12, padx=10)

    button = tk.CTkButton(master=root, width=240, height=32, text="Login", command=login)
    button.grid(row=10,column=8,pady=12, padx=10)

    checkbox = tk.CTkCheckBox(master=root, text="Remember me")
    checkbox.grid(row=11,column=8,pady=12, padx=10)

    # Creating button for registration page
    registration_button = tk.CTkButton(root, width=240, height=32, text="Register", command=registration)
    registration_button.grid(row=12, columnspan=10)

    # Creating button for reset password page
    reset_password_button = tk.CTkButton(root, width=240, height=32, text="Forgot Password?", command=forgot_password)
    reset_password_button.grid(row=14, columnspan=10)

    admin = tk.CTkButton(root, text="Are you an admin?Login", width=240, height=32, command=admin_login)
    admin.grid(row=16, columnspan=10)


# Creating function for login button
def login():
    global eml

    # Getting user input
    email = email_entry.get()
    password = password_entry.get()

    # Checking if user exists in database
    cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = cur.fetchone()
    # If user exists, open a new window for data entry or visualization
    if result:
        # Clearing the main window
        eml = email
        for widget in root.winfo_children():
            widget.forget()
        # Creating labels and buttons for data page
        cur.execute('select * from users where email=? and password=?', (eml,password))
        name = cur.fetchone()
        dashboard(name[0])

    # If user does not exist, show an error message
    else:
        error_label = tk.CTkLabel(root, text="Invalid name, email or password. Please try again.",)
        error_label.grid(row=8, columnspan=10)

# Calling the login page function


login_page()

# Running the main loop
root.mainloop()