from playsound import playsound
import speech_recognition as sr 
from googletrans import Translator 
from gtts import gTTS
import pyttsx3
import os

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

dic=('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 
     'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
 'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
     'bs', 'bulgarian', 'bg', 'catalan', 'ca',
  'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
     'zh-cn', 'chinese (traditional)', 'zh-tw',
  'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
     'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
  'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi', 
     'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
  'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati', 
     'gu', 'haitian creole', 'ht', 'hausa', 'ha', 
  'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong', 
     'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
  'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it', 
     'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
  'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
     'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
  'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
     'lb', 'macedonian', 'mk', 'malagasy',
  'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
     'mi', 'marathi', 'mr', 'mongolian', 'mn',
  'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
     'odia', 'or', 'pashto', 'ps', 'persian',
   'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
     'romanian', 'ro', 'russian', 'ru', 'samoan',
   'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 
     'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
   'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so', 
     'spanish', 'es', 'sundanese', 'su', 
  'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
     'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
  'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 
     'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
  'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')
  
engine = pyttsx3.init()
#Set Language first through input
langInput = input("Enter a new language to learn: " )

while (langInput.lower() not in dic):
    print("That language unfortunately does not exist!" )
    langInput = input("Enter a new language to learn: " )

to_lang = dic[dic.index(langInput.lower())+1]
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


    # Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the
    # speak = gTTS(text=text, lang=to_lang, slow=False)
    
    # # Using save() method to save the translated
    # # speech in capture_voice.mp3
    # filename = 'captured_voice' + str(currentvoiceNumber) + '.mp3'
    # speak.save(filename)
    
    # # Using OS module to run the translated voice.
    # playsound(filename)
    # os.remove(filename)

    # print(text)

    
    # engine = pyttsx3.init()
    for voice in engine.getProperty('voices'):
        print(voice)
    change_voice(engine, "nl_BE", "VoiceGenderFemale")
    engine.say(text)
    engine.runAndWait()