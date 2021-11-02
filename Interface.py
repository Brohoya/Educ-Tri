import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from assets.classes.eductrigaming import *
from assets.classes.maintenance import Reglages
from assets.classes.menu import Menu
pygame.init()

pygame.display.set_caption("Educ'Tri G@ming")
resolution = [1024, 600]
fenetre = pygame.display.set_mode(resolution)
click = False

background = pygame.image.load('assets/bordel/paysageux.png')

jeu = Jeu()
reglages = Reglages()
menu = Menu(jeu, reglages)
running = True

while running:

    #inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  #1 => gauche  | 2 => molette | 3 => droit
                if menu.lanced:
                    menu.click = True
                if jeu.lanced:
                    jeu.click = True
                if reglages.lanced:
                    reglages.click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if menu.lanced:
                    menu.click = False
                if jeu.lanced:
                    jeu.click = False
                if reglages.lanced:
                    reglages.click = False
                
    if jeu.lanced:
        jeu.update(fenetre)
    else:                       #à enlever quand il y aura un screen de fin de game
        menu.lanced = True

    if menu.lanced:
        menu.update(fenetre)

    if reglages.lanced:
        reglages.update(fenetre)

    #maj de la fenetre (.update() fait la meme chose si pas d'argument)
    pygame.display.flip()   

