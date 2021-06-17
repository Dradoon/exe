# Python program to translate
# speech to text and text to speech
  
import modules.narrator as narrator
import speech_recognition as sr



def hear_this(speech,voice,txt):
    
    # Initialize the recognizer 
    r = sr.Recognizer()

    # Exception handling to handle
        # exceptions at the runtime
    while True:
        try:
                  
                # use the microphone as source for input.
                with sr.Microphone() as source:
                      
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level 

                    narrator.speak("I am hearing",voice)
                    
                    #listens for the user's input 
                    audio = r.listen(source)
                    print("i am here")
                    # Using ggogle to recognize audio
                    MyText = r.recognize_google(audio)
                    MyText = MyText.lower()
                    read="Did you say "+MyText
                    
                    if txt:print(read)
                    if speech:narrator.speak(read,voice)

                    
                    #confirming if the question is right
                    audio =  r.listen(source)
                    print("i am here 2")
                    confirm = r.recognize_google(audio)
                    if "yes" in confirm.lower():
                        print("yes")
                        return MyText                
        except Exception as e:
                print(e)
              
           
        


              
        
