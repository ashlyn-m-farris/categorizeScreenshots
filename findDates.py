import datefinder
from OCR import *
from conversions import *
import re

def formatDates(text):
        dates = []
        for line in re.split('\n', text):
                date = re.findall('\d+/\d+/\d+|\d+/\d+/\d+|\d+-\d+-\d+', line)
                time = re.findall('\d+:\d+', line)
                am_pm = re.findall('AM|PM', line)
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

def findDates(listOfLines):
        if len(listOfLines) <= 0:
                return 'No Dates Found'
        result = []
        for line in listOfLines:
                dates = datefinder.find_dates(line)
                for date in dates:
                        result.append(date)
                        
        return(result)