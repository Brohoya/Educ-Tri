import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP

#setup fenetre + clock
clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Educ'Tri G@ming")
fenetre = pygame.display.set_mode((1024,600))
background = pygame.image.load('assets/paysageux.png')

loc = [300, 50]
lastLoc = [0, 0]
marge_ergo = 0.15
gaming = True
click = False
drag = False

class Dechet:
    def __init__(self, nom, largeur, hauteur, type):
        self.nom = nom
        self.taille = [largeur, hauteur]
        self.type = type
    def importer(self):
        dechet = pygame.image.load('assets/dechets/' + self.nom)
        return pygame.transform.scale(dechet, self.taille)

#déchets
jager = Dechet("jager.png", 60, 150, "vert")
bouteille = Dechet("bouteille.png", 100, 180, "jaune")
livre = Dechet("livre.png", 150, 150, "bleu")
pomme = Dechet("pomme.png", 75, 100, "composte")

#poubelles
taille_poubelle = [200, 230]
scale_ouverture = [taille_poubelle[0]*50/250, taille_poubelle[1]*100/280]
ouverture_loc = scale_ouverture[1];
ecart = 180

#jaune
loc_pj = [830, 350]
pjf = pygame.image.load('assets/poubelles/pjf.png')
pjf = pygame.transform.scale(pjf, taille_poubelle)
pjo = pygame.image.load('assets/poubelles/pjo.png')
pjo = pygame.transform.scale(pjo, (taille_poubelle[0] + scale_ouverture[0], taille_poubelle[1] + scale_ouverture[1]))

#vert
loc_pv = [loc_pj[0] - ecart, loc_pj[1]]
pvf = pygame.image.load('assets/poubelles/pvf.png')
pvf = pygame.transform.scale(pvf, taille_poubelle)
pvo = pygame.image.load('assets/poubelles/pvo.png')
pvo = pygame.transform.scale(pvo, (taille_poubelle[0] + scale_ouverture[0], taille_poubelle[1] + scale_ouverture[1]))

#bleu
loc_pb = [loc_pv[0] - ecart, loc_pv[1]]
pbf = pygame.image.load('assets/poubelles/pbf.png')
pbf = pygame.transform.scale(pbf, taille_poubelle)
pbo = pygame.image.load('assets/poubelles/pbo.png')
pbo = pygame.transform.scale(pbo, (taille_poubelle[0] + scale_ouverture[0], taille_poubelle[1] + scale_ouverture[1]))


while gaming:
    if not click: loc = [300, 50]

    #input de souris
    mx, my = pygame.mouse.get_pos()
    track = [mx, my]

    #background
    fenetre.blit(background, (-50, -75))

    #affichage poubelles
    if drag == True:
        if track[0] in range(loc_pj[0], (loc_pj[0] + taille_poubelle[0])) and track[1] in range(loc_pj[1], (loc_pj[1] + taille_poubelle[1])):
            fenetre.blit(pjo, (loc_pj[0], loc_pj[1] - ouverture_loc))
        else: fenetre.blit(pjf, loc_pj)

        if track[0] in range(loc_pv[0], (loc_pv[0] + taille_poubelle[0])) and track[1] in range(loc_pv[1], (loc_pv[1] + taille_poubelle[1])):
            fenetre.blit(pvo, (loc_pv[0], loc_pv[1] - ouverture_loc))
        else: fenetre.blit(pvf, loc_pv)

        if track[0] in range(loc_pb[0], (loc_pb[0] + taille_poubelle[0])) and track[1] in range(loc_pb[1], (loc_pb[1] + taille_poubelle[1])):
            fenetre.blit(pbo, (loc_pb[0], loc_pb[1] - ouverture_loc))
        else: fenetre.blit(pbf, loc_pb)
    else:
        fenetre.blit(pjf, loc_pj)
        fenetre.blit(pvf, loc_pv)
        fenetre.blit(pbf, loc_pb)

    #input de boutons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                gaming = False
                pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  #1 => gauche  | 2 => molette | 3 => droit
                click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                click = False
                drag = False
                

    #dragging
    fenetre.blit(jager.importer(), (loc[0], loc[1]))
    taille_dechet = jager.taille
    if click and track[0]<=(loc[0] + taille_dechet[0])*(1 + marge_ergo) and track[0]>=(loc[0])*(1 - marge_ergo) and track[1]<=(loc[1] + taille_dechet[1])*(1 + marge_ergo) and track[1]>=(loc[1])*(1 - marge_ergo):
        loc = [track[0] - taille_dechet[0]/2, track[1] - taille_dechet[1]/2]
        lastLoc = [track[0], track[1]]
        drag = True
    

    #maj de la fenetre
    pygame.display.flip()   #maj de l'écran (.update() fait la meme chose si pas d'argument)

    clock.tick(60)
