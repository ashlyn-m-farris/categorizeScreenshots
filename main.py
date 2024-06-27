from findDates import *
from OCR import *
from findAuthors import *
from categorize import *
from groupTriples import *
from determinePlatform import *



#Get image input, pass to OCR and output OCR results
img = input('Please enter image pathway: ')
results = OCR(img)
print(results)

authors = findAuthors(results)
print(authors)
dates = findDates(formatDates(results))
h_m = hmFormat(results)

#DetermineStructure
print(f"The Internal category is {categorize(dates, h_m, authors)}.")
print(f"The Platform is {determinePlatform(results)}.")

triples = groupTriples(results, authorLines(results))
i = 1
for triple in triples:
    authors = findAuthors(triple)
    dates = findDates(formatDates(triple))
    h_m = hmFormat(triple)
    
    print(f'**********************BEGIN GROUP {i}***************************')
    print(triple)

    print('Author:')
    for author in authors:
        print(author)

    print('\n')

    print('Date:')
    if (len(dates) == 0):
        print('No Full Timestamp')
    else:
        for date in dates:
            print(date)
            
    if len(h_m) > 0:
        for time in h_m:
            print(time)
    print(f'***********************END Group {i}****************************')
    i += 1
    print('\n')