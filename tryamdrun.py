import tkinter as tk
from tkinter import messagebox
import mysql.connector as sqltor
from ddddd import machinelearning
'''
mycon = sqltor.connect(host='localhost', user='root', password='1234', database='stock_prediction')
cursor = mycon.cursor()
cursor.execute('USE stock_prediction;')
# cursor.execute('drop database examples;')
'''
font = ("Algerian", 18)


def login():
    root = tk.Tk()
    root.geometry("700x300")
    root.title("Login into user account")

    def login_data():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:
            cursor.execute("SELECT username FROM user_Data WHERE Username=%s;", (username,))
            existing_username = cursor.fetchone()
            if existing_username:
                cursor.execute("SELECT Password FROM user_data WHERE Username=%s;", (username,))
                existing_password = cursor.fetchone()
                if existing_password[0] == password:
                    data()
                else:
                    messagebox.showwarning("Error!", "Invalid username or password!")
            else:
                msg = tk.Label(root, text="Username does not exist, Enter a Valid Username.", font=font)
                msg.grid(column=3)
        else:
            messagebox.showwarning("Warning!", "Details cannot be Blank, Fill all the required details.")

    username_label = tk.Label(root, text="Username: ", font=font)
    username_label.grid(padx=100, pady=5, sticky=tk.W)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, padx=20, pady=10)

    password_label = tk.Label(root, text="Password: ", font=font)
    password_label.grid(padx=100, pady=5, sticky=tk.W)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=20, pady=10)

    forgot_password_button = tk.Button(root, text="Forgot Password", font=font, command=forgot_password)
    forgot_password_button.grid(row=2, column=0, columnspan=2, padx=0, pady=20)

    login_button = tk.Button(root, text="Login", font=font, command=login_data)
    login_button.grid(row=2, column=1, columnspan=2, padx=0, pady=0)

    # open()
    root.mainloop()


def register():
    global root
    root = tk.Tk()
    root.geometry("1000x500")
    root.title("Registeration for New User")
    gender_option = tk.StringVar()
    gender_option.set(" ")

    def insert_data():
        global username
        name = name_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        gender = gender_option.get()
        username = create_username_entry.get()
        password = create_password_entry.get()
        if name and mobile and email and gender and username and password:
            cursor.execute("SELECT Username FROM user_Data WHERE Username=%s;", (username,))
            existing_username = cursor.fetchone()
            if existing_username:
                u_label = tk.Label(root, text="Username already exist,Create unique username", font=font)
                u_label.grid(row=3, column=3, pady=20, padx=10)
            else:
                cursor.execute('INSERT INTO user_Data values(%s, %s, %s, %s, %s, %s);',
                               (name, mobile, email, gender, username, password))
                login()
                mycon.commit()
        else:
            messagebox.showwarning("Warning!", "Details cannot be Blank, Fill all the required details.")

    name_label = tk.Label(root, text="Name: ", font=font)
    name_label.grid(padx=100, pady=5, sticky=tk.W)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    mobile_label = tk.Label(root, text="Mobile: ", font=font)
    mobile_label.grid(padx=100, pady=5, sticky=tk.W)
    mobile_entry = tk.Entry(root)
    mobile_entry.grid(row=1, column=1, padx=20, pady=10)

    email_label = tk.Label(root, text="Email: ", font=font)
    email_label.grid(padx=100, pady=5, sticky=tk.W)
    email_entry = tk.Entry(root)
    email_entry.grid(row=2, column=1, padx=20, pady=5)

    gender_label = tk.Label(root, text="Gender: ", font=font)
    gender_label.grid(padx=100, pady=5, sticky=tk.W)

    radio_button1 = tk.Radiobutton(root, text="Male", variable=gender_option, value="Male", font=font)
    radio_button1.grid(row=3, column=1)
    radio_button2 = tk.Radiobutton(root, text="Female", variable=gender_option, value="Female", font=font)
    radio_button2.grid(row=3, column=2)
    radio_button3 = tk.Radiobutton(root, text="Others", variable=gender_option, value="Other", font=font)
    radio_button3.grid(row=3, column=3)

    create_username_label = tk.Label(root, text="Create Username: ", font=font)
    create_username_label.grid(padx=100, pady=5, sticky=tk.W)
    create_username_entry = tk.Entry(root)
    create_username_entry.grid(row=4, column=1, padx=20, pady=10)

    info_label = tk.Label(root, text="*Create a Unique Username*")
    info_label.grid(row=5)

    create_password_label = tk.Label(root, text="Create Password: ", font=font)
    create_password_label.grid(padx=100, pady=5, sticky=tk.W)
    create_password_entry = tk.Entry(root)
    create_password_entry.grid(row=6, column=1, padx=20, pady=10)

    imp_label = tk.Label(root, text="*Create a Strong Password of minimun 8 Characters*")
    imp_label.grid(row=7)

    register_button = tk.Button(root, text="Register", font=font, command=insert_data)
    register_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    if_label = tk.Label(root, text="If already register then login from here", font=font)
    if_label.grid(row=9)

    if_login_button = tk.Button(root, text="Login", font=font, command=login)
    if_login_button.grid(row=10, column=0, columnspan=2, padx=0, pady=10)

    root.mainloop()


