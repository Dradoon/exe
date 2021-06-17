import wikipedia

def wiki_ln(Q):
    #wiki search language change
    if ":wiki ln hindi" in Q:
        ln="hi"
        return("Wiki summary will be in hindi\n")
    elif ":wiki ln en" in Q:
        ln="en"
        return("Wiki summary will be in english\n")
    else:return("Invalid command did you use :wiki ln")

def wiki(Q,ln):
    # checking if page exist
    try:
        wikipedia.set_lang(ln)
        answer=wikipedia.summary(Q)
        return(answer)
    except Exception as e:
        return("Check your internet connection or use keywords only.")

