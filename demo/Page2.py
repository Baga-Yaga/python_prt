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