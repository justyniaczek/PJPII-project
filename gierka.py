import pygame
import sys
from random import shuffle
from pygame.locals import *
import pygame
import time
import math
import datetime

#CONSTANS

#COLORS IN RGB
black = (0, 0, 0)
white = (255, 255, 255)
violet = (162, 72, 225)

#naprawic potem
RED = (255, 0, 0)
GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
#YELLOW = (255, 255, 0)

#SZEROKOSC I DLUGOSC OKNA
DISPLAYWIDTH = 800
DISPLAYHEIGHT = 600
XMARGIN = 50
YMARGIN = 50

#POCZATKOWE WARTOSCI

start_life = 3    #POCZTAKOWA LICZBA ZYC
level_number = 1    #POCZATKOWY LEVEL
start_score = 0
extra_bullets_counter = 0


#PLAYER

PLAYERWIDTH = 40
PLAYERHEIGHT = 10
PLAYER1 = 'Player 1'
PLAYERSPEED = 5


#BULLETSTATES

BULLETWIDTH = 5
BULLETHEIGHT = 5
BULLETOFFSET = 800


# MOBS
MOB_WIDTH = 40
MOB_HEIGHT = 30
PREDKOSC_MOB = 10
ENEMYNAME = 'Enemy'
ENEMYGAP= 15
ARRAYWIDTH = 10
ARRAYHEIGHT = 6
MOVETIME = 600
MOVEX = 10
MOVEY = MOB_HEIGHT
TIMEOFFSET = 800

BOOST_SPEED = 1

#WCZYTYWANIE OBRAZOW
cosmosImg = pygame.image.load("cosmos.jpg")
logoImg = pygame.image.load("logo.png")
infoImg = pygame.image.load("info.jpg")
strzalImg = pygame.image.load("strzal.jpg")
obcy_1Img = pygame.image.load("enemy1_1.png")
obcy_2Img = pygame.image.load("enemy1_2.png")
obcy_3Img = pygame.image.load("enemy1_3.png")
rocketImg = pygame.image.load('rocket.gif')
boostImg = pygame.image.load("boost.jpg")


#POZWALA NA WIELOKROTNY INPUT
DIRECT_DICT = {pygame.K_LEFT: (-1),
               pygame.K_RIGHT: (1)}


#INICJALIZUJE PYGAME
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT)) #INICJALIZUJE OKNO


class Boost(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = BOOST_SPEED
    def update(self):
        self.rect.x += self.speedx

boosts = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = PLAYERWIDTH
        self.height = PLAYERHEIGHT
        #self.image = self.setImage()
        self.image = rocketImg
        self.image = pygame.Surface((self.width, self.height))
       # self.color = PLAYERCOLOR
        self.color = violet
        self.image.fill(self.color)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
       # self.rect = self.image.get_rect()
        self.name = PLAYER1
        self.speed = PLAYERSPEED
        self.vectorx = 0

    def update(self, keys, *args):
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key] * self.speed
        self.checkForSide()
        #self.image.fill(self.color)

    def checkForSide(self):
        if self.rect.right > DISPLAYWIDTH:
            self.rect.right = DISPLAYWIDTH
            self.vectorx = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vectorx = 0

