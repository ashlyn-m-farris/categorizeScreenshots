#Find possible authors and add them to a list
import re
from conversions import *
from RegExPatterns import *

def findAuthors(text):
    handleLines = re.findall('.*(?:@|©)\w{4,15}.*', text)
    possibleAuthors = []

    for author in handleLines:
        words = re.findall(common_words(), author)
        if not words:
            found = re.findall('(?:@|©)\w{4,15}', author)
            x = listString(found)
            possibleAuthors.append(x)    
    return(possibleAuthors)
