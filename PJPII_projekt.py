import pygame
import time

pygame.init() #inicjalizuje pygame

#SZEROKOSC I DLUGOSC OKNA
screen_width = 800
screen_height = 600

#kolory które beda uzyte, podane w RGB
black = (0, 0, 0)
white = (255, 255, 255)
violet = (162, 72, 225)

gameDisplay = pygame.display.set_mode((screen_width,screen_height)) #INICJALIZUJE OKNO
pygame.display.set_caption("KOSMICZNY ATAK") # NADAJE TYTUŁ
rocketImg= pygame.image.load('rocket.gif') # WCZYTUJE OBRAZ POSTACI GRACZA
score = 0   # POCZATKOWY WYNIK
life = 3    #POCZTAKOWA LICZBA ZYC
level_number = 1    #POCZATKOWY LEVEL

#WCZYTYWANIE OBRAZOW
cosmosImg = pygame.image.load("cosmos.jpg")
logoImg = pygame.image.load("logo.png")
infoImg = pygame.image.load("info.jpg")
strzalImg = pygame.image.load("strzal.jpg")

#RUCH RAKIETA
def rocket (x,y):
    gameDisplay.blit(rocketImg, (x, y))

#LICZNIK PUNKTOW
def your_score(score):
    font = pygame.font.SysFont('Courier', 20)
    text = font.render("SCORE:"+str(score), True, white)
   # gameDisplay.blit(text, (20, 20))

#LICZNIK ZYC
def lives(life):
    font = pygame.font.SysFont('Courier', 15)
    text = font.render("LIVES:" + str(life), True, white)
   # gameDisplay.blit(text, (20, 560))

#LICZNIK POZIOMOW
def level_counter(level_number):
    font = pygame.font.SysFont('Courier', 20)
    text = font.render("LEVEL:" + str(level_number), True, violet)
    gameDisplay.blit(text, (690, 20))

#FUNKCJA DEKLARUJACA NAPISY
def text_objects(text , font):
    text_surface = font.render(text, True, white)   # font.render -> rysuje text na surface render(text, antialias, color)
    return text_surface, text_surface.get_rect() # zwraca textSurface i rysuje prostokat

# INTRO GRY
def game_menu():
    intro = True
    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse= pygame.mouse.get_pos()
        gameDisplay.blit(cosmosImg, (0, 0))
        klik = pygame.mouse.get_pressed()

        #OBSLUGA PRZYCISKU START
        if 140+500>mouse[0]> 140 and 150+100>mouse[1]>150:
            pygame.draw.rect(gameDisplay, violet, (140, 150, 500, 100)) #szerokosc na ekranie, wys. na ekranie , szerokosc i wysokosc
            if klik[0] == 1:
                time.sleep(1)
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, black, (140, 150, 500, 100))
        #OBSLUGA PRZYCISKU INFO
        if 140+500 > mouse[0] > 140 and 300+100 > mouse[1]>300:
            pygame.draw.rect(gameDisplay, violet, (140, 300, 500, 100))
            if klik[0] == 1:
                info_loop()
        else:
            pygame.draw.rect(gameDisplay, black, (140, 300, 500, 100))
        #OBSLUGA PRZYCISKU EXIT
        if 140+500 > mouse[0] > 140 and 450+100 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, violet, (140, 450, 500, 100))
            if klik[0] == 1:
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
        textSurf, textRect = text_objects("INFO", button_text)
        textRect.center = ((140 + (500 / 2)), 300 + (100 / 2))
        gameDisplay.blit(textSurf, textRect)

        # TEKST WYSWIETLONY NA PRZYCISKU EXIT
        textSurf, textRect = text_objects("EXIT", button_text)
        textRect.center = ((140 + (500 / 2)), 450 + (100 / 2))
        gameDisplay.blit(textSurf, textRect)

        #WYSWIETLAM LOGO GRY
        gameDisplay.blit(logoImg, (150, screen_height * 0.1))
        pygame.display.update()

#FUNKCJA DO PĘTLI INFO
def info_loop():
    info = True
    while(info):
        gameDisplay.blit(infoImg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():  # EVERY EVENT WHICH HAPPENS- KLIKNIECIE MYSZKA , KLAWISZ ITP.
            if event.type == pygame.QUIT:  # PO WCISNIECIU W OKNIE X
                pygame.quit()               #WYJSCIE Z GRY
                quit()
            if event.type == pygame.KEYDOWN: # JESLI PRZYCISK JEST WCISNIETY
                if event.key == pygame.K_ESCAPE: #PO WCISNIECIU ESC - POWRÓT DO MENU GLOWNEGO
                    game_menu()

#FUNKCJA PETLI GRY
def game_loop():
    game = True
    x = screen_width/2 - 40
    y = 500
    x_change = 0
    liczbastrzalow = 0
    bullet_speed = 14
    bullet_x = x + 20
    bullet_y = y - 50
    bulletstate = "ready"

    while(game):
        gameDisplay.blit(cosmosImg, (0, 0))
        your_score(score)
        lives(life)
        level_counter(level_number)
        rocket(x, y)

        for event in pygame.event.get():  # EVERY EVENT WHICH HAPPENS- KLIKNIECIE MYSZKA , KLAWISZ ITP.
            if event.type == pygame.QUIT:  # PO WCISNIECIU W OKNIE X
                pygame.quit()               #WYJSCIE Z GRY
                quit()
            if event.type == pygame.KEYDOWN: # JESLI PRZYCISK JEST WCISNIETY
                if event.key == pygame.K_ESCAPE: #PO WCISNIECIU ESC - POWRÓT DO MENU GLOWNEGO
                    game_menu()
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                if event.key == pygame.K_RIGHT:
                    x_change += 5
                if event.key == pygame.K_SPACE:
                    if bulletstate == "ready":
                        liczbastrzalow+=1
                        bullet_x = x+20
                        bullet_y = 500
                        bulletstate = "fire"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        if liczbastrzalow >= 1 and bulletstate == "fire":
            gameDisplay.blit(strzalImg, (bullet_x, bullet_y))
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bulletstate = "ready"
        x = x+x_change
        if x > screen_width-50:
            x = 747
        elif x < 0:
            x = 0
        rocket(x, y)
        pygame.display.update()

game_menu()
pygame.quit()
quit()
