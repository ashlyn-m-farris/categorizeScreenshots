import pytesseract
import datefinder
import re

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string('screenshotImg/Jun3_24_1.jpg')
print(text)