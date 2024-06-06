#Find possible authors and add them to a list
import re
from conversions import *

def findAuthors(text):
    handleLines = re.findall('.*@\w{4,15}.*', text)
    possibleAuthors = []

    for author in handleLines:
        if not re.findall('Replying', author):
            found = re.findall('@\w{4,15}', author)
            x = listString(found)
            possibleAuthors.append(x)    
    return(possibleAuthors)
