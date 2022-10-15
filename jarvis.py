import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")
engine.setProperty('rate', 150)
engine.setProperty('voice',voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour<12:
        speak("Good Morning Sir Arkoprovo Datta")
    elif hour >=12 and hour<17:
        speak("Good Afternoon Sir Arkoprovo Datta")
    elif hour >=17 and hour < 21:
        speak("Good Evening Sir Arkoprovo Datta")
    else:
        speak("Good Night Sir Arkoprovo Datta")
    speak("I am Jarvis, tell me how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening youtube for you sir, here you go")
            webbrowser.open("youtube.com")
            speak("Anything else sir?")
        elif "open google" in query:
            speak("Opening google for you sir, here you go")
            webbrowser.open("google.com")
            speak("Anything else sir?")
        elif "open linkedin" in query:
            speak("Opening Linkedin for you sir, here you go")
            webbrowser.open("linkedin.com")
            speak("Anything else sir?")
        elif "open github" in query:
            speak("Opening Github for you sir, here you go")
            webbrowser.open("Github.com")
            speak("Anything else sir?")
        elif "open gmail" in query:
            speak("Opening gmail or google mail for you sir, here you go")
            webbrowser.open("gmail.com")
            speak("Anything else sir?")
        elif "open facebook" in query:
            speak("Opening facebook for you sir, here you go")
            webbrowser.open("facebook.com")
            speak("Anything else sir?")
        elif "open stack overflow" in query:
            speak("Opening stack overflow for you sir, here you go")
            webbrowser.open("stackoverflow.com")
            speak("Anything else sir?")
        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        elif "the date" in query:
            d = date.today()
            speak(f"Today's date is {d}")
