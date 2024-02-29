import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pygame import mixer
from io import BytesIO
import os
import openai

openai.api_key=''
messages_array = [
    {'role': 'system', 'content': 'You are my friend, Jessica'}
]

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user has said {query}')
        messages_array.append({'role': 'user', 'content': query})
        respond(audio)
    except Exception as e:
        print('Say that again please...', e)
        
def respond(audio):
    print('Responding...')
    res=openai.Completion.create(
        model = 'gpt-3.5-turbo',
        messages=messages_array
    )

    res_message = res.choices[0].message
    messages_array.append(res_message)

    speak(res_message.content)

def speak(text) :
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save('captured_voice.mp3')
    playsound('captured_voice.mp3')

    os.remove('captured_voice.mp3')
    listen()


query = listen()