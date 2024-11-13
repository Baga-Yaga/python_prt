import tkinter as tk
from tkinter import *

# creating main window

top=Tk()
top.geometry("700x500+400+150")
top.maxsize(700, 500)
top.minsize(700, 500)
top.resizable(False,False)
top.config(bg="light yellow")
top.title('Audio Book')

def convert_page():
    # top.destroy()
    import page3

def recording_page():
    # top.destroy()
    import page4

def back():
    top.destroy()
    exit()

#Top Frame
left_frame=Frame(top,bg="white",width=350,height=500)#,borderwidth=9
left_frame.pack(side=LEFT)
right_frame=Frame(top,bg="#8207FA",width=350,height=500)#,borderwidth=9
right_frame.pack(side=RIGHT)

#Center Text
b = Label(top, text="Welcome to", font=("TimesNewRoman", 30, "bold"), bg="white")
b.pack(padx=10, pady=20, side="top")
b.place(x=20,y=140)
d = Label(top, text="AudioBook", font=("TimesNewRoman", 30, "bold"), bg="white")
d.pack(padx=70, pady=20, side="top")
d.place(x=100,y=240)


#Buttons
b1=Button(top,text="Audio Conversion",font=("TimesNewRoman", 14, "bold"),bg="white",fg="black",command=convert_page)
b1.pack()
b1.place(x=430,y=150)


b2=Button(top,text="Previous Recordings",font=("TimesNewRoman", 14, "bold"),bg="white",fg="black",command=recording_page)
b2.pack(fill=X)
b2.place(x=420,y=250)

b3=Button(top,text="Exit",font=("TimesNewRoman", 14, "bold"),bg="white",fg="black",command=back)
b3.pack()
b3.place(x=500,y=350)

top.mainloop()