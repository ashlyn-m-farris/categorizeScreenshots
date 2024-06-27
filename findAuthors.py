#Find possible authors and add them to a list
import re
from conversions import *
from RegExPatterns import *
import re

def findAuthors(text):
    possibleAuthors = []
    line_index = 0
    line_list = re.split('\n', text)
    while line_index < len(line_list):
        words = re.findall(common_words(), line_list[line_index])
        if not words and line_index >= 0 and not re.findall("(?:Replying|replying)", line_list[line_index - 1]) and not re.findall("(?<![^a-zA-Z])\.", line_list[line_index]) :
            found = re.findall(r'(?:@|©)\w{2,15}', line_list[line_index])
            if found:
                possibleAuthors.append(found[0])
        line_index += 1
    return possibleAuthors

def authorLines(text):
    lines = []
    line_index = 0
    line_list = re.split('\n', text)
    while line_index < len(line_list):
        handleLines = re.findall('.*(?:@|©)\w{2,15}.*', line_list[line_index])
        handle_index = 0
        while handle_index < len(handleLines):
            handleLine = handleLines[handle_index]
            words = re.findall(common_words(), handleLine)
            if not words and line_index >= 0 and not re.findall("(?:Replying|replying)", line_list[line_index - 1]):
                x = listString(handleLine)
                lines.append(x)
            handle_index += 1
        line_index += 1
    return(lines)
