import speech_recognition as sr
from google_trans_new import google_translator 
from gtts import gTTS
import os

def translate_and_speak(text, src, dest):
    translator = google_translator()
    translation = translator.translate(text, lang_tgt='fr')
    print(translation.text)
    # tts = gTTS(translation.text, lang=dest)
    # tts.save('translation.mp3')
    # os.system("mpg321 translation.mp3")

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)

text = r.recognize_google(audio, show_all=False)
translate_and_speak(text, 'en', 'fr')