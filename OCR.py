import pytesseract

#Use Python Tesseract to extract all of the text from a screenshot and print the results
def OCR(img):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    return(pytesseract.image_to_string(img))
