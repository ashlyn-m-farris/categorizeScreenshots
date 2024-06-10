def categorize(dates, h_m, authors):
    if len(dates) + len(h_m) > 1:
        post = 'PN'
    else:
        post = 'P1'

    same = []
    if authors.count(authors[0]) == len(authors):
        author = 'A1'
    else:
        author = 'AN'
    
    return(post + author)