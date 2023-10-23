from pypdf import PdfReader
from gtts import gTTS

# Open and read the PDF file
pdf_file_path = "11-strategies-of-a-world-class-cybersecurity-operations-center.pdf"  # Replace with your PDF file path
pdf_reader = PdfReader(pdf_file_path)

# Specify the number of pages to convert (e.g., the first 100 pages)
pages_to_convert = 100

# Initialize an empty list to store text from each page
page_texts = []

# Iterate through the first 100 pages of the PDF
for page in pdf_reader.pages[:pages_to_convert]:
    # Extract text from the current page
    page_text = page.extract_text()
    page_texts.append(page_text)

# Combine text from the selected pages
combined_text = "\n".join(page_texts)

# Convert the combined text to speech
tts = gTTS(combined_text)

# Save the audio to an MP3 file
output_mp3_path = "first_100_pages.mp3"
tts.save(output_mp3_path)

print("Conversion complete. Audio for the first 100 pages saved as 'first_100_pages.mp3'.")
