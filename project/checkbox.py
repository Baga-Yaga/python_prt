from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox

r = Tk()
r.title("CheckBox")
r.geometry("1080x560")

def submit():
    if ch_var.get():
        messagebox.showinfo("Ordered Succcessfullt","Ordered")
    else:
        messagebox.showerror("Unsuccessfull", "not orderd")


l1 = Label(r, text="Buy Products", bg="purple",fg="black")
l1.pack(side="top",fill=X,)
f1 = Frame(r,width=520, height=360,bg="grey")
f1.pack(fill="x",side="top")

Label(f1, text="Product Name ",padx=5,pady=5,fg="black",bg="grey").grid(row=0,column=0,)
Label(f1, text="Quantity ",padx=5,pady=5,fg="black",bg="grey").grid(row=1,column=0)

prd_value = StringVar()
qty_value = IntVar()

Entry(f1,textvariable=prd_value).grid(row=0,column=1)
Entry(f1,textvariable=qty_value).grid(row=1,column=1)

ch_var = BooleanVar()
ch1 = Checkbutton(f1,text="Agreee terms and conditions!",variable=ch_var).grid(row=2,columnspan=2)


b1 = Button(f1,text="Submit",command=submit).grid(row=3,columnspan=2)

r.mainloop()