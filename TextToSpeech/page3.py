from tkinter import *
import pyttsx3
import pygame
from tkinter import ttk

z = Tk()
z.geometry("700x500+400+150")
z.configure(bg="light yellow")
z.maxsize(700, 500)
z.minsize(700, 500)
a = Frame(z, bg="#8207FA", height=50)
a.pack(side="top", anchor=NW, fill=X)
n = "."
pygame.mixer.init()


def gen():
    id = 0
    if aud.get() == "Male":
        id = 0
    else:
        id = 1
    return id


def rate():
    spd = 178
    if aud2.get() == "Fast":
        spd = 270
    elif aud2.get() == "Slow":
        spd = 60
    elif aud2.get() == "Medium":
        spd = 178

    return spd


def to_mp3():
    if enty.get() == "":
        pygame.mixer.music.load('z_warning_mp3')
        pygame.mixer.music.play()
    else:
        str1 = inp.get(1.0, "end-1c")
        y = pyttsx3.init()
        voices = y.getProperty('voices')
        y.setProperty('voice', voices[gen()].id)
        y.setProperty('rate', rate())
        y.say(str1)
        y.save_to_file(str1, f"{enty.get()}_mp3")
        y.runAndWait()
        pygame.mixer.music.load('z_confirmation_mp3')
        pygame.mixer.music.play()


def to_audio():
    str1 = inp.get(1.0, "end-1c")
    y = pyttsx3.init()
    voices = y.getProperty('voices')
    for voice in voices:
        print(voice.name)
    y.setProperty('voice', voices[gen()].id)
    y.setProperty('rate', rate())
    y.say(str1)
    y.runAndWait()


def back():
    z.destroy()
    import page2

b = Label(a, text="Welcome to AudioBook", font=("TimesNewRoman", 24, "bold"), bg="#8207FA", fg="white")
b.pack(padx=70, pady=20, side="top", anchor=NW)
# b.place(x=)
d = Label(a, text="Add your Text here", font=("TimesNewRoman", 24, "bold"), bg="#8207FA", fg="white")
d.pack(padx=10, pady=10, side="top")

# label-Enter text here
lab1 = Label(z, text="Enter your text Here", font=("TimesNewRoman", 18, "bold"), fg="black", bg="light yellow")
lab1.pack()
lab1.place(x=235, y=160)

# label - choose audio voice type
lab2 = Label(z, text="Voice  Type", font=("TimesNewRoman", 13, "bold"), fg="black", bg="light yellow")
lab2.pack()
lab2.place(x=210, y=310)

# combo1-type
stg = StringVar()
aud = ttk.Combobox(z, values=["Male", "Female"], font=("TimesNewRoman", 10, "bold"), textvariable=stg)
aud.pack()
aud.place(x=190, y=340)
aud.set("Female")

# label - choose audio speed
lab2 = Label(z, text="Audio Speed", font=("TimesNewRoman", 13, "bold"), fg="black", bg="light yellow")
lab2.pack()
lab2.place(x=375, y=310)

# combo1-type
stg2 = StringVar()
aud2 = ttk.Combobox(z, values=["Fast", "Medium", "Slow"], font=("TimesNewRoman", 10, "bold"), textvariable=stg2)
aud2.pack()
aud2.place(x=360, y=340)
aud2.set("Medium")

# textbox
inp = Text(z, height=6, width=43)
inp.pack()
inp.place(x=180, y=200)

# but1-play
but1 = Button(z, text="Play", command=to_audio, font=("TimesNewRoman", 13, "bold"), bg="#8207FA", fg="white")
but1.pack(pady=20, padx=20)
but1.place(x=190, y=390)

# but3-convert to mp3
but3 = Button(z, text="Convert to Mp3", command=to_mp3, font=("TimesNewRoman", 13, "bold"), bg="#8207FA", fg="white")
but3.pack(pady=20, padx=20)
but3.place(x=283, y=390)

# but4-back
but4 = Button(z, text="Back", command=back, font=("TimesNewRoman", 13, "bold"), bg="#8207FA", fg="white")
but4.pack(pady=20, padx=20)
but4.place(x=460, y=390)

# lab3-file name,
lab3 = Label(z, text="Enter File Name", font=("TimesNewRoman", 12, "bold"), fg="black", bg="light yellow")
lab3.pack()
lab3.place(x=200, y=450)

# enty-file name
str = StringVar()
enty = Entry(z, textvariable=str)
enty.pack()
enty.place(x=330, y=450)

print(enty.get())

z.mainloop()
