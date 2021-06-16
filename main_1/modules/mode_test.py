def mode_test(Q):
    #gui+speech
    if ":mode sg" in Q or ":mode gs" in Q:
        gui=True
        speech=True
        txt=False
        read=("mode set to gui and speech")
        return gui,speech,txt,read
    #yet to be added




    # speech+text 1
    
    elif ":mode st" in Q or ":mode ts" in Q:
        speech=True
        txt=True
        gui=False
        read=("mode set to speech and text(online)\n")
        return gui,speech,txt,read
    



    #text only 2
             
    elif ":mode t" in Q:
        txt=True
        speech=False
        gui=False
        read=("\nmode set to text only(offline)")
        return gui,speech,txt,read
    

    #speech only 3

    elif ":mode s" in Q:
        txt=False
        speech=True
        gui=False
        read=("\nmode set to speech only(online)")
        return gui,speech,txt,read
