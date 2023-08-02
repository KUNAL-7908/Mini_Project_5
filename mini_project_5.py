# Mini Project 5

# Install the following libraries before proceeding:
# !sudo apt install tesseract-ocr
# !pip install pytesseract
# !pip install Pillow==9.0.0
# !pip install gTTS


# Import Required Libraries
import pytesseract  
from PIL import Image 
import pygame
import gtts

# Open The image
img = Image.open('D:\Coding\Python programmming\summer_school\image.png')
print(img)

# Extract Text From the image
result = pytesseract.image_to_string(Image.open('D:\Coding\Python programmming\summer_school\image.png'))
print(result)

#Initialize the gTTS (Google Text-to-Speech) object with the extracted text
tts = gtts.gTTS(result)
# Saving the text as an audio file:
tts.save("audio_file.mp3")