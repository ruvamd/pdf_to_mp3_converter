import tkinter as tk
from tkinter import filedialog
from gtts import gTTS

def select_text_file():
    # Open file dialog to select a text file
    text_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if text_file_path:
        selected_file_label.config(text=f"Selected Text File: {text_file_path}")
        convert_button.config(state=tk.NORMAL)  # Enable the convert button

def convert_text_to_mp3():
    text_file_path = selected_file_label.cget("text").split(": ")[1]

    # Read the text from the selected .txt file
    with open(text_file_path, "r", encoding="ISO-8859-1") as text_file:
        text = text_file.read()

    # Convert the text to speech
    tts = gTTS(text)

    # Save the audio to an MP3 file
    output_mp3_path = "output.mp3"
    tts.save(output_mp3_path)

    result_label.config(text="Conversion complete. Audio saved as 'output.mp3'.")

# Create the main window
app = tk.Tk()
app.title("Text to MP3 Converter")

# Create and pack widgets
select_file_button = tk.Button(app, text="Select Text File", command=select_text_file)
select_file_button.pack(pady=10)

selected_file_label = tk.Label(app, text="Selected Text File: None")
selected_file_label.pack(pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_text_to_mp3, state=tk.DISABLED)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the main loop
app.mainloop()
