from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import time
import os
import pygame
import pygame_gui
from functools import partial
import threading
# from threading import Timer


def TranslateVoice(to_lang='en'):

    currentvoiceNumber = 0
    # Mayeb do something other than while loop?

    # while True:
    #     # Capture Voice
    #     # takes command through microphone
    #     currentvoiceNumber = currentvoiceNumber + 1

    #     def takecommand():
    #         r = sr.Recognizer()
    #         with sr.Microphone() as source:
    #             print("listening.....")
    #             r.pause_threshold = 1
    #             audio = r.listen(source)

    #         try:
    #             print("Recognizing.....")
    #             query = r.recognize_google(audio, language='en-in')
    #             print(f"user said {query}\n")
    #         except Exception as e:
    #             print("say that again please.....")
    #             return "None"
    #         return query

    #     # Taking voice input from the user
    #     query = takecommand()
    #     while (query == "None"):
    #         query = takecommand()

    #     # invoking Translator
    #     translator = Translator()

    #     # Translating from src to dest
    #     text_to_translate = translator.translate(query, dest=to_lang)
    #     text = text_to_translate.text

    #     speak = gTTS(text=text, lang=to_lang, slow=False)

    #     # Using save() method to save the translated
    #     # speech in capture_voice.mp3
    #     filename = 'captured_voice' + str(currentvoiceNumber) + '.mp3'
    #     speak.save(filename)

    #     audio_file = os.path.dirname(__file__) + "\\" + filename

    #     # Using OS module to run the translated voice.
    #     playsound(audio_file)
    #     # os.remove(filename)
    #     time.sleep(1)


def SetNewLang(name, code):
    print("language set to " + name + " with code " + code)
    chosenLanguageLabel.text = 'Chosen Languange: ' + name  # not working?
    # t = Timer(.1, partial(TranslateVoice, code))
    # t.start()
    # TranslateVoice(to_lang = code)


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600), 'theme.json')
# push to talk

chosenLanguageLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (300, 0), (200, 50)), text='Chosen Language: English')
translationText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (150, 50), (500, 50)), text='Choose a laguage you want to translate to')

dutch_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (150, 100), (100, 50)), text='Dutch', manager=manager)
danish_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (250, 100), (100, 50)), text='Danish', manager=manager)
spanish_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (350, 100), (100, 50)), text='Spanish', manager=manager)
greek_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (450, 100), (100, 50)), text='Greek', manager=manager)
japanese_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (550, 100), (100, 50)), text='Japanese', manager=manager)
german_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (150, 150), (100, 50)), text='German', manager=manager)
bulgarian_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (250, 150), (100, 50)), text='Bulgarian', manager=manager)
italian_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (350, 150), (100, 50)), text='Italian', manager=manager)
korean_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (450, 150), (100, 50)), text='Korean', manager=manager)
russian_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (550, 150), (100, 50)), text='Russian', manager=manager)
french_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (150, 200), (100, 50)), text='French', manager=manager)
croatian_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (250, 200), (100, 50)), text='Croatian', manager=manager)
romanian_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (350, 200), (100, 50)), text='Romanian', manager=manager)
chinese_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (450, 200), (100, 50)), text='Chinese', manager=manager)
polish_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (550, 200), (100, 50)), text='Polish', manager=manager)


listeningText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (150, 250), (500, 50)), text='Listening...')


speechLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (0, 300), (150, 50)), text='What you said:')
translatedLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (380, 300), (150, 50)), text='Translation:')

transcribeText = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
    (0, 350), (400, 250)), html_text='What you said', manager=manager)
translationText = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
    (400, 350), (400, 250)), html_text='Translation', manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == dutch_button:
                SetNewLang("Dutch", 'nl')
                # threading.Thread(target=SetNewLang, args=("Dutch", 'nl'), daemon=True).start()
            if event.ui_element == danish_button:
                SetNewLang("Danish", 'da')
            if event.ui_element == spanish_button:
                SetNewLang("Spanish", 'es')
            if event.ui_element == greek_button:
                SetNewLang("Greek", 'el')
            if event.ui_element == japanese_button:
                SetNewLang("Japanese", 'ja')
            if event.ui_element == german_button:
                SetNewLang("German", 'de')
            if event.ui_element == bulgarian_button:
                SetNewLang("Bulgarian", 'bg')
            if event.ui_element == italian_button:
                SetNewLang("Italian", 'it')
            if event.ui_element == korean_button:
                SetNewLang("Korean", 'ko')
            if event.ui_element == russian_button:
                SetNewLang("Russian", 'ru')
            if event.ui_element == french_button:
                SetNewLang("French", 'fr')
            if event.ui_element == croatian_button:
                SetNewLang("Croatian", 'hr')
            if event.ui_element == romanian_button:
                SetNewLang("Romanian", 'ro')
            if event.ui_element == chinese_button:
                SetNewLang("Chinese (simplified)", 'zh-cn')
            if event.ui_element == polish_button:
                SetNewLang("Polish", 'pl')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
