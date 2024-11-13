# from tkinter import * 

# root = Tk()
# root.geometry("1080x560")
# root.title("Frame")

# f1 = Frame(root,bg="yellow",width=200,height=100)
# f1.pack(side="top",anchor="center")

# # l = Label(f1,text="Hello")
# # l.pack()

# f2 = Frame(root,bg="red",width=400,height=260)
# f2.pack(side="right")
# l1 = Label(f2,text="Demo",fg="white",bg="red")
# l1.pack()

# root.mainloop()


from tkinter import *

r = Tk()
r.title("VsCode")
r.geometry("1980x1080")

def hello():
    print("Hello its Me your friend!")



f1 = Frame(r,bg="grey", width=220,relief=SUNKEN)
f1.pack(side="left",fill=Y)

f2 = Frame(r,bg="black",width=1760,height=780,relief=SUNKEN)
f2.pack(fill=X,side="top")

f3 = Frame(r,bg="yellow",width=1760,height=260,relief=SUNKEN)
f3.pack(side="bottom")

b1 = Button(f2, bg="white", text="Click here",command=hello)
b1.pack()



r.mainloop()