import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

playerSprite = pygame.sprite.Sprite()
enemySprite = pygame.sprite.Sprite()
enemySpeed = 0
bg = pygame.image.load("nebo.jpg")


def playerInit():
    global playerSprite
    # playerSprite.image = pygame.Surface((75, 25))
    playerSprite.image = pygame.image.load("samolet.jpg").convert()
    # playerSprite.image.fill((255,255,255))
    playerSprite.image.set_colorkey((255, 255, 255), RLEACCEL)
    playerSprite.rect = playerSprite.image.get_rect()


def playerUpdate(pressed_keys):
    global playerSprite
    if pressed_keys[K_UP]:
        playerSprite.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        playerSprite.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        playerSprite.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        playerSprite.rect.move_ip(5, 0)

    if playerSprite.rect.left < 0:
        playerSprite.rect.left = 0
    if playerSprite.rect.right > SCREEN_WIDTH:
        playerSprite.rect.right = SCREEN_WIDTH
    if playerSprite.rect.top <= 0:
        playerSprite.rect.top = 0
    if playerSprite.rect.bottom >= SCREEN_HEIGHT:
        playerSprite.rect.bottom = SCREEN_HEIGHT


def enemyInit():
    global enemySpeed
    global enemySprite
    # enemySprite.image = pygame.Surface((20, 10))
    enemySprite.image = pygame.image.load("raketa.png").convert()
    # enemySprite.image.fill((255,255,255))
    enemySprite.image.set_colorkey((255, 255, 255), RLEACCEL)
    enemySprite.rect = enemySprite.image.get_rect(
        center=(
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
            random.randint(0, SCREEN_HEIGHT),
        )
    )
    enemySpeed = random.randint(5, 10)


def enemyUpdate():
    global enemySprite
    enemySprite.rect.move_ip(-enemySpeed, 0)
    if enemySprite.rect.right < 0:
        enemySprite.rect = enemySprite.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

playerInit()
enemyInit()
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    playerUpdate(pressed_keys)
    enemyUpdate()


    if pygame.sprite.collide_rect(playerSprite, enemySprite):
        playerInit()
        enemyInit()
        try:
            import Tkinter as tk
        except:
            import tkinter as tk



        root = tk.Tk()
        root.geometry("200x200")
        root.title("PyGame")
        root.resizable(width=0 , height=0)


        button = tk.Button(text="Попробовать снова", command=root.destroy, padx="15", pady="6")
        button.place(x=40,y=70,width=120,height=50)

        root.geometry('200x200-805-505')
        root.mainloop()



    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # screen.blit(playerSprite.image, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(playerSprite.image, playerSprite.rect)
    screen.blit(enemySprite.image, enemySprite.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



