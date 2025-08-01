import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3

# Get voices once
voices = pyttsx3.init().getProperty('voices')

def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        selected_index = voice_var.get().split(":")[0]
        engine.setProperty('voice', voices[int(selected_index)].id)
        engine.setProperty('rate', rate_var.get())
        engine.setProperty('volume', volume_var.get() / 100.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

def clear_text():
    text_input.delete("1.0", tk.END)

def load_from_file():
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🗣️ Offline Text-to-Speech")
root.geometry("600x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TCombobox", font=("Segoe UI", 10), padding=4)

# Title
ttk.Label(root, text="Offline Text-to-Speech Generator", font=("Segoe UI Semibold", 14)).pack(pady=10)

# Text Input
ttk.Label(root, text="Enter your text below:").pack()
text_input = tk.Text(root, height=6, width=65, font=("Segoe UI", 10), wrap=tk.WORD,
                     bg="#2d2d2d", fg="white", insertbackground="white", borderwidth=0, padx=10, pady=10)
text_input.pack(pady=5)

# Voice Dropdown
ttk.Label(root, text="Choose a Voice:").pack(pady=(10, 0))
voice_var = tk.StringVar()
voice_dropdown = ttk.Combobox(root, textvariable=voice_var, state="readonly", width=55)
voice_dropdown['values'] = [f"{i}: {voice.name}" for i, voice in enumerate(voices)]
voice_dropdown.current(0)
voice_dropdown.pack(pady=5)

# Rate Slider
ttk.Label(root, text="Speech Rate:").pack(pady=(10, 0))
rate_var = tk.IntVar(value=150)
rate_slider = ttk.Scale(root, from_=100, to=300, variable=rate_var, orient="horizontal", length=300)
rate_slider.pack(pady=5)

# Volume Slider
ttk.Label(root, text="Volume:").pack(pady=(10, 0))
volume_var = tk.IntVar(value=90)
volume_slider = ttk.Scale(root, from_=0, to=100, variable=volume_var, orient="horizontal", length=300)
volume_slider.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)

ttk.Button(button_frame, text="🔊 Speak", command=speak_text).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="🧹 Clear", command=clear_text).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="📂 Load from File", command=load_from_file).grid(row=0, column=2, padx=10)

# Footer
ttk.Label(root, text="Built with ❤️ using pyttsx3", font=("Segoe UI", 9)).pack(side="bottom", pady=10)

root.mainloop()
