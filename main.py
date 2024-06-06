from findDates import *
from OCR import *
from findAuthors import *

img = input('Please enter image pathway: ')
results = OCR(img)
authors = findAuthors(results)


print('Possible Authors Are:')
for author in authors:
    print(author)
print('\n')


dates = findDates(formatDates(OCR(img)))
print('Possible Time-frames Are:')
if (dates == "No Dates Found"):
    print(dates)
else:
    for date in dates:
        print(date)
print('\n')




