from tkinter import *
from tkinter import messagebox

def login():
    username = uservalue.get()
    password = passvalue.get()
    
    # Sample validation (you can customize this)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
r = Tk()
r.title("Login Page")
r.geometry("300x150")

# Labels
user_label = Label(r, text="Username", font="Arial 12")
user_label.grid(row=0, column=0, padx=10, pady=10)

# Entry for username
uservalue = StringVar()
user_entry = Entry(r, textvariable=uservalue)
user_entry.grid(row=0, column=1, padx=10, pady=10)

# Labels
pass_label = Label(r, text="Password", font="Arial 12")
pass_label.grid(row=1, column=0, padx=10, pady=10)

# Entry for password
passvalue = StringVar()
pass_entry = Entry(r, textvariable=passvalue, show='*')
pass_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit button
submit_button = Button(r, text="Submit", command=login, bg="green")
submit_button.grid(row=2, columnspan=2, pady=20)

# Run the application
r.mainloop()
