from os import truncate
import random
import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP
pygame.init()

pygame.display.set_caption("Educ'Tri G@ming")
fenetre = pygame.display.set_mode((1024,600))
background = pygame.image.load('assets/paysageux.png')

running = True

loc = [300, 50]
lastLoc = [0, 0]
marge_ergo = 0.15
click = False
drag = False
score = 0

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
jager = [jager, jager.importer()]
bouteille = Dechet("bouteille.png", 100, 180, "jaune")
bouteille = [bouteille, bouteille.importer()]
livre = Dechet("livre.png", 150, 150, "bleu")
livre = [livre, livre.importer()]
pomme = Dechet("pomme.png", 75, 100, "composte")
pomme = [pomme, pomme.importer()]
dechets = [jager, bouteille, livre, pomme]


#poubelles
taille_poubelle = [200, 230]
scale_ouverture = [taille_poubelle[0]*50/250, taille_poubelle[1]*100/280]
ouverture_loc = scale_ouverture[1];
ecart = 180
taille_composte = [150, 200]

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

#composte
loc_co = [loc_pb[0] - ecart, loc_pb[1] + 30]
cof = pygame.image.load('assets/poubelles/composte.png')
cof = pygame.transform.scale(cof, taille_composte)
# coo = pygame.transform.scale(cof, (taille_poubelle[0] + 0.1, taille_poubelle[1] + 0.1))
coo = cof

def spawner(num):
    if(num<0):
        return random.randint(0, len(dechets) - 1)
    else:
        dechets.pop(num)
        return random.randint(0, len(dechets) - 1)

num = spawner(-1)

while running:
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

        if track[0] in range(loc_co[0], (loc_co[0] + taille_composte[0])) and track[1] in range(loc_co[1], (loc_co[1] + taille_composte[1])):
            fenetre.blit(coo, (loc_co[0], loc_co[1] - 5))
        else: fenetre.blit(cof, loc_co)
    else:
        fenetre.blit(pjf, loc_pj)
        fenetre.blit(pvf, loc_pv)
        fenetre.blit(pbf, loc_pb)
        fenetre.blit(cof, loc_co)

    dechet = dechets[num]
    # fenetre.blit(pomme[1], (loc[0], loc[1]))
    fenetre.blit(dechets[num][1], (loc[0], loc[1]))
    taille_dechet = dechets[num][0].taille

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
                if lastLoc[0] in range(loc_pj[0], (loc_pj[0] + taille_poubelle[0])) and lastLoc[1] in range(loc_pj[1], (loc_pj[1] + taille_poubelle[1])):
                    if dechets[num][0].type == "jaune":
                        num = spawner(num)
                        score += 1
                    else:
                        print("ha batard tu fumes ?!")
                elif lastLoc[0] in range(loc_pv[0], (loc_pv[0] + taille_poubelle[0])) and lastLoc[1] in range(loc_pv[1], (loc_pv[1] + taille_poubelle[1])):
                    if dechets[num][0].type == "vert":
                        num = spawner(num)
                        score += 1
                    else:
                        print("fichtre diantre ?!")
                elif lastLoc[0] in range(loc_pb[0], (loc_pb[0] + taille_poubelle[0])) and lastLoc[1] in range(loc_pb[1], (loc_pb[1] + taille_poubelle[1])):
                    if dechets[num][0].type == "bleu":
                        num = spawner(num)
                        score += 1
                    else:
                        print("tu n'es point gaté par la nature ma parole ?!")
                elif lastLoc[0] in range(loc_co[0], (loc_co[0] + taille_composte[0])) and lastLoc[1] in range(loc_co[1], (loc_co[1] + taille_composte[1])):
                    if dechets[num][0].type == "composte":
                        num = spawner(num)
                        score += 1
                    else:
                        print("sur le coran jvais tniquer !!")
            click = False
            drag = False
            # print(dechets)
                

    #dragging
    if click and track[0]<=(loc[0] + taille_dechet[0])*(1 + marge_ergo) and track[0]>=(loc[0])*(1 - marge_ergo) and track[1]<=(loc[1] + taille_dechet[1])*(1 + marge_ergo) and track[1]>=(loc[1])*(1 - marge_ergo):
        loc = [track[0] - taille_dechet[0]/2, track[1] - taille_dechet[1]/2]
        lastLoc = [track[0], track[1]]
        drag = True
    

    #maj de la fenetre
    pygame.display.flip()   #maj de l'écran (.update() fait la meme chose si pas d'argument)

