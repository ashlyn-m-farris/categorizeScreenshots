def categorize(dates, h_m, authors):  # sourcery skip: assign-if-exp
    #No author no dates
    if len(authors) == 0 and (len(dates) + len(h_m) == 0):
        return("No author and timestamp info recieved.")

    #No authors at least 1 date
    elif len(authors) == 0 and (len(dates) + len(h_m)) > 0:
        print("There is no author information")
        if len(dates) + len(h_m) > 1:
            return('PN')
        else:
            return('P1')

    #No dates at least 1 author
    elif (len(dates) + len(h_m)) == 0 and len(authors) > 0:
        print('There is no date information')
        if len(authors) > 1:
            return 'AN'
        else:
            return 'A1'
    
    #At least 1 author and at least 1 date
    else:
        if len(dates) + len(h_m) > 1:
            post = 'PN'
        else:
            post = 'P1'

        if authors.count(authors[0]) == len(authors):
            author = 'A1'
        else:
            author = 'AN'

        return(post + author)