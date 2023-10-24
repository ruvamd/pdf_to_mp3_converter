from gtts import gTTS

# Read the text from the .txt file
with open("/Users/vadim/Documents/education/UW/ISSEC 310 A Au 23/module 3/11-strategies-of-a-world-class-cybersecurity-operations-center.txt", "r", encoding="ISO-8859-1") as text_file:
    text = text_file.read()

# Convert the text to speech
tts = gTTS(text)

# Save the audio to an MP3 file
tts.save("output.mp3")

print("Conversion complete. Audio saved as 'output.mp3'.")
