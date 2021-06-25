
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from webbrowser import Chrome
import os
import smtplib
import random




hour =int(datetime.datetime.now().hour)
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id).............
engine.setProperty('voice',voices[0].id)


#for speaking operation
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()


#use to wish user
def wishMe():
    
    if hour>=0 and hour<=12 :
        speak("Good morning")
    elif hour>=12 and hour<=18 :
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Hello There I am Jarvis your assistant  How may I help you") 


#This function take microphone input from user n written string as an output
def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try :
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')

        print(f"user say : {query}")
    except Exception as e:
        print(e)
        print("Say that again, please.....")
        speak("Say that again, please.....")
        return "none" 
    return query   

#Sending Email 
def sendEmail(to,content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_main@gmail.com','your_password')
    server.sendmail('shubhamvast26@gmail.com',to,content)
    server.close()


#Main 
if __name__ == "__main__":

    name=""

    print("JARVIS")

    wishMe()
    

    while True:
        #  Logic to execute task based on query
        userRequest = takeCommand().lower()

#searching something on wikipedia.............................        
        if "wikipedia" in userRequest :
            speak("Searching on wikipedia...")
            userRequest= userRequest.replace("wikipedia","")
            result=wikipedia.summary(userRequest,sentences=2)
            print(result)
            speak(result)
#opening popular websites.......................................
        elif "open youtube" in userRequest :
            speak("opening youtube...")
            webbrowser.open("youtube.com")
        elif "open google map" in userRequest or "open map" in userRequest :
            speak("opening google map...")
            webbrowser.open("https://www.google.com/maps")    
        elif "open google" in userRequest :
            speak("opening google.....")
            webbrowser.open("google.com")
        elif "open stackoverflow" in userRequest :
            speak("opening stackoverflow.......")
            webbrowser.open("stackoverflow.com")
        elif "open gmail" in userRequest:
            speak("opening gmail.........")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
#playing music...................................................   
        elif "play music" in userRequest :
            
            music_dir = "C:\\Users\\ADMIN\\Downloads\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            speak("playing music....")
            os.startfile(os.path.join(music_dir,songs[0])) 
#tell date and time......................................................
        elif "time"in userRequest :
                currentTime= datetime.datetime.now().strftime("%H:%M:%S")
                print(currentTime)
                speak(f"The time is {currentTime}")
#sending emails.............................
        elif " email to" in userRequest :
             
            try :
                speak("Whom I send email ?")
                address = takeCommand()
                speak("what should i say")
                content = takeCommand()
                to =   address + "@gmail.com"
                sendEmail(to,content)
                speak("Email has been send succesfully ")
            except Exception as  e:
                print(e)
                speak("sorry my friend shubham , I am not able to send this eamil")

        elif "open chrome" in userRequest :
            speak("opening chrome ")
            codePath= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
#Quit program...................................

        elif "quit" in userRequest or "stop now" in userRequest :
            speak("Thanks for taking my helf")
            speak("have a great time  ! bye!")
            break

#for identity of assistant......................

        elif "who are you" in userRequest :
            speak("I am your virtual assistant jarvis how may I help you")

#for what it is..........................

        elif "what can you do " in userRequest:
            speak("I can open your software or app in your pc ")
            speak("can open gmail , youtube, stackoverflow")
            speak("Search something on wikipedia")
            speak("And many more as I can")

#opening file...........................

        elif "open file" in userRequest :
            speak("opening file") 
            codePath="C:\\Users\\ADMIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\File Explorer.exe"
            os.startfile(codePath)  
#Wishing .................................
        elif ("good" in userRequest) and (("morning" in userRequest) or ("afternoon" in userRequest) or ("evening" in userRequest) or ("night" in userRequest)) :
                if hour>=0 and hour<=12 :
                    speak("Good morning have good day")
                elif hour>=12 and hour<=18 :
                    speak("Good Afternoon ")
                     
                else:
                    speak("Good evening")
 #opening programs......................
       
        elif "open android studio" in userRequest :
            modifyRequest=userRequest.replace("open","")
            speak(f"opening {modifyRequest}")    
            codePath="D:\\Android Studio\\bin\\studio64.exe" 
            os.startfile(codePath)   

        elif "visual studio" in userRequest :
            modify_reqst = userRequest.replace("open","")
            speak(f"opening  {modify_reqst}")
            os.startfile("C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            continue

        elif "what's up " in userRequest :
            speak("Alright   thanks for asking")

        elif"i am fine "in userRequest:
            speak("nice to hear that")
        
        elif "how are you" in userRequest:
            speak("i am fine thank you   ")
         
#for user name................................  
        

        elif "my name" in userRequest:
             if name=="":
                    speak("Sorry  but i dont know what's your name")
                    speak("what should i call you ?")
                    name=takeCommand().lower()
                    speak(f"Do you like to call{name}")
                    nm_chkr=takeCommand().lower()
                    if "yes" in nm_chkr :
                        speak(f"hello  {name}")
                        continue
                    else:
                        speak("ok ")
             else:
                 speak(f"you are {name}")

        elif "shut up" in userRequest :
            speak("Sorry ")

#Anything is not here........................................
        else :
            search_Rqst=userRequest
            speak("Do you like to search it on internet")
            userRequest=takeCommand().lower()
            if "yes" in userRequest :
                webbrowser.open(f"{search_Rqst}")
            else:
                continue




