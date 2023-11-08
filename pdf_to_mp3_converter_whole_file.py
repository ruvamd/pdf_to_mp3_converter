import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pypdf import PdfReader
from gtts import gTTS

def select_pdf_file():
    # Open file dialog to select a PDF file
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if pdf_file_path:
        selected_file_label.config(text=f"Selected PDF: {pdf_file_path}")
        convert_button.config(state=tk.NORMAL)  # Enable the convert button

def convert_pdf_to_mp3():
    pdf_file_path = selected_file_label.cget("text").split(": ")[1]

    # Open and read the PDF file
    pdf_reader = PdfReader(pdf_file_path)

    # Initialize an empty list to store text from each page
    page_texts = []

    # Get the total number of pages for the progress bar
    total_pages = len(pdf_reader.pages)

    # Configure progress bar
    progress_bar["maximum"] = total_pages
    progress_bar["value"] = 0

    # Iterate through each page of the PDF file
    for i, page in enumerate(pdf_reader.pages, start=1):
        # Extract text from the current page
        page_text = page.extract_text()

        # Append the text to the list
        page_texts.append(page_text)

        # Update progress bar
        progress_bar["value"] = i
        app.update_idletasks()

    # Combine text from all pages
    combined_text = "\n".join(page_texts)

    # Convert the combined text to speech
    tts = gTTS(combined_text)

    # Save the audio to an MP3 file
    output_mp3_path = "output.mp3"
    tts.save(output_mp3_path)

    result_label.config(text="Conversion complete. Audio saved as 'output.mp3'.")
    progress_bar["value"] = 0

# Create the main window
app = tk.Tk()
app.title("PDF to MP3 Converter")

# Create and pack widgets
select_file_button = tk.Button(app, text="Select PDF File", command=select_pdf_file)
select_file_button.pack(pady=10)

selected_file_label = tk.Label(app, text="Selected PDF: None")
selected_file_label.pack(pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_pdf_to_mp3, state=tk.DISABLED)
convert_button.pack(pady=10)

# Create progress bar
progress_bar = ttk.Progressbar(app, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the main loop
app.mainloop()
