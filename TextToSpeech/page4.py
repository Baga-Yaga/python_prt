from tkinter import *
from tkinter import ttk
import glob
import pygame

root = Tk()
root.geometry("700x500+400+150")
root.maxsize(700, 500)
root.minsize(700, 500)
root.configure(bg="white")

lab1 = Label(root, text="Previous ", font=("TimesNewRoman", 34, "bold"), bg="white", fg="black")
lab1.pack(pady=20)
lab1.place(x=10, y=140)

lab2 = Label(root, text="Recordings ", font=("TimesNewRoman", 34, "bold"), bg="white", fg="black")
lab2.pack(pady=20)
lab2.place(x=50, y=240)

def back():
    root.destroy()
    import page2

but1 = Button(root, text="Back", font=("TimesNewRoman", 12, "bold"), command=back,bg="black",fg="white")
but1.pack(side=BOTTOM, pady=10, padx=20)
but1.place(x=200,y=440)

# main Frame
main_frame = Frame(root,width=300,bg="#8207FA")
main_frame.pack(side=RIGHT,fill=Y)#, expand=1

# canvas
canvas = Canvas(main_frame,bg="#8207FA")
canvas.pack(side=LEFT, fill=Y)#, expand=1

# scroll
scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scroll.pack(side=RIGHT, fill=Y)

# configure
canvas.configure(yscrollcommand=scroll.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# another frame
sec_frame = Frame(canvas,bg="#8207FA")

# frame to a window
canvas.create_window((300, 0), window=sec_frame, anchor=SE)

def play(var):
    pygame.mixer.init()
    pygame.mixer.music.load(var)
    pygame.mixer.music.play()

mp3_files = glob.iglob('**/*_mp3', recursive=True)
var = 0
for mp3 in mp3_files:
    var = mp3
    mp3 = Button(sec_frame, text=mp3, font=("TimesNewRoman", 14, "bold"),bg="white", fg="black",
                 command=lambda var=mp3: play(var))
    # print(f"{mp3}")
    mp3.pack(padx=10, pady=20)
    # root.create_window(window=var)

root.mainloop()
