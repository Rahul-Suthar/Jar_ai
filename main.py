import speech_recognition as sr
import webbrowser
import pyttsx3
import daily
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("API_URL")
genapi = os.getenv("GenAPI_KEY")

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(cmmd):
    genai.configure(api_key=genapi)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(cmmd)

    return response.text

def processCmd(c):
    cm = c.lower()
    if cm.startswith("open"):
        tab = cm.split(' ')[1]
        if tab in daily.Tabs:
            link = daily.Tabs[tab]
            webbrowser.open(link)
            speak(f'opening {tab}')
        else:
            speak("Unable to find {tab}")
    elif cm.startswith("play"):
        song = cm.split(' ')[1]
        if song in daily.Songs:
            link =  daily.Songs[song]
            webbrowser.open(link)
            speak(f'playing {song}')
        else:
            speak("Unable to find {song}")
    elif cm.startswith("do"):
        solve = cm.split(' ')[1]
        if solve in daily.Solves:
            link = daily.Solves[solve]
            webbrowser.open(link)
            speak(f'Solving {solve}')
        else:
            speak(f"cann't open {solve}")
    elif 'news' in cm:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for art in articles:
                print(art['title'])
                # speak(art['title'])
    else:
        # let openai handle the request
        output = aiProcess(cm)
        print(output)
        # speak(output)

def start():
    speak("Welcome to Workplace")
    while True:
        try:
            with sr.Microphone() as source:
                print("listening......")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            print("recognizing.......")
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if 'jar' == word.lower():
                speak("yes sir")
                with sr.Microphone() as source:
                    print("Jarvis Activated.")
                    audio = r.listen(source)
                    cmd = r.recognize_google(audio)

                    processCmd(cmd)
            
        except Exception as e:
            print(f"Error , {e}")

if __name__ == "__main__":
    start()
