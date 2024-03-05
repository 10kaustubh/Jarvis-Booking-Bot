from email.mime import audio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
speak("I am Airline Bot Sir. Please tell me how may I help you")
speak("Do you want to book ticket or ")
speak("Do you want to cancel ticket or ")
speak("Do you want to exit")

def takeCommand():
#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
# print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
while True:
# if 1:
        query = takeCommand().lower()
# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'book ticket' in query:
        #   if'book ticket' in query:
            speak('Please tell your source and destination')
            query = takeCommand().lower()
#while True: # in query:
#def takeCommand():
            speak("tell the date ")
            query = takeCommand().lower()
            #break
# def takeCommand():
# print(audio)
# query = takeCommand().lower()
#while True:
            speak("enter number of seats for reservation")
            query = takeCommand().lower()
            #break
# print(audio)
# def takeCommand():
#while True:
            speak("we have recorded your date and transferring you to our website")
            webbrowser.open("https://www.makemytrip.com/")
            break
   # break
#elif 'cancel ticket' in query:
        elif'cancel ticket' in query:
            speak('Please tell your source and destination')
            query = takeCommand().lower()
#while True: # in query:
#def takeCommand():
            speak("tell the date ")
            query = takeCommand().lower()
        #break
# def takeCommand():
# print(audio)
# query = takeCommand().lower()
#while True:
            speak("enter number of seats for cancellation")
            query = takeCommand().lower()
        #break
# print(audio)
# def takeCommand():
#while True:
            speak("we have recorded your date and You can proceed for cancellation on your website ")
            webbrowser.open("https://www.makemytrip.com/")
            break
        # break
        elif 'exit'in query:
            break
            exit
    #break
# speak("Please tell your source and destination")
# webbrowser.open("makemytrip.com")
# elif 'open google' in query:
# webbrowser.open("google.com")
# elif 'open stackoverflow' in query:
# webbrowser.open("stackoverflow.com")
# elif 'play music' in query:
# music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
# songs = os.listdir(music_dir)
# print(songs)
# os.startfile(os.path.join(music_dir, songs[0]))
# elif 'the time' in query:
# strTime = datetime.datetime.now().strftime("%H:%M:%S")
# speak(f"Sir, the time is {strTime}")
#elif 'open code' in query:
# codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#os.startfile(codePath)
        elif 'email to kash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "thekaustubhm@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend kash bhai. I am not able to send this email")