def forgot_password():
    global root
    root = tk.Tk()
    root.geometry("700x300")
    root.title("User verification")

    def forgot_data():
        global username
        username = username_forgot_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        if username and mobile and email:
            cursor.execute("SELECT Username from User_Data where Username=%s;", (username,))
            existing_username = cursor.fetchone()
            if existing_username:
                cursor.execute("SELECT Mobile from User_Data where Username=%s;", (username,))
                existing_mobile = cursor.fetchone()
                if existing_mobile[0] == mobile:
                    cursor.execute("SELECT Email from User_Data where Username=%s and Mobile=%s;", (username, mobile))
                    existing_email = cursor.fetchone()
                    if existing_email[0] == email:
                        mycon.commit()
                        change()
                    else:
                        messagebox.showwarning("Warning!", "Invalid Email. Enter Valid Email!")
                else:
                    messagebox.showwarning("Warning!", "Invalid Mobile Number. Enter Valid Mobile Number!")
            else:
                messagebox.showwarning("Warning!", "Username does not exist, Enter a Valid Username.")
        else:
            messagebox.showwarning("Warning!", "Details cannot be Blank, Fill all the required details.")

    username_forgot_label = tk.Label(root, text="Username: ", font=font)
    username_forgot_label.grid(sticky=tk.S)
    username_forgot_entry = tk.Entry(root)
    username_forgot_entry.grid(row=0, column=1, padx=10, pady=5)

    mobile_label = tk.Label(root, text="Mobile No. ", font=font)
    mobile_label.grid(row=1, sticky=tk.S)
    mobile_entry = tk.Entry(root)
    mobile_entry.grid(row=1, column=1, padx=20, pady=10)

    email_label = tk.Label(root, text="Email ", font=font)
    email_label.grid(row=2, sticky=tk.S)
    email_entry = tk.Entry(root)
    email_entry.grid(row=2, column=1, padx=20, pady=10)

    verify_button = tk.Button(root, text="Verify", font=font, command=forgot_data)
    verify_button.grid(row=3, column=0, columnspan=2, padx=0, pady=10)

    root.mainloop()


def change():
    root = tk.Tk()
    root.geometry("600x300")
    root.title("Change the Password")

    def change_password():
        # username=username_change_entry.get()
        new = new_entry.get()
        confirm = confirm_entry.get()
        if new and confirm:
            cursor.execute("SELECT username FROM User_Data WHERE Username=%s;", (username,))
            existing_username = cursor.fetchone()
            if existing_username:
                if new == confirm:
                    cursor.execute("UPDATE User_Data SET Password=%s WHERE Username = %s;", (confirm, username))
                    mycon.commit()
                    message()
                else:
                    messagebox.showwarning("Error!", "Passwords do not match")
            else:
                messagebox.showwarning("Warning!", "Username does not exist, Enter a Valid Username.")
        else:
            messagebox.showwarning("Invalid details. Enter correct verification details!")

    """username_change_label=tk.Label(forgot_password,text="Username: ",font=font)
    username_change_label.grid(sticky=tk.W)
    username_change_entry=tk.Entry(forgot_password)
    username_change_entry.grid(row=0, column=1,padx=10,pady=5)"""

    new_label = tk.Label(root, text="New Password: ", font=font)
    new_label.grid(sticky=tk.W)
    new_entry = tk.Entry(root)
    new_entry.grid(row=0, column=1, padx=20, pady=10)

    confirm_label = tk.Label(root, text="Confirm Password:  ", font=font)
    confirm_label.grid(row=1, sticky=tk.W)
    confirm_entry = tk.Entry(root)
    confirm_entry.grid(row=1, column=1, padx=20, pady=10)

    change_button = tk.Button(root, text="change", font=font, command=change_password)
    change_button.grid(row=2, column=0, columnspan=2, padx=0, pady=10)

    root.mainloop()


