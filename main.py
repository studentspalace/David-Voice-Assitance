import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif(hour>=12 and hour<=18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am David! How can I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        r.energy_threshold=100
        audio = r.listen(source, timeout=1, phrase_time_limit=4)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print("User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.eclo()
    server.starttls()
    server.login("chitrankmishra010@gmail.com",'bittu0614')
    server.sendmail('chitrankmishra010@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open codeforces" in query:
            webbrowser.open("codeforces.com")
        
        elif "play music" in query:
            music_dir = ""
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is {strtime}")

        elif "open code" in query:
            codepath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email" in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to= "chitrankmishra@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, Can't send email")
        
        elif "quit" in query:
            exit()
        




