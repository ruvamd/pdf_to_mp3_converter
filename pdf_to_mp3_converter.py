from pypdf import PdfReader
from gtts import gTTS

'''
from pypdf import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
'''

# Open and read the PDF file
pdf_file_path = "11-strategies-of-a-world-class-cybersecurity-operations-center-compressed.pdf"
pdf_reader = PdfReader(pdf_file_path)

# Initialize an empty list to store text from each page
page_texts = []

# Iterate through each page of the PDF file
for page in pdf_reader.pages:
    # Extract text from the current page
    page_text = page.extract_text()
    
    # Append the text to the list
    page_texts.append(page_text)

# Combine text from all pages
combined_text = "\n".join(page_texts)

# Convert the combined text to speech
tts = gTTS(combined_text)

# Save the audio to an MP3 file
output_mp3_path = "output.mp3"
tts.save(output_mp3_path)

print("Conversion complete. Audio saved as 'output.mp3'.")