class Blocker(pygame.sprite.Sprite):
    def __init__(self, side, color, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.width = side
        self.height = side
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.name = 'blocker'
        self.row = row
        self.column = column

class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect, color, vectory, speed):
        pygame.sprite.Sprite.__init__(self)
        self.width = BULLETWIDTH
        self.height = BULLETHEIGHT
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = rect.centerx
        self.rect.top = rect.bottom
        self.name = 'bullet'
        self.vectory = vectory
        self.speed = speed

    def update(self, *args):
        self.oldLocation = (self.rect.x, self.rect.y)
        self.rect.y += self.vectory * self.speed
        if self.rect.bottom < 0:
            self.kill()
        elif self.rect.bottom > 600:
            self.kill()

    def extraBullet(self, *args):
        self.oldLocation = (self.rect.x, self.rect.y)
        self.bulletdx = 1.7
        self.bulletdy = 1.1
        self.rect.y += self.bulletdy * self.speed
        self.rect.x += self.bulletdx * self.speed

    def extraBullet2(self, *args):
        self.oldLocation = (self.rect.x, self.rect.y)
        self.bulletdx = 1.7
        self.bulletdy = 1.1
        self.rect.y -= self.bulletdy * self.speed
        self.rect.x -= self.bulletdx * self.speed

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
        if 140+500 > mouse[0] > 140 and 150+100 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, violet, (140, 150, 500, 100)) #szerokosc na ekranie, wys. na ekranie , szerokosc i wysokosc
            if klik[0] == 1:
                time.sleep(1)
               # game_loop()
                app = App()
                app.mainLoop()
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
        gameDisplay.blit(logoImg, (150, DISPLAYHEIGHT * 0.1))
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

#LICZNIK PUNKTOW
def your_score(score):
    font = pygame.font.SysFont('Courier', 20)
    text = font.render("SCORE:"+str(score), True, white)
    gameDisplay.blit(text, (20, 20))

#LICZNIK LEVEL
def level_counter(level_number):
    font = pygame.font.SysFont('Courier', 20)
    text = font.render("LEVEL:" + str(level_number), True, violet)
    gameDisplay.blit(text, (690, 20))

#LICZNIK ZYC
def lives(life):
    font = pygame.font.SysFont('Courier', 15)
    text = font.render("LIVES:" + str(life), True, white)
    gameDisplay.blit(text, (20, 560))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.width = MOB_WIDTH
        self.height = MOB_HEIGHT
        self.row = row
        self.column = column
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.name = 'enemy'
        self.vectorx = 1
        self.moveNumber = 0
        self.moveTime = MOVETIME
        self.timeOffset = row * TIMEOFFSET
        self.timer = pygame.time.get_ticks() - self.timeOffset   # czas w milisekundach

    def update(self, keys, currentTime):
        if currentTime - self.timer > self.moveTime:
            if self.moveNumber < 10:
                self.rect.x += MOVEX * self.vectorx
                self.moveNumber += 1
            elif self.moveNumber >= 10:
                self.vectorx *= -1
                self.moveNumber = 0
                self.rect.y += MOVEY
                if self.moveTime > 100:
                    self.moveTime -= 50
            self.timer = currentTime

    def setImage(self):
        if self.row == 0:
            image = pygame.image.load('enemy1_3.png')
        elif self.row == 1:
            image = pygame.image.load('enemy1_2.png')
        elif self.row == 2:
            image = pygame.image.load('enemy1_1.png')
        else:
            image = pygame.image.load('enemy1_1.png')
        image.convert_alpha()
        image = pygame.transform.scale(image, (self.width, self.height))

        return image

class Text(object):
    def __init__(self, font, size, message, color, rect, surface):
        #self.font = pygame.font.Font(font, size)
        self.font = pygame.font.SysFont('Courier', 20)
        self.message = message
        self.surface = self.font.render(self.message, True, color)
        self.rect = self.surface.get_rect()
        self.setRect(rect)

    def setRect(self, rect):
        self.rect.centerx, self.rect.centery = rect.centerx, rect.centery - 5

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

