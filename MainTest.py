from findDates import *
from OCR import *
from findAuthors import *
from categorize import *
from groupTriples import *
import sys

# Save the original stdout
original_stdout = sys.stdout

# Redirect stdout to a file
with open('output.txt', 'w') as f: 
    sys.stdout = f
    with open("DGScreenshots.txt", "r") as file:
        while True:
            if not (path := file.readline().replace('\n', '')):
                break
            print('**********************NEW SCREENSHOT***************************')
            print(path)
            print('\n')
            #Get image input, pass to OCR and output OCR results
            results = OCR(path)
            #print(results)

            authors = findAuthors(results)
            dates = findDates(formatDates(results))
            h_m = hmFormat(results)

            #DetermineStructure
            print({categorize(dates, h_m, authors)})

            triples = groupTriples(results, authorLines(results))
            i = 1
            for triple in triples:
                authors = findAuthors(triple)
                dates = findDates(formatDates(triple))
                h_m = hmFormat(triple)
                
                #print(f'**********************BEGIN GROUP {i}***************************')
                #print(triple)

                #print('Author:')
                #for author in authors:
                    #print(author)

                #print('\n')

                #print('Date:')
                #if (len(dates) == 0):
                    #print('No Full Timestamp')
                #else:
                    #for date in dates:
                       #print(date)
                        
                #if len(h_m) > 0:
                    #for time in h_m:
                        #print(time)
                #print(f'***********************END Group {i}****************************')
                i += 1
                #print('\n')