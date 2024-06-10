#RegEX patterns

def months_pattern():
    return('(?:(?:January|Jan)|(?:February|Feb)|(?:March|Mar)|(?:April|Apr)|(?:May)|(?:June|Jun)|(?:July|Jul)|(?:August|Aug)|(?:September|Sep|Sept)|(?:October|Oct)|(?:November|Nov)|(?:December|Dec))')

def common_words():
    #Forked from first20hours/google-10000-english
    words = []
    start = '(?:'
    end = ')'

    file = open("20k.txt", "r")
    while True:
        word=file.readline().replace('\n', '')
        if not word:
            break
        words.append(word)
    file.close()
    mid1 = '\s|[^(?:@|©)]\s'.join(words)
    
    return("{}{}{}".format(start, mid1, end))
