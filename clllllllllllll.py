import tkinter as tk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Switch Frames Example")

# Function to switch frames
def switch_to_frame_1():
    frame2.pack_forget()  # Hide frame2
    frame1.pack()  # Display frame1

def switch_to_frame_2():
    frame1.pack_forget()  # Hide frame1
    frame2.pack()  # Display frame2

# Create frames
frame1 = tk.Frame(root, width=200, height=100, bg="lightblue")
frame2 = tk.Frame(root, width=200, height=100, bg="lightgreen")

frame1.pack_propagate(False)  # Prevents frame resizing to its contents
frame2.pack_propagate(False)

# Adding some widgets to frames
label_frame1 = tk.Label(frame1, text="Frame 1", font=('Arial', 18), bg="lightblue")
label_frame1.pack(padx=20, pady=20)

label_frame2 = tk.Label(frame2, text="Frame 2", font=('Arial', 18), bg="lightgreen")
label_frame2.pack(padx=20, pady=20)

# Show frame 1 by default
frame1.pack()

# Create buttons to switch frames
switch_button1 = tk.Button(root, text="Switch to Frame 1", command=switch_to_frame_1)
switch_button1.pack()

switch_button2 = tk.Button(root, text="Switch to Frame 2", command=switch_to_frame_2)
switch_button2.pack()

root.mainloop()