import datefinder
from OCR import *
from conversions import *
import re

#def extractDates(text):
def formatDates(text):
        dates = []
        for line in re.split('\n', text):
                #00/00/00 or 0/0/0
                date1 = re.findall('\d+/\d+/\d+.*\d:\d+...|\d+/\d+/\d+', line)
                #date2 = re.findall('', line)
                if len(date1) > 0:
                        dates.append(listString(date1))
        return(dates)


def findDates(listOfLines):
        if len(listOfLines) <= 0:
                return 'No Dates Found'
        for line in listOfLines:
                return datefinder.find_dates(line)
