import tkinter
from tkinter import messagebox


def login():
    username = "raksha"
    password = "123@"

    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


def forget_window(window):
    window.destroy()
    # global forget_window
    # messagebox.showinfo(title="Forget Password ?", message="Click to Change password..")
    forget_window = tkinter.Tk()
    forget_window.title("Change Password..")
    forget_window.geometry('700x500')
    forget_window.configure(bg='thistle2')
    forget_window_frame = tkinter.Frame(bg='thistle3')

    change_label = tkinter.Label(forget_window_frame, text='CHANGE PASSWORD', bg='plum4', fg='white',
                                 font=("Arial", 30))
    change_label.grid(row=0, column=0, columnspan=2, pady=40)

    username_label = tkinter.Label(forget_window_frame, text="Username", bg='#8F00FF', fg="#FFFFFF",
                                   font=("Arial", 16, 'bold'), width=8, height=1)
    username_label.grid(row=1, column=0)

    password_label = tkinter.Label(forget_window_frame, text="Password", bg='#8F00FF', fg="#FFFFFF",
                                   font=("Arial", 16, 'bold'), width=8, height=1)
    password_label.grid(row=2, column=0)

    username_entry = tkinter.Entry(forget_window_frame, font=("Arial", 16))
    username_entry.grid(row=1, column=1, pady=20)

    password_entry = tkinter.Entry(forget_window_frame, show="*", font=("Arial", 16))
    password_entry.grid(row=2, column=1, pady=20)

    username_entry = tkinter.Entry(forget_window_frame, font=("Arial", 16))
    username_entry.grid(row=1, column=1, pady=20)

    password_entry = tkinter.Entry(forget_window_frame, show="*", font=("Arial", 16))
    password_entry.grid(row=2, column=1, pady=20)

    ok_button = tkinter.Button(forget_window_frame, text="OK", bg="#FFFFFF", fg="#DC143C", font=("Arial", 16),
                               command=login)
    ok_button.grid(row=3, column=1, columnspan=1, pady=30)

    # messagebox.askyesno(title="Confirn to Change Password..", message="Password Changed Succesfully !")

    forget_window_frame.pack()
    forget_window.mainloop()


# __main__

window = tkinter.Tk()
window.title("PREDICTION SYSTEM")
window.geometry('700x500')
window.configure(bg='thistle2')
frame = tkinter.Frame(bg='thistle3', padx=50, pady=30)

login_label = tkinter.Label(frame, text='LOGIN PAGE', bg='plum4', fg='white', font=("Arial", 30))
login_label.grid(row=0, column=0, columnspan=2, sticky="news", padx=30, pady=40)

username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'), width=8,
                               height=1)
username_label.grid(row=1, column=0, padx=10, pady=5)

password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'), width=8,
                               height=1)
password_label.grid(row=2, column=0, padx=10, pady=5)

login_button = tkinter.Button(frame, text="Login", bg="#FFFFFF", fg="#DC143C", font=("Arial", 16), command=login)
login_button.grid(row=3, column=0, columnspan=1, pady=30)

forget_button = tkinter.Button(frame, text="Forget Password ?", bg="#FFFFFF", fg="#DC143C", font=("Arial", 16),
                               command=lambda: forget_window(window))
forget_button.grid(row=3, column=1, columnspan=1, pady=30)

username_entry = tkinter.Entry(frame, font=("Arial", 16))
username_entry.grid(row=1, column=1, padx=10, pady=20)

password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_entry.grid(row=2, column=1, padx=10, pady=20)

frame.pack(padx=110, pady=50)
window.mainloop()
window.destroy()


