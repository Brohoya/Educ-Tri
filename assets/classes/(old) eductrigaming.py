from math import fabs
from os import defpath
from os import truncate
import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP
import random
from assets.classes.menu import Menu
from assets.classes.poubelles import Poubelles
from assets.classes.dechets import Dechet

menu = Menu()

class Jeu:
    def __init__(self):
        self.lanced = False
        self.background = pygame.image.load('assets/bordel/paysageux.png')
        self.poubelles = Poubelles()
        self.dechets = Dechet()
        self.num = self.spawner(-1)
        self.score = 0
        self.loc = [300, 50]
        self.drag = False
        self.dechet = self.dechets.dechets[self.num]
        self.taille_dechet = self.dechet[0][1]
        self.marge_ergo = 0.15

    def spawner(self, num):
            if(num<0):
                return random.randint(0, len(self.dechets.dechets) - 1)
            else:
                self.dechets.dechets.pop(num)
                if len(self.dechets.dechets) <= 0: return -1
                else: return random.randint(0, len(self.dechets.dechets) - 1)

    def update(self, track, fenetre, click):
        #background
        fenetre.blit(self.background, (-50, -75))
        #dechet
        fenetre.blit(self.dechet[1], (self.loc[0], self.loc[1]))

        # for event in pygame.event.get():
        #     if event.type == MOUSEBUTTONDOWN:
        #         if event.button == 1:  #1 => gauche  | 2 => molette | 3 => droit
        #             click = True
        #             if not jeu.lanced:
        #                 jeu.lanced = True
        #     if event.type == MOUSEBUTTONUP:
        #         if event.button == 1:
        #             if menu.lanced:
        #                 if menu.bouton_jouer.isClicked(track, click):
        #                     menu.lanced = False
        #                     jeu.lanced = True
        #             click = False

        if not click and self.drag:
            self.checkScore(track)
            self.drag = False
            self.loc = [300, 50]

        #drag
        if click and track[0]<=(self.loc[0] + self.taille_dechet[0])*(1 + self.marge_ergo) and track[0]>=(self.loc[0])*(1 - self.marge_ergo) and track[1]<=(self.loc[1] + self.taille_dechet[1])*(1 + self.marge_ergo) and track[1]>=(self.loc[1])*(1 - self.marge_ergo):
            self.loc = [track[0] - self.taille_dechet[0]/2, track[1] - self.taille_dechet[1]/2]
            self.drag = True

        #affichage poubelles
        if self.drag == True:
            if track[0] in range(self.poubelles.loc_pj[0], (self.poubelles.loc_pj[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pj[1], (self.poubelles.loc_pj[1] + self.poubelles.taille_poubelle[1])):
                fenetre.blit(self.poubelles.pjo, (self.poubelles.loc_pj[0], self.poubelles.loc_pj[1] - self.poubelles.ouverture_loc))
            else: fenetre.blit(self.poubelles.pjf, self.poubelles.loc_pj)

            if track[0] in range(self.poubelles.loc_pv[0], (self.poubelles.loc_pv[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pv[1], (self.poubelles.loc_pv[1] + self.poubelles.taille_poubelle[1])):
                fenetre.blit(self.poubelles.pvo, (self.poubelles.loc_pv[0], self.poubelles.loc_pv[1] - self.poubelles.ouverture_loc))
            else: fenetre.blit(self.poubelles.pvf, self.poubelles.loc_pv)

            if track[0] in range(self.poubelles.loc_pb[0], (self.poubelles.loc_pb[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pb[1], (self.poubelles.loc_pb[1] + self.poubelles.taille_poubelle[1])):
                fenetre.blit(self.poubelles.pbo, (self.poubelles.loc_pb[0], self.poubelles.loc_pb[1] - self.poubelles.ouverture_loc))
            else: fenetre.blit(self.poubelles.pbf, self.poubelles.loc_pb)

            if track[0] in range(self.poubelles.loc_co[0], (self.poubelles.loc_co[0] + self.poubelles.taille_composte[0])) and track[1] in range(self.poubelles.loc_co[1], (self.poubelles.loc_co[1] + self.poubelles.taille_composte[1])):
                fenetre.blit(self.poubelles.coo, (self.poubelles.loc_co[0], self.poubelles.loc_co[1] - 5))
            else: fenetre.blit(self.poubelles.cof, self.poubelles.loc_co)
        else:
            fenetre.blit(self.poubelles.pjf, self.poubelles.loc_pj)
            fenetre.blit(self.poubelles.pvf, self.poubelles.loc_pv)
            fenetre.blit(self.poubelles.pbf, self.poubelles.loc_pb)
            fenetre.blit(self.poubelles.cof, self.poubelles.loc_co)

    def checkScore(self, track):

        if self.drag and track[0] in range(self.poubelles.loc_pj[0], (self.poubelles.loc_pj[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pj[1], (self.poubelles.loc_pj[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "jaune":
                if len(self.dechets.dechets) > 0:
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("ha batard tu fumes ?!")

        elif track[0] in range(self.poubelles.loc_pv[0], (self.poubelles.loc_pv[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pv[1], (self.poubelles.loc_pv[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "vert":
                if len(self.dechets.dechets) > 0:
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("fichtre diantre ?!")

        elif track[0] in range(self.poubelles.loc_pb[0], (self.poubelles.loc_pb[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pb[1], (self.poubelles.loc_pb[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "bleu":
                if len(self.dechets.dechets) > 0:
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("tu n'es point gaté par la nature ma parole ?!")

        elif track[0] in range(self.poubelles.loc_co[0], (self.poubelles.loc_co[0] + self.poubelles.taille_composte[0])) and track[1] in range(self.poubelles.loc_co[1], (self.poubelles.loc_co[1] + self.poubelles.taille_composte[1])):
            if self.dechet[0][2] == "noir":
                if len(self.dechets.dechets) > 0:
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("sur le coran jvais tniquer !!")

        if len(self.dechets.dechets) <= 0:
            print("FIIIIIIN")
            self.lanced = False
            # menu.lanced = True
        else :
            self.dechet = self.dechets.dechets[self.num]
            
        self.drag = False

        print("SCORE : ", self.score)


