import speech_recognition as sr
import webbrowser
import pyttsx3
import json
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("API_URL")
genapi = os.getenv("GenAPI_KEY")

r = sr.Recognizer()
engine = pyttsx3.init()

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)
    
Tabs = load_data('tabs.json')
Songs = load_data('songs.json')
Solves = load_data('solves.json')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(cmmd):
    genai.configure(api_key=genapi)
    model = genai.GenerativeModel("gemini-1.5-flash")
    try :
        response = model.generate_content(cmmd)
        return response.text
    except Exception as e:
        return f'Error from AI: {e}'

def processCmd(c):
    cm = c.lower()
    if cm.startswith("open"):
        tab = cm.split(' ')[1]
        if tab in Tabs:
            link = Tabs[tab]
            webbrowser.open(link)
            speak(f'opening {tab}')
        else:
            speak(f"Unable to find {tab}")
    elif cm.startswith("play"):
        song = cm.split(' ')[1]
        if song in Songs:
            link = Songs[song]
            webbrowser.open(link)
            speak(f'playing {song}')
        else:
            speak(f"Unable to find {song}")
    elif cm.startswith("do"):
        solve = cm.split(' ')[1]
        if solve in Solves:
            link = Solves[solve]
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
                audio = r.listen(source, timeout=3, phrase_time_limit=4)
            print("recognizing.......")
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            if 'jar' == word.lower():
                speak("yes sir")
                with sr.Microphone() as source:
                    print("Jarvis Activated.")
                    audio = r.listen(source)
                    cmd = r.recognize_google(audio)
                    
                    if cmd.lower() in ['exit', 'stop', 'quit', 'packup']:
                        speak('Shutting down. Goodbye!')
                        break

                    processCmd(cmd)
            
        except Exception as e:
            print(f"Error occured : {e}")

if __name__ == "__main__":
    start()
