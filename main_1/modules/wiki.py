import wikipedia


def wiki(Q,ln):
    wikipedia.set_lang(ln)
    answer=wikipedia.summary(Q)
    return(answer)
