# import tkinter as tk
# from tkinter import filedialog, Text
# import os
# import pyttsx3  # Import the text-to-speech library

# class TextToSpeechApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Text to Speech App")
#         self.root.geometry("1980x1080")  # Set window size to 1980x1080

#         # Frame for layout
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(side=tk.LEFT, padx=20, pady=20)

#         # Text Entry Area
#         self.text_area = Text(self.frame, height=40, width=100)
#         self.text_area.pack(pady=10)

#         # Load File Button
#         self.load_button = tk.Button(self.frame, text="Load File", command=self.load_file, height=2, width=20)
#         self.load_button.pack(pady=5)

#         # Speak Button
#         self.speak_button = tk.Button(self.frame, text="Speak", command=self.speak, height=2, width=20)
#         self.speak_button.pack(pady=5)

#         # Animation Indicator
#         self.indicator = tk.Label(self.root, text="", bg="lightblue", width=20)
#         self.indicator.pack(side=tk.LEFT, padx=20)

#         # Move the indicator
#         self.indicator_position = 0
#         self.indicator_moving = False

#         # Initialize the text-to-speech engine
#         self.engine = pyttsx3.init()
        
#         self.set_female_voice()
        
    
#     def set_female_voice(self):
#         voices = self.engine.getProperty('voices')  # Get available voices
#         for voice in voices:
#             if 'female' in voice.name.lower():  # Check for female voice
#                 self.engine.setProperty('voice', voice.id)  # Set female voice
#                 break 

#     def load_file(self):
#         file_path = filedialog.askopenfilename(
#             title="Open File",
#             filetypes=(("PDF files", "*.pdf"), ("Word files", "*.docx"), ("PowerPoint files", "*.pptx"), ("All files", "*.*"))
#         )
#         if file_path:
#             self.read_file(file_path)

#     def read_file(self, file_path):
#         # Placeholder for file reading logic
#         if file_path.endswith('.pdf'):
#             # Implement PDF reading logic
#             pass
#         elif file_path.endswith('.docx'):
#             # Implement DOCX reading logic
#             pass
#         elif file_path.endswith('.pptx'):
#             # Implement PPTX reading logic
#             pass
#         else:
#             print("Unsupported file type!")

#     def speak(self):
#         text = self.text_area.get("1.0", tk.END)  # Get all text from the text area
#         if text.strip():  # Check if there's text to speak
#             if not self.indicator_moving:
#                 self.indicator_moving = True
#                 self.move_indicator()
#                 self.engine.setProperty('rate',130)
#                 self.engine.say(text)  # Convert text to speech
#                 self.engine.runAndWait()  # Wait until speaking is done
#                 self.indicator_moving = False  # Reset indicator movement after speaking

#     def move_indicator(self):
#         if self.indicator_moving:
#             self.indicator_position += 5
#             if self.indicator_position > 180:  # Reset position if it moves too far
#                 self.indicator_position = 0
#             self.indicator.place(x=self.indicator_position, y=500)  # Adjust Y as needed
#             self.root.after(100, self.move_indicator)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TextToSpeechApp(root)
#     root.mainloop()




import tkinter as tk
from tkinter import filedialog, Text
import os
import pyttsx3  # Import the text-to-speech library

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech App")
        self.root.geometry("1980x1080")  # Set window size to 1980x1080

        # Frame for layout
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, padx=20, pady=20)

        # Text Entry Area
        self.text_area = Text(self.frame, height=40, width=100)
        self.text_area.pack(pady=10)

        # Load File Button
        self.load_button = tk.Button(self.frame, text="Load File", command=self.load_file, height=2, width=20)
        self.load_button.pack(pady=5)

        # Speak Button
        self.speak_button = tk.Button(self.frame, text="Speak", command=self.speak, height=2, width=20)
        self.speak_button.pack(pady=5)

        # Animation Indicator on the left
        self.indicator = tk.Label(self.root, text="", bg="lightblue", width=20)
        self.indicator.pack(side=tk.LEFT, padx=20)

        # Animation Component on the right
        self.moving_label = tk.Label(self.root, text="Talking...", bg="lightgreen", width=20)
        self.moving_label.pack(side=tk.RIGHT, padx=20)

        # Move the indicators
        self.indicator_position = 0
        self.indicator_moving = False
        self.label_position = 0
        self.label_moving = False
        self.label_direction = 1  # 1 for down, -1 for up

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()
        self.set_female_voice()

    def set_female_voice(self):
        voices = self.engine.getProperty('voices')  # Get available voices
        for voice in voices:
            if 'female' in voice.name.lower():  # Check for female voice
                self.engine.setProperty('voice', voice.id)  # Set female voice
                break  # Stop after setting the first female voice found

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=(("PDF files", "*.pdf"), ("Word files", "*.docx"), ("PowerPoint files", "*.pptx"), ("All files", "*.*"))
        )
        if file_path:
            self.read_file(file_path)

    def read_file(self, file_path):
        # Placeholder for file reading logic
        if file_path.endswith('.pdf'):
            # Implement PDF reading logic
            pass
        elif file_path.endswith('.docx'):
            # Implement DOCX reading logic
            pass
        elif file_path.endswith('.pptx'):
            # Implement PPTX reading logic
            pass
        else:
            print("Unsupported file type!")

    def speak(self):
        text = self.text_area.get("1.0", tk.END)  # Get all text from the text area
        if text.strip():  # Check if there's text to speak
            if not self.indicator_moving and not self.label_moving:
                self.indicator_moving = True
                self.label_moving = True
                self.move_indicator()
                self.move_label()

                # Set the speech rate
                self.engine.setProperty('rate', 150)  # Adjust this value as needed
                
                self.engine.say(text)  # Convert text to speech
                self.engine.runAndWait()  # Wait until speaking is done
                
                self.indicator_moving = False  # Reset indicator movement after speaking
                self.label_moving = False  # Reset label movement after speaking

    def move_indicator(self):
        if self.indicator_moving:
            self.indicator_position += 5
            if self.indicator_position > 180:  # Reset position if it moves too far
                self.indicator_position = 0
            self.indicator.place(x=self.indicator_position, y=500)  # Adjust Y as needed
            self.root.after(100, self.move_indicator)

    def move_label(self):
        if self.label_moving:
            self.label_position += 5
            
            # Change the y-coordinate to create zigzag motion
            current_y = 500 + (50 * self.label_direction)  # Adjust 50 for the height of zigzag
            self.moving_label.place(x=self.label_position, y=current_y)

            # Change direction if the label reaches certain x-coordinate limits
            if self.label_position > self.root.winfo_width():
                self.label_position = -200  # Reset to start from the left
                self.label_direction *= -1  # Reverse direction
            
            self.root.after(100, self.move_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
