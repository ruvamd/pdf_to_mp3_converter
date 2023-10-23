from pypdf import PdfReader
from gtts import gTTS

# Open and read the PDF file
pdf_file_path = "11-strategies-of-a-world-class-cybersecurity-operations-center.pdf"  # Replace with your PDF file path
pdf_reader = PdfReader(pdf_file_path)

# Determine the total number of pages in the PDF
total_pages = len(pdf_reader.pages)

# Specify the number of pages to include in each segment
pages_per_segment = 100

# Initialize a counter to keep track of segments
segment_counter = 1

# Initialize an empty list to store text from each segment
segment_texts = []

# Iterate through each page of the PDF
for page in pdf_reader.pages:
    # Extract text from the current page
    page_text = page.extract_text()

    # Append the text to the segment's list
    segment_texts.append(page_text)

    # Check if the current segment is complete (reached 100 pages)
    if len(segment_texts) == pages_per_segment:
        # Combine text from the segment
        combined_text = "\n".join(segment_texts)

        # Convert the combined text to speech
        tts = gTTS(combined_text)

        # Save the audio to an MP3 file for this segment
        output_mp3_path = f"segment_{segment_counter}.mp3"
        tts.save(output_mp3_path)

        print(f"Segment {segment_counter} conversion complete. Audio saved as '{output_mp3_path}'.")

        # Increment the segment counter
        segment_counter += 1

        # Reset the segment's text list
        segment_texts = []

# After processing all pages, check if there are remaining pages in the last segment
if segment_texts:
    # Combine text from the last segment
    combined_text = "\n".join(segment_texts)

    # Convert the combined text to speech
    tts = gTTS(combined_text)

    # Save the audio to an MP3 file for the last segment
    output_mp3_path = f"segment_{segment_counter}.mp3"
    tts.save(output_mp3_path)

    print(f"Last segment conversion complete. Audio saved as '{output_mp3_path}'.")
