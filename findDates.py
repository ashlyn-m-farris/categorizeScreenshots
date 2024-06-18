import datefinder
from OCR import *
from conversions import *
from RegExPatterns import *
import re


def formatDates(text):
        dates = []
        months = months_pattern()
        for line in re.split('\n', text):
                words = re.findall(common_words(), line)
                if not words:
                        #MM/DD/YY or M/D/Y or MM/DD/YYYY or with - or . or Month(Mon) DD, YYYY or Month DD
                        date = re.findall('\d+(?:/|-|.)\d+(?:/|-|.)\d+|' +months+ '(?: \d+, \d+)|' +months+ '(?: \d+)' , line)
                        #HH:MM
                        time = re.findall('\d+:\d+', line)
                        #AM or PM or am or pm
                        am_pm = re.findall('AM|PM|am|pm', line)

                        if len(date) > 0 and len(time) > 0 and len(am_pm) > 0:
                                dates.append(f'{listString(date)} {listString(time)} {listString(am_pm)}')
                        elif len(date) > 0 and len(time) > 0:
                                dates.append(f'{listString(date)} {listString(time)}')
                        elif len(time) > 0 and len(am_pm) > 0:
                                dates.append(f'{listString(time)} {listString(am_pm)}')
                        elif len(time) > 0:
                                dates.append(listString(time))
                        elif len(date) > 0:
                                dates.append(listString(date))
        return(dates)

def hmFormat(text):
        return re.findall('\d+(?:m|h|d)', text)

def findDates(listOfLines):
        # sourcery skip: for-append-to-extend, simplify-generator
        if len(listOfLines) <= 0:
                return []
        result = []
        for line in listOfLines:
                dates = datefinder.find_dates(line)
                for date in dates:
                        result.append(date)
                        
        return(result)