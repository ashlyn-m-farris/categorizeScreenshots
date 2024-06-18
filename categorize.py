def categorize(dates, h_m, authors):  # sourcery skip: assign-if-exp
    #No author no dates
    if len(authors) == 0 and (len(dates) + len(h_m) == 0):
        return("P1A1")

    elif len(authors) == 0 and (len(dates) + len(h_m) == 1):
        return('P1A1')

    #No authors at least 1 date
    elif len(authors) == 0 and (len(dates) + len(h_m)) > 1:
        return('PNA1')

    #No dates at least 1 author
    elif (len(dates) + len(h_m)) == 0 and len(authors) > 1:
        return 'PNAN'
    
    #At least 1 author AND at least 1 date
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