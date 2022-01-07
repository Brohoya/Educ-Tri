import pygame
import random
from assets.classes.poubelles import Poubelles
from assets.classes.dechets import Dechet
from pygame import gfxdraw

class Jeu:
    def __init__(self):
        self.lanced = False
        self.background = pygame.image.load('assets/images/jeu/paysageux.png')
        self.poubelles = Poubelles()
        self.dechets = Dechet()

        self.num = self.spawner(-1)
        self.dechet = self.dechets.dechets[self.num]
        self.taille_dechet = self.dechet[0][1]

        self.score = 0
        self.loc = [300, 50]
        self.drag = False
        self.click = False
        self.marge_ergo = 0.15

        self.font = pygame.font.SysFont(None, 24)
        self.color = (0, 0, 255)

    def spawner(self, num):
            if(num<0):
                return random.randint(0, len(self.dechets.dechets) - 1)
            else:
                self.dechets.dechets.pop(num)
                if len(self.dechets.dechets) <= 0: return -1
                else: return random.randint(0, len(self.dechets.dechets) - 1)

    def update(self, fenetre):
        #inputs
        track = pygame.mouse.get_pos()
        self.affichage_score = self.font.render("SCORE : " + str(self.score), True, (0, 0, 0))

        #background
        fenetre.blit(self.background, (-50, -75))
        #dechet
        fenetre.blit(self.dechet[1], (self.loc[0], self.loc[1]))
        #score
        fenetre.blit(self.affichage_score, (800, 50))

        if not self.click and self.drag:
            self.checkScore(track)
            self.drag = False
            self.loc = [300, 50]

        #drag
        if self.click and track[0]<=(self.loc[0] + self.taille_dechet[0])*(1 + self.marge_ergo) and track[0]>=(self.loc[0])*(1 - self.marge_ergo) and track[1]<=(self.loc[1] + self.taille_dechet[1])*(1 + self.marge_ergo) and track[1]>=(self.loc[1])*(1 - self.marge_ergo):
            self.loc = [int(track[0] - self.taille_dechet[0]/2), int(track[1] - self.taille_dechet[1]/2)]
            gfxdraw.pixel(fenetre, self.loc[0], self.loc[1], self.color)
            gfxdraw.pixel(fenetre, int(self.loc[0] + self.taille_dechet[0]), self.loc[1], self.color)
            gfxdraw.pixel(fenetre, self.loc[0], int(self.loc[1] + self.taille_dechet[1]), self.color)
            gfxdraw.pixel(fenetre, int(self.loc[0] + self.taille_dechet[0]), int(self.loc[1] + self.taille_dechet[1]), self.color)
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

            if track[0] in range(self.poubelles.loc_pn[0], (self.poubelles.loc_pn[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pn[1], (self.poubelles.loc_pn[1] + self.poubelles.taille_poubelle[1])):
                fenetre.blit(self.poubelles.pno, (self.poubelles.loc_pn[0], self.poubelles.loc_pn[1] - self.poubelles.ouverture_loc))
            else: fenetre.blit(self.poubelles.pnf, self.poubelles.loc_pn)
        else:
            fenetre.blit(self.poubelles.pjf, self.poubelles.loc_pj)
            fenetre.blit(self.poubelles.pvf, self.poubelles.loc_pv)
            fenetre.blit(self.poubelles.pbf, self.poubelles.loc_pb)
            fenetre.blit(self.poubelles.pnf, self.poubelles.loc_pn)

    def checkScore(self, track):

        if self.drag and track[0] in range(self.poubelles.loc_pj[0], (self.poubelles.loc_pj[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pj[1], (self.poubelles.loc_pj[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "jaune":
                if len(self.dechets.dechets) > 0:
                    print(len(self.dechets.dechets))
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("ha batard tu fumes ?!")

        elif track[0] in range(self.poubelles.loc_pv[0], (self.poubelles.loc_pv[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pv[1], (self.poubelles.loc_pv[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "vert":
                if len(self.dechets.dechets) > 0:
                    print(len(self.dechets.dechets))
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("fichtre diantre ?!")

        elif track[0] in range(self.poubelles.loc_pb[0], (self.poubelles.loc_pb[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pb[1], (self.poubelles.loc_pb[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "bleu":
                if len(self.dechets.dechets) > 0:
                    print(len(self.dechets.dechets))
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("tu n'es point gaté par la nature ma parole ?!")

        elif track[0] in range(self.poubelles.loc_pn[0], (self.poubelles.loc_pn[0] + self.poubelles.taille_poubelle[0])) and track[1] in range(self.poubelles.loc_pn[1], (self.poubelles.loc_pn[1] + self.poubelles.taille_poubelle[1])):
            if self.dechet[0][2] == "noir":
                if len(self.dechets.dechets) > 0:
                    print(len(self.dechets.dechets))
                    self.num = self.spawner(self.num)
                    self.score += 1
            else:
                print("sur le coran jvais tniquer !!")

        if len(self.dechets.dechets) <= 0:
            self.score = 0
            self.dechets = Dechet()
            self.num = self.spawner(-1)
            self.lanced = False
            # menu.lanced = True
        else :
            self.dechet = self.dechets.dechets[self.num]
            self.taille_dechet = self.dechet[0][1]
            
        self.drag = False

        print("SCORE : ", self.score)


