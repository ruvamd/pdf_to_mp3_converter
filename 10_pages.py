from pypdf import PdfReader
from gtts import gTTS
import time

# Open and read the PDF file
pdf_file_path = "/Users/vadim/Documents/education/UW/ISSEC 310 A Au 23/module 3/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf"  # Replace with your PDF file path
pdf_reader = PdfReader(pdf_file_path)

# Specify the number of pages per segment
pages_per_segment = 10

# Initialize a variable to keep track of the page number
page_number = 0

# Initialize a segment counter
segment_counter = 1

# Initialize a variable to store the combined text from all segments
all_text = ""

# Iterate through the PDF pages
for page in pdf_reader.pages:
    # Extract text from the current page
    page_text = page.extract_text()

    # Increment the page number
    page_number += 1

    # Append the text to the combined text
    all_text += page_text

    # Check if we have processed the desired number of pages for this segment
    if page_number % pages_per_segment == 0:
        # Check if there is text to speak
        if all_text.strip():
            # Save the combined text to a text file for this segment
            segment_text_file = f"segment_{segment_counter}.txt"
            with open(segment_text_file, 'w', encoding='utf-8') as text_file:
                text_file.write(all_text)

            # Convert the combined text to speech
            tts = gTTS(all_text)

            # Save the audio to an MP3 file for this segment
            output_mp3_path = f"segment_{segment_counter}.mp3"
            tts.save(output_mp3_path)

            print(f"Segment {segment_counter} conversion complete. Audio saved as '{output_mp3_path}'.")

            # Increment the segment counter
            segment_counter += 1

            # Reset the combined text variable
            all_text = ""

        # Add a delay of 10 seconds to respect rate limits
        time.sleep(10)

# Check if there are remaining pages in the last segment
if all_text.strip():
    # Save the combined text to a text file for the last segment
    segment_text_file = f"segment_{segment_counter}.txt"
    with open(segment_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(all_text)

    # Convert the combined text to speech
    tts = gTTS(all_text)

    output_mp3_path = f"segment_{segment_counter}.mp3"
    tts.save(output_mp3_path)

    print(f"Last segment conversion complete. Audio saved as '{output_mp3_path}'.")
