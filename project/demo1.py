import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 110)

def speak_text():
    # Use threading to prevent the GUI from freezing or causing segmentation faults
    text = text_box.get("1.0", "end-1c")
    if text:
        threading.Thread(target=run_speak, args=(text,)).start()

def run_speak(text):
    engine.say(text)
    engine.runAndWait()

def read_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            # Display the extracted text in the text box
            text_box.delete("1.0", "end")
            text_box.insert("1.0", text)

def stop_speech():
    engine.stop()

def reset():
    text_box.delete("1.0", "end")
    stop_speech()

def change_rate(rate):
    engine.setProperty('rate', rate)

root = tk.Tk()
root.title("Text to Speech and PDF Reader")
root.geometry("800x600")

text_box = tk.Text(root, height=15, width=100)
text_box.pack(pady=10)

speak_button = tk.Button(root, text="Speak Text", command=speak_text)
speak_button.pack(pady=5)

load_pdf_button = tk.Button(root, text="Load PDF", command=read_pdf)
load_pdf_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Speech", command=stop_speech)
stop_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=5)

rate_label = tk.Label(root, text="Adjust Reading Speed:")
rate_label.pack(pady=5)

rate_slider = tk.Scale(root, from_=50, to=300, orient="horizontal", command=lambda value: change_rate(int(value)))
rate_slider.set(150)  
rate_slider.pack(pady=5)

root.mainloop()
