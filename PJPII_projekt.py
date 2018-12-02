import pygame
import time
pygame.init() #inicjalizuje pygame

#SZEROKOSC I DLUGOSC OKNA
screen_width=800
screen_height=600

#kolory które beda uzyte, podane w RGB
black= (0,0,0)
white= (255,255,255)
violet= (162, 72, 225)

gameDisplay =pygame.display.set_mode((screen_width,screen_height)) #INICJALIZUJE OKNO
pygame.display.set_caption("KOSMICZNY ATAK") # NADAJE TYTUŁ
rocketImg= pygame.image.load('rocket.gif') # WCZYTUJE OBRAZ POSTACI GRACZA
score=0 # POCZATKOWY WYNIK
cosmosImg=pygame.image.load("cosmos.jpg") # WCZYTUJE OBRAZ TŁA
logoImg=pygame.image.load("logo.png")
infoImg=pygame.image.load("info.jpg")

def text_objects(text, font): # FUNKCJA DEKLARUJACA NAPISY
    text_surface =font.render(text, True, white)   # font.render -> rysuje text na surface render(text, antialias, color)
    return text_surface, text_surface.get_rect() # zwraca textSurface i rysuje prostokat

def game_intro():   # INTRO GRY
    intro= True
    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse= pygame.mouse.get_pos()
        gameDisplay.blit(cosmosImg, (0,0))
        klik= pygame.mouse.get_pressed()

        #OBSLUGA PRZYCISKU START
        if 140+500>mouse[0]> 140 and 150+100>mouse[1]>150:
            pygame.draw.rect(gameDisplay, violet, (140, 150, 500, 100)) #szerokosc na ekranie, wys. na ekranie , szerokosc i wysokosc
            if klik[0]==1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, black, (140, 150, 500, 100))

        #OBSLUGA PRZYCISKU INFO
        if 140+500>mouse[0]> 140 and 300+100>mouse[1]>300:
            pygame.draw.rect(gameDisplay, violet, (140, 300, 500, 100))
            if klik[0]==1:
                info_loop()
        else:
            pygame.draw.rect(gameDisplay, black, (140, 300, 500, 100))

        #OBSLUGA PRZYCISKU EXIT
        if 140+500>mouse[0]> 140 and 450+100>mouse[1]>450:
            pygame.draw.rect(gameDisplay, violet, (140, 450, 500, 100))
            if klik[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, black, (140, 450, 500, 100))

        #TEKST JAKI BEDZIE WYSWIETLONY NA PRZYCISKU START
        button_text = pygame.font.SysFont('Courier', 60)
        textSurf, textRect = text_objects("START", button_text)
        textRect.center = ((140 + (500 / 2)), 150 + (100 / 2))
        gameDisplay.blit(textSurf, textRect)

        # TEKST WYSWIETLONY NA PRZYCISKU INFO
        button2_text = pygame.font.SysFont('Courier', 60)
        textSurf, textRect = text_objects("INFO", button_text)
        textRect.center = ((140 + (500 / 2)), 300 + (100 / 2))
        gameDisplay.blit(textSurf, textRect)

        # TEKST WYSWIETLONY NA PRZYCISKU EXIT
        button_text = pygame.font.SysFont('Courier', 60)
        textSurf, textRect = text_objects("EXIT", button_text)
        textRect.center = ((140 + (500 / 2)), 450 + (100 / 2))
        gameDisplay.blit(textSurf, textRect)

        #WYSWIETLAM LOGO GRY
        gameDisplay.blit(logoImg, (150, screen_height * 0.1))
        pygame.display.update()

#FUNKCJA DO PĘTLI INFO
def info_loop():
    info=True
    while(info):
        gameDisplay.blit(infoImg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():  # EVERY EVENT WHICH HAPPENS- KLIKNIECIE MYSZKA , KLAWISZ ITP.
            if event.type == pygame.QUIT:  # PO WCISNIECIU W OKNIE X
                pygame.quit()               #WYJSCIE Z GRY
                quit()
            if event.type == pygame.KEYDOWN: # JESLI PRZYCISK JEST WCISNIETY
                if event.key == pygame.K_ESCAPE: #PO WCISNIECIU ESC - POWRÓT DO MENU GLOWNEGO
                    game_intro()

#FUNKCJA PETLI GRY
def game_loop():
    game=True
    while(game):
        gameDisplay.blit(cosmosImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():  # EVERY EVENT WHICH HAPPENS- KLIKNIECIE MYSZKA , KLAWISZ ITP.
            if event.type == pygame.QUIT:  # PO WCISNIECIU W OKNIE X
                pygame.quit()               #WYJSCIE Z GRY
                quit()
            if event.type == pygame.KEYDOWN: # JESLI PRZYCISK JEST WCISNIETY
                if event.key == pygame.K_ESCAPE: #PO WCISNIECIU ESC - POWRÓT DO MENU GLOWNEGO
                    game_intro()

game_intro()
pygame.quit()
quit()
