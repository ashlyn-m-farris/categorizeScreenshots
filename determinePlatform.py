import re

def determinePlatform(results):
    line_index = 0
    line_list = re.split('\n', results)
    while line_index < len(line_list):
            if re.findall("(?:\d\.\d*(?:k|M)|\d*) ReTruths", results):
                return("Truth Social")
            elif re.findall("(?:\d\.\d*(?:k|M)|\d*) Reposts", results):
                return("Twitter")
            else:
                return("unable to be determined")
            line_index += 1
        