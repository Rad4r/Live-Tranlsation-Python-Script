import pygame
import pygame_gui


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
    (380, 300), (150, 50)), text='Translation')

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
                print('Dutch Translation')
                dutch_button.disable()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