class App(object):
    def __init__(self):
        pygame.init()
        self.displaySurf, self.displayRect = self.makeScreen()
        self.gameStart = True
        self.gameOver = False
        self.beginGame = False

    def makeScreen(self):
        pygame.display.set_caption("KOSMICZNY ATAK")
        displaySurf = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
        displayRect = displaySurf.get_rect()
        displaySurf.convert()

        return displaySurf, displayRect

    def resetGame(self):
        self.gameStart = True
        self.needToMakeEnemies = True

        self.introMessage1 = Text('Courier.ttf', 50,
                                 'Wcisnij przycisk aby rozpoczac',
                                white, self.displayRect,
                                self.displaySurf)
        self.gameOverMessage = Text('Courier.ttf', 100,
                                    'GAME OVER', white,
                                    self.displayRect, self.displaySurf)
        self.win = Text('Courier.ttf', 100,
                                    'Wygrana', white,
                                    self.displayRect, self.displaySurf)

        self.player = self.makePlayer()
        self.bullets = pygame.sprite.Group()
        self.greenBullets = pygame.sprite.Group()

        self.allSprites = pygame.sprite.Group(self.player)
        self.players = pygame.sprite.Group()

        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.enemyMoves = 0
        self.enemyBulletTimer = pygame.time.get_ticks()
        self.gameOver = False
        self.gameOverTime = pygame.time.get_ticks()


    def checkForEnemyBullets(self):
        global start_life
        redBulletsGroup = pygame.sprite.Group()

        for bullet in self.bullets:
            if bullet.color == RED:
                redBulletsGroup.add(bullet)

        for bullet in redBulletsGroup:
            if pygame.sprite.collide_rect(bullet, self.player):
                start_life -= 1
                bullet.kill()

    def shootEnemyBullet(self, rect):
        if (pygame.time.get_ticks() - self.enemyBulletTimer) > BULLETOFFSET:
            self.bullets.add(Bullet(rect, RED, 1, 5))
            self.allSprites.add(self.bullets)
            self.enemyBulletTimer = pygame.time.get_ticks()

    def findEnemyShooter(self):
        columnList = []
        for enemy in self.enemies:
            columnList.append(enemy.column)
        columnSet = set(columnList)
        columnList = list(columnSet)
        shuffle(columnList)
        column = columnList[0]
        enemyList = []
        rowList = []

        for enemy in self.enemies:
            if enemy.column == column:
                rowList.append(enemy.row)

        row = max(rowList)

        for enemy in self.enemies:
            if enemy.column == column and enemy.row == row:
                self.shooter = enemy

    def makePlayer(self):
        players = pygame.sprite.Group()
        player = Player()
        ##Place the player centerx and five pixels from the bottom
        player.rect.centerx = self.displayRect.centerx
        player.rect.bottom = self.displayRect.bottom - 5
        players.add(player)

        return player

    def makeEnemies(self):
        enemies = pygame.sprite.Group()
        for row in range(ARRAYHEIGHT):
            for column in range(ARRAYWIDTH):
                enemy = Enemy(row, column)
                enemy.rect.x = XMARGIN + (column * (MOB_WIDTH + ENEMYGAP))
                enemy.rect.y = YMARGIN + (row * (MOB_HEIGHT + ENEMYGAP))
                enemies.add(enemy)

        return enemies

    def checkInput(self):
        global extra_bullets_counter
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == QUIT:
                self.terminate()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE and len(self.greenBullets) < 1 and extra_bullets_counter == 0:
                    bullet = Bullet(self.player.rect, RED, -1, 20)
                    self.greenBullets.add(bullet)
                    self.bullets.add(self.greenBullets)
                    self.allSprites.add(self.bullets)

                elif event.key == K_SPACE and len(self.greenBullets) < 1 and extra_bullets_counter > 0:
                    bullet = Bullet(self.player.rect, RED, -1, 20)
                    bullet.update()
                    bullet_extra = Bullet(self.player.rect, RED, -1, 20)
                    bullet_extra2 = Bullet(self.player.rect, RED, -1, 20)
                    bullet_extra2.extraBullet2()
                    bullet_extra.extraBullet()
                    self.greenBullets.add(bullet_extra)
                    self.greenBullets.add(bullet_extra2)
                    self.greenBullets.add(bullet)
                    self.bullets.add(self.greenBullets)
                    self.allSprites.add(self.bullets)
                    extra_bullets_counter -= 1

                elif event.key == K_ESCAPE:
                    self.terminate()

    def gameStartInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYUP:
                self.gameOver = False
                self.gameStart = False
                self.beginGame = True


    def gameOverInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYUP:
                self.gameStart = True
                self.beginGame = False
                self.gameOver = False
                game_menu()

    def checkCollisions(self):
        self.checkForEnemyBullets()
        global start_score
        if pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
            start_score += 10
        global extra_bullets_counter
        reds = (shot for shot in self.bullets if shot.color == RED)
        red_bullets = pygame.sprite.Group(reds)
        pygame.sprite.groupcollide(red_bullets, self.players, True, False)
        if pygame.sprite.groupcollide(red_bullets, boosts, True, True):
            extra_bullets_counter = 5

    def collide_red_blockers(self):
        global extra_bullets_counter
        reds = (shot for shot in self.bullets if shot.color == RED)
        red_bullets = pygame.sprite.Group(reds)
        pygame.sprite.groupcollide(red_bullets, self.players, True, False)
        if pygame.sprite.groupcollide(red_bullets, boosts, True, True):
            extra_bullets_counter = 5


    def checkGameOver(self):
        global start_life
        global t0
        global start_score
        global level_number
        global MOVETIME
        if len(self.enemies) == 0:
            level_number += 1
            MOVETIME -= 150
            self.needToMakeEnemies = True

        if start_life == 0:
            self.gameOver = True
            self.gameStart = False
            self.beginGame = False
            self.gameOverTime = pygame.time.get_ticks()
            start_life = 3
            t0 = 0
            start_score = 0

        if level_number == 4:
            print("wygrana")
            self.gameOver = True
            self.gameStart = False
            self.beginGame = False
            self.gameOverTime = pygame.time.get_ticks()
            self.win.draw(self.displaySurf)

        else:
            for enemy in self.enemies:
                if enemy.rect.bottom > DISPLAYHEIGHT:
                    self.gameOver = True
                    self.gameStart = False
                    self.beginGame = False
                    self.gameOverTime = pygame.time.get_ticks()
                    start_life = 3
                    t0 = 0
                    start_score = 0

    def terminate(self):
        pygame.quit()
        sys.exit()

    def mainLoop(self):
        life = 3
        t0 = 0
        while True:
            t0 += 1
            if self.gameStart:
                self.resetGame()
                self.gameOver = False
                self.displaySurf.fill(black)
                self.introMessage1.draw(self.displaySurf)

                self.gameStartInput()
                pygame.display.update()

            elif self.gameOver:
                #self.playIntroSound = True
                self.displaySurf.fill(black)
                self.gameOverMessage.draw(self.displaySurf)
                # prevent users from exiting the GAME OVER screen
                # too quickly
                if (pygame.time.get_ticks() - self.gameOverTime) > 2000:
                    self.gameOverInput()
                pygame.display.update()

            elif self.beginGame:
                if self.needToMakeEnemies:
                    self.enemies = self.makeEnemies()
                    self.allSprites.add(self.enemies)
                    self.needToMakeEnemies = False
                    pygame.event.clear()

                else:
                    currentTime = pygame.time.get_ticks()
                    gameDisplay.blit(cosmosImg, (0, 0))
                   # self.displaySurf.fill(black)
                    level_counter(level_number)
                    lives(start_life)
                    your_score(start_score)
                    # WARUNEK PO KTORYM POJAWIA SIE BOOST
                    if t0 % 500 == 0:
                        boost = Boost(0, 500, boostImg)
                        boosts.add(boost)

                    self.checkInput()
                    self.allSprites.update(self.keys, currentTime)
                    boosts.draw(gameDisplay)
                    boosts.update()
                    if len(self.enemies) > 0:
                        self.findEnemyShooter()
                        self.shootEnemyBullet(self.shooter.rect)
                    self.checkCollisions()
                    self.allSprites.draw(self.displaySurf)
    #                self.blockerGroup1.draw(self.displaySurf)
                    pygame.display.update()
                    self.checkGameOver()
                    self.clock.tick(self.fps)
game_menu()
