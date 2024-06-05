import pytesseract
import datefinder
import re
import json

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string('images/PNA1/May30_24_16.jpg')
print(text)

handles = re.findall('@\w{4,15}', text)
print(handles)

if (len(handles)) > 1:
    print("AN")
