import re
from conversions import *

def groupTriples(text, lines):
    text = text.replace('(\w', "").replace('\)', "").replace('[', "").replace(']', "").replace('\\', '').replace('|', '')
    listOfGroups = []
    i = 1
    while i < len(lines):
        group = re.split(lines[i], text, maxsplit=1)
        listOfGroups.append(group[0])
        text = text.replace(group[0], '')
        i += 1
    listOfGroups.append(text)
    return(listOfGroups)
            