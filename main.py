from findDates import *
from OCR import *
from findAuthors import *
from categorize import *

#Get image input, pass to OCR and output OCR results
img = input('Please enter image pathway: ')
results = OCR(img)
print(results)

#Pass OCR results to findAuthors, findDates, and hmFormat
authors = findAuthors(results)
dates = findDates(formatDates(OCR(img)))
h_m = hmFormat(OCR(img))

#Output possible authors
print('Possible Authors Are:')
for author in authors:
    print(author)
print('\n')

#Output possible dates
print('Possible Time-frames Are:')
if (len(dates) == 0):
    print("No Dates Found")
else:
    for date in dates:
        print(date)
if len(h_m) > 0:
    print('\n')
    print('Other posts within image are likely within m/h of timeframe')
    for time in h_m:
        print(time)
print('\n')

#DetermineStructure
print(f"The Category is: {categorize(dates, h_m, authors)}")




