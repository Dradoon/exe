from gtts import gTTS
import pyglet


def tx_speech(tx):
    #removing pun to make saving simple
    
    j=""
    for i in tx:
        if i.isalnum():
            j=j+i
        elif i.isspace():
            j=j+i
    tx=j
    
    ##playing if speech answer exist
    #PATH =audio folder
    try:
        saved=tx.replace(" ","_")
        
        path="./audio/"+saved+".mp3"
        
        music = pyglet.media.load(path, streaming=False)
        music.play()

    #saving when speech doesn't exist downloading

    except:
        
        saving=gTTS(text=tx,lang="en",slow=False)
        saving.save(path)
        tx_speech(tx)
