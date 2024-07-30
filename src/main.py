import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import pygame

r = sr.Recognizer()
translator = Translator()

def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(fp, 'mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")
            audio = r.listen(source)

            my_text = r.recognize_google(audio)
            my_text = my_text.lower()

            translated_text = translator.translate(my_text, dest='hi').text

            print("Did you say:", my_text)
            print("Translated:", translated_text)

            # Speak the translated text
            speak(translated_text, 'hi')
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
