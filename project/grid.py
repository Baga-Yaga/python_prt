from tkinter import *
from tkinter import messagebox

r = Tk()
r.geometry("1080x560")

def login():
    username = uservalue.get()
    password = passvalue.get()
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        
        
user = Label(r,  text="Username",bg="grey",fg="black")
password = Label(r,text="Password" , pady=10,bg="grey",fg="black")
user.grid(padx=10,pady=10)
password.grid(row=1,padx=10,pady=10)


#input
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(r,textvariable=uservalue)
passentry = Entry(r,textvariable=passvalue)

userentry.grid(row=0,column=1,padx=10,pady=10)
passentry.grid(row=1,column=1,padx=10,pady=10) 

b1 = Button(r,text="Submit",bg="green",command=login)
b1.grid(row=2,columnspan=2,padx=10,pady=20)

r.mainloop()