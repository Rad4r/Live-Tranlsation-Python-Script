from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import time
import os
import tkinter as tk
from functools import partial
from threading import Timer


def TranslateVoice(to_lang='en'):

    currentvoiceNumber = 0

    while True:
        # Capture Voice
        # takes command through microphone
        currentvoiceNumber = currentvoiceNumber + 1

        def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening.....")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing.....")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said {query}\n")
            except Exception as e:
                print("say that again please.....")
                return "None"
            return query

        # Taking voice input from the user
        query = takecommand()
        while (query == "None"):
            query = takecommand()

        # invoking Translator
        translator = Translator()

        # Translating from src to dest
        text_to_translate = translator.translate(query, dest=to_lang)
        text = text_to_translate.text

        speak = gTTS(text=text, lang=to_lang, slow=False)

        # Using save() method to save the translated
        # speech in capture_voice.mp3
        filename = 'captured_voice' + str(currentvoiceNumber) + '.mp3'
        speak.save(filename)

        audio_file = os.path.dirname(__file__) + "\\" + filename

        # Using OS module to run the translated voice.
        playsound(audio_file)
        # os.remove(filename)
        time.sleep(1)


def DisableAllButtons():
    DutchButton["state"] = "disable"
    GermanButton["state"] = "disable"
    ChineseButton["state"] = "disable"
    FrenchButton["state"] = "disable"


def SetNewLang(name, code):
    label.config(text="Language set to " + name)
    DisableAllButtons()
    t = Timer(.1, partial(TranslateVoice, code))
    t.start()
    # TranslateVoice(to_lang = code)


root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()

title = tk.Label(root, text="Choose the language you want to translate to \n")
title.pack(pady=10)

# Optimize a little more
DutchButton = tk.Button(
    root, text="Dutch", command=partial(SetNewLang, "Dutch", "nl"))
GermanButton = tk.Button(
    root, text="German", command=partial(SetNewLang, "German", "de"))
ChineseButton = tk.Button(root, text="Chinese",
                          command=partial(SetNewLang, "Chinese", "zh-cn"))
FrenchButton = tk.Button(
    root, text="French", command=partial(SetNewLang, "French", "fr"))
DutchButton.pack(pady=10)
GermanButton.pack(pady=10)
ChineseButton.pack(pady=10)
FrenchButton.pack(pady=10)

label = tk.Label(root)
label.pack(pady=10)

root.mainloop()

# Need to reset the voices when a different button is pressed
# Clear everythiing to be able to chose a differnet button
