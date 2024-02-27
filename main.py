import speech_recognition as sr
from gtts import gtts
from playsound import playsound
from pygame import mixer
from io import BytesIO
import os
import openai

openai.api_key=''
messages_array = [
    {'role': 'system', 'content': 'You are my friend, Thomas'}
]

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, 'en-in')
        print(f'user has said {query}')
        messages_array.append({'role': 'user', 'content': query})
        respond(audio)
    except: