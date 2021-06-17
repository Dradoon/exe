import random
import pickle
import modules.narrator as narrator
import modules.hear as hear
    

#trying if QA exists if not create one
def path_test(path_QA):
    try:
        g=open(path_QA,"rb")
        g.close()
    except:
        g=open(path_QA,"wb")
        g.close()

## QaA defines the learning process

def QaA(Q,speech,txt,voice,hearing):


    #path of information
    
    path_QA="./imports/QA"


    #testing the path
    
    path_test(path_QA)

    

    #removing all puntuation marks so that users can casually use the program
    
    j=""
    for i in Q:
        if i.isalnum():
            j=j+i
        elif i.isspace():
            j=j+i
    Q=j



    #program starts
    
    g=open(path_QA,"rb")
    while True:
        # checking if question exits in file if yes then random answers in the the question dict{} are given
        
        try:
            answer=pickle.load(g)
            if answer[0]==Q:
                leng=len(answer)
                rand=random.randint(1,leng-1)
                return(answer[rand])
                g.close()
                break
            else:pass


        #if question not present and file reached its end exception arises
        #creating a new dict{} of question with answer asked to the user
        
        except Exception as e:
            g.close()
            rand=random.randint(1,6)
            print("\nShould I check on wikipedia\n")
            option=input("yes/no: ")
            if option.lower()=="yes":
                return "use_wiki"            
            if rand==1:read=("Oh! I don't know the answer for this could you tell me please.")
            elif rand==2:read=("Answer not present please would you give me a answer for this.")
            elif rand==3:read=("I don't know how the reply for this could you tell me.")
            elif rand==4:read=("Help me to reply this please.")
            elif rand==5:read=("This is a new statement for me could you tell me the answer.")
            print(read)
            if speech:narrator.speak(read,voice)
            new_Q=Q
            if hearing:new_A=hear.hear_this(speech,voice,txt)
            else:new_A=input()

            new=[new_Q,new_A]
            f=open(path_QA,"ab+")
            pickle.dump(new,f)
            rand=random.randint(0,3)
            if rand==1:read=("Noted! Thankyou.")
            elif rand==2:read=("Got it!")
            elif rand==3:read=("Now i know.")
            f.close()
            return read
            break