def message():
    messagebox.showinfo("Information!",
                        "Your Password has been changed succesfully! Kindly, Login to get access to your account to proceed further.")
    login()


def data():
    global root
    root = tk.Tk()
    root.geometry("700x300")
    root.title("Data Manipulation")

    def add_data():
        st_id = st_id_entry.get()
        opens = opens_entry.get()
        high = high_entry.get()
        low = low_entry.get()
        close = close_entry.get()
        year = year_entry.get()
        if st_id and opens and high and low and close and year:
            cursor.execute("SELECT ST_ID FROM stock_data WHERE ST_ID=%s;", (st_id,))
            existing_ID = cursor.fetchone()
            if existing_ID:
                b_label = tk.Label(root, text="DATA ALREADY AVAILABLE", font=font)
                b_lacel.grid(row=1, column=1, padx=0, pady=10)
            else:
                cursor.execute("insert into stock_data values(%s,%s,%s,%s,%s,%s);",
                               (st_id, opens, high, low, close, year))
                mycon.commit
                messagebox.showinfo("DATA ADDED SUCCESSFULLY")
        else:
            messagebox.showwarning("DETAILS CANNOT BE BLANK ")

    # def delete_data()

    opens_label = tk.Label(root, text="OPENING PRICE: ", font=font)
    opens_label.grid(row=2, padx=100, pady=5, sticky=tk.W)
    opens_entry = tk.Entry(root)
    opens_entry.grid(row=2, column=1, padx=20, pady=10)

    high_label = tk.Label(root, text="HiGHEST PRICE: ", font=font)
    high_label.grid(row=3, padx=100, pady=5, sticky=tk.W)
    high_entry = tk.Entry(root)
    high_entry.grid(row=3, column=1, padx=20, pady=10)

    low_label = tk.Label(root, text="LOWEST PRICE: ", font=font)
    low_label.grid(row=4, padx=100, pady=5, sticky=tk.W)
    low_entry = tk.Entry(root)
    low_entry.grid(row=4, column=1, padx=20, pady=10)

    close_label = tk.Label(root, text="CLOSING PRICE: ", font=font)
    close_label.grid(row=5, padx=100, pady=5, sticky=tk.W)
    close_entry = tk.Entry(root)
    close_entry.grid(row=5, column=1, padx=20, pady=10)

    year_label = tk.Label(root, text="YEAR: ", font=font)
    year_label.grid(row=6, padx=100, pady=5, sticky=tk.W)
    year_entry = tk.Entry(root)
    year_entry.grid(row=6, column=1, padx=20, pady=10)

    st_id_label = tk.Label(root, text="STOCK_ID: ", font=font)
    st_id_label.grid(row=1, padx=100, pady=5, sticky=tk.W)
    st_id_entry = tk.Entry(root)
    st_id_entry.grid(row=1, column=1, padx=20, pady=10)

    add_data_button = tk.Button(root, text="Add Data", font=font, command=add_data)
    add_data_button.grid(row=7, column=1, columnspan=2, padx=0, pady=10)

    delete_data_button = tk.Button(root, text="Delete Data", font=font)
    delete_data_button.grid(row=7, column=3, columnspan=2, padx=0, pady=10)

    update_data_button = tk.Button(root, text="Update Data", font=font)
    update_data_button.grid(row=7, column=5, columnspan=2, padx=0, pady=10)

    graph_button = tk.Button(root, text="PLOT GRAPH", font=font, command=machinelearning)
    graph_button.grid(row=8, column=4, padx=0, pady=10)
    root.mainloop()


register()


