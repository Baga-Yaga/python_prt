import turtle

def clk():
    import Page2

z = turtle.Turtle()
z.shapesize(2,2)
z.color('cyan')
z.pensize(10)
z.shape('turtle')
turtle.bgcolor('black')
turtle.setup(800,600,startx=400,starty=150)
turtle.onclick(clk,btn=1,add=None)

z.penup()
z.backward(190)
z.left(90)
z.forward(190)
z.pendown()
z.speed(0)

def e ():
    z.forward(30)
    z.backward(30)
    z.right(90)
    z.forward(30)
    z.left(90)
    z.forward(20)
    z.backward(20)
    z.right(90)
    z.forward(30)
    z.left(90)
    z.forward(30)

def o ():
    for i in range(2):
        z.forward(30)
        z.left(90)
        z.forward(60)
        z.left(90)

# W
z.right(180)
z.forward(60)
z.left(135)
z.forward(30)
z.right(90)
z.forward(30)
z.left(135)
z.forward(60)

# E
z.penup()
z.right(90)
z.forward(20)
z.pendown()

e()

#L
z.penup()
z.forward(20)
z.pendown()
z.forward(30)
z.backward(30)
z.left(90)
z.forward(60)

#C
z.penup()
z.right(90)
z.forward(50)
z.pendown()
z.forward(30)
z.backward(30)
z.right(90)
z.forward(60)
z.left(90)
z.forward(30)

#O
z.penup()
z.forward(20)
z.pendown()
o()

#M
z.penup()
z.forward(50)
z.pendown()
z.left(90)
z.forward(60)
z.right(135)
z.forward(30)
z.left(90)
z.forward(30)
z.right(135)
z.forward(60)

#E
z.penup()
z.left(90)
z.forward(20)
z.left(90)
z.forward(60)
z.right(90)
z.pendown()
e()

#T
z.penup()
z.right(90)
z.forward(60)
z.right(90)
z.forward(220)
z.pendown()
z.backward(40)
z.forward(20)
z.left(90)
z.forward(60)

#O
z.penup()
z.left(90)
z.forward(40)
z.pendown()
o()

#A
z.penup()
z.right(90)
z.forward(60)
z.right(90)
z.forward(220)
z.pendown()
z.left(70)
z.forward(70)
z.backward(70)
z.left(40)
z.forward(70)
z.backward(30)
z.right(110)
z.forward(25)

#U
z.penup()
z.right(125)
z.forward(40)
z.right(55)
z.forward(35)
z.pendown()
z.right(90)
z.forward(60)
z.left(90)
z.forward(40)
z.left(90)
z.forward(60)

#D
z.speed(0)
z.penup()
z.right(90)
z.forward(20)
z.pendown()
z.right(90)
z.forward(60)
z.left(90)
z.forward(10)
for a in range(95):
    z.left(1.9)
    z.fd(1)
z.forward(10)
# z.speed(7)

#I
z.penup()
z.right(0.5)
z.backward(50)
z.pendown()
z.backward(40)
z.forward(20)
z.left(90)
z.forward(60)
z.right(90)
z.forward(20)
z.backward(40)

#O
z.penup()
z.backward(20)
z.right(180)
z.pendown()
o()

#B
z.penup()
z.forward(50)
z.pendown()
# o()
# z.left(90)
# z.forward(30)
# z.right(90)
# z.forward(30)
# z.right(90)
# z.forward(30)
# z.left(90)
z.left(90)
z.forward(60)
z.right(90)
z.forward(15)
for a in range(45):
    z.right(4)
    z.fd(1)
z.forward(13)
z.right(180)
z.forward(17)
for a in range(45):
    z.right(4)
    z.fd(1)
z.forward(15)
z.left(180)
z.forward(22)

#oo
for a in range(2):
    z.penup()
    z.forward(20)
    z.pendown()
    o()
    z.forward(30)

#k
z.penup()
z.forward(20)
z.pendown()
z.left(90)
z.forward(60)
z.backward(30)
z.right(45)
z.forward(40)
z.backward(40)
z.right(90)
z.forward(40)
z.left(45)
z.forward(15)

a=0
turtle.bgcolor('black')
while a<4:
    z.left(90)
    z.speed(1)
    a = a + 1

# turtle.mainloop()
# turtle.hideturtle()
# turtle.clear()
import Page2



import tkinter as tk
from tkinter import filedialog, ttk
import pyttsx3
import PyPDF2
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
lock = threading.Lock()

def speak_text():
    text = text_box.get("1.0", "end-1c")
    if text:
        threading.Thread(target=run_speak, args=(text,)).start()

def run_speak(text):
    with lock:
        engine.say(text)
        engine.runAndWait()

def read_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join(page.extract_text() for page in reader.pages)
            text_box.delete("1.0", "end")
            text_box.insert("1.0", text)

def stop_speech():
    with lock:
        engine.stop()

def reset():
    text_box.delete("1.0", "end")
    stop_speech()

def change_rate(event):
    speeds = {"Slow": 60, "Medium": 150, "Fast": 260}
    engine.setProperty('rate', speeds[speed_var.get()])

def change_voice(event):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id if voice_var.get() == "Male" else voices[1].id)

root = tk.Tk()
root.title("Text to Speech and PDF Reader")
root.geometry("800x600")
root.configure(bg="light blue")

text_box = tk.Text(root, height=15, width=80, font=("Arial", 14))
text_box.pack(pady=10, padx=(20, 20))

control_frame = tk.Frame(root, bg="light blue")
control_frame.pack(pady=10)

buttons = [
    ("Speak Text", speak_text),
    ("Stop", stop_speech),
    ("Open PDF", read_pdf),
    ("Reset", reset)
]
for text, command in buttons:
    tk.Button(control_frame, text=text, command=command, bg="light green", fg="black", font=("Arial", 12), padx=10, pady=5).grid(row=0, column=buttons.index((text, command)), padx=10, pady=5)

speed_var = tk.StringVar(value="Medium")
tk.Label(control_frame, text="Adjust Reading Speed:", bg="light blue", fg="dark blue", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
speed_combobox = ttk.Combobox(control_frame, textvariable=speed_var, values=["Slow", "Medium", "Fast"], state="readonly", font=("Arial", 12))
speed_combobox.grid(row=1, column=1, padx=10, pady=5)
speed_combobox.bind("<<ComboboxSelected>>", change_rate)

voice_var = tk.StringVar(value="Male")
tk.Label(control_frame, text="Select Voice:", bg="light blue", fg="dark blue", font=("Arial", 12)).grid(row=1, column=2, padx=10, pady=5)
voice_combobox = ttk.Combobox(control_frame, textvariable=voice_var, values=["Male", "Female"], state="readonly", font=("Arial", 12))
voice_combobox.grid(row=1, column=3, padx=10, pady=5)
voice_combobox.bind("<<ComboboxSelected>>", change_voice)

root.mainloop()