#RegEX patterns

def months_pattern():
    return('(?:(?:January|Jan)|(?:February|Feb)|(?:March|Mar)|(?:April|Apr)|(?:May)|(?:June|Jun)|(?:July|Jul)|(?:August|Aug)|(?:September|Sep|Sept)|(?:October|Oct)|(?:November|Nov)|(?:December|Dec))')

def common_words():
    #Forked from first20hours/google-10000-english
    words = []
    start = '(?:'
    end = ')'

    with open("20k.txt", "r") as file:
        while True:
            if word := file.readline().replace('\n', ''):
                words.append(word)
            else:
                break
    mid1 = '\s|[^(?:@|©)]\s'.join(words)

    return f"{start}{mid1}{end}"
