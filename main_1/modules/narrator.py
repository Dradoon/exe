import pyttsx3

def set_voice(Q,voice):
    if ":narrator female" in Q:
        voice="female"
        print("Narrator voice set to female.\n")
    elif ":narrator male" in Q:
        voice="male"
        print("Narrator voice set to male.")
    return voice

def speak(tx,voice):
    #readying engine to speak
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice=="male":
        engine.setProperty('voice',voices[0].id)
    elif voice=="female":
        engine.setProperty('voice',voices[1].id)

    #set rate right

    rate = engine.getProperty('rate')   # getting details of current speaking rate

    engine.setProperty('rate', 125)
    
    engine.say(tx)
    
    engine.runAndWait()
    engine.stop()

