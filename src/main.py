import speech_recognition as sr
import pyttsx3
from googletrans import Translator

r = sr.Recognizer()
translator = Translator()

def speak(text, lang="en"):
    engine = pyttsx3.init()

    # Voice config
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Saying text in configured voice
    engine.say(text)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)

            my_text = r.recognize_google_cloud(audio)
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
