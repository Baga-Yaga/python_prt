import tkinter as tk
from tkinter import messagebox

def check_login():
    username = entry_username.get()
    password = entry_password.get()

    correct_username = "amar"
    correct_password = "amar"

    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Success", "You have logged in successfully!")
        root.quit()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, width=30, show="*")  
entry_password.pack(pady=5)

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack(pady=10)

root.mainloop()
