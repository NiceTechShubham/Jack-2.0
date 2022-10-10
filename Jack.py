import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import time
import os
import wolframalpha
import vlc
import pyfirmata

#board=pyfirmata.ArduinoNano("INSERT_COM_PORT")
#board.digital[2].mode=pyfirmata.OUTPUT

def query(ask):
    app_id="YOUR_WOLFRAMALPHA_APP_ID"
    client=wolframalpha.Client(app_id)
    r= client.query(ask)
    try:
        a=next(r.results).text
        if "|" in a:
            a=a.replace("|",".")
    except:
        a=wikipedia.summary(ask, sentences=4)
    return a

def speak(audio):
    tts= pyttsx3.init("sapi5")
    sounds=tts.getProperty("voices")
    tts.setProperty("voice",sounds[1].id)
    tts.setProperty("rate",125)
    tts.say(audio)
    tts.runAndWait()

def command():
    s=sr.Recognizer()
    with sr.Microphone() as mic:
        # board.digital[3].write(1)
        print("Listening...")
        s.pause_threshold=1
        audio=s.listen(mic,0,4)
    try:
        # board.digital[3].write(0)
        print("Recognizing...")
        query= s.recognize_google(audio,language="en-in")
        print("Your command is: ",query)
    except Exception as e:
        return "empty"
    return query

def greet():
    hr=datetime.datetime.now().hour
    if hr>=0 and hr<12:
        speak("Good Morning Sir")
    elif hr>=12 and hr<17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir")
        
speak("Hello")
greet()
speak("i am jack 2 point o")
speak("what can i call you sir ?")
user=command().lower()
if user=="shubham":
    speak("Welcome sir. as your name is shubham, so i think you are my creator. Am i right sir ?")
    m= command().lower()
    if m=="yes" or m=="yeah" or m== "ya":
        speak("Tell me something which is confidential in between us.")
        m= command().lower()
        for i in range(4):
            if m=="sparrow":
                speak("Welcome my godfather")
                speak("jack two point o in your service sir. Say how can i help you")
                break 
            else:
                speak("wrong password, please say again")
    else:
        speak("So you are not my creator.")
else:
    speak("Welcome"+ user)    
    
while True: 
    
    t=command().lower()
    if t=="stop":
        p.stop()
    if t=="jack" or t=="hey jack":
        speak("yes sir.")
        q=command().lower()
        if q== "how are you" or q=="are you fine" :
            speak("i am fine sir. How are you ?")
            m=command().lower()
            if m=="fine" or m=="i am also fine" or m== "i am fine":
                speak("i am very happy to hear that, you are fine.")
            else:
                speak("Oookay")
        elif q=="empty":
            speak("i did not hear anything")
        elif q=="hello" or q=="hi" or q=="hello jack" or q=="hi jack":
            speak("hello sir")
        elif q=="where are you from" or q== "where you live":
            speak("i am from Dhoba, Ramgarh")
        elif q=="who create you" or q=="who created you" or q=="who made you" or q=="who is your creator":
            speak("Mister Shubham Kumar is my creator")
        elif q=="tell me your specification" or q=="tell me your configuration" or q=="what is your configuration" or q=="what is your specifications":
            speak("i am jack two poin o, my random operating memory is one tera byte, proccessor is ryzen 5 2500u, Random access memory eight gb and my host is lenovo ideapad 330 and i am created by mister Shuhbham Kunar.")
        elif  q=="play some music" or q=="play a music" or q=="play music" or q=="play your favourite music" or q=="your favourite music":
            p=vlc.MediaPlayer("C:\\Users\\Shubham\\Desktop\\Jack 2.0\\Files\\despacito.mp3")
            p.play()
        elif  q=="relax music" or q=="play some relaxing music" or q=="play some relax music" or q=="play a relax music" or q=="play my music" or q=="play my favourite music" or q=="play relax music" or q=="play a relaxing music":
            p=vlc.MediaPlayer("C:\\Users\\Shubham\\Desktop\\Jack 2.0\\Files\\relax.mp3")
            p.play()
        elif  q=="play some evergreen music" or q=="play a old music" or q=="play evergreen music" or q=="play classic music":
            p=vlc.MediaPlayer("C:\\Users\\Shubham\\Desktop\\Jack 2.0\\Files\\evergreen.mp3")
            p.play()
        elif "turn on" in q or "on the light" in q:
            speak("turning on")
            # board.digital[2].write(1)
        elif "turn off" in q or "off the light" in q:
            speak("turning off")
            # board.digital[2].write(0)
        elif q=="who are you" or q=="what is your name" or q=="your name":
            speak("I am jack 2 point o and i am created by mister shubham kumar.")
        elif q=="who i am" or q=="what is my name":
            speak("as i remember you told me that your name is")
            speak(user)
        elif q=="bye":
            speak("ok sir, now i am going to sleep. have a good day, bye")
            break
        else:
            w=query(q)
            print(w)
            speak(w)
    else:
        continue
