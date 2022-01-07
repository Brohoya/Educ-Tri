import pygame

class Poubelles:
    def __init__(self):
        self.taille_poubelle = [200, 230]
        self.scale_ouverture = [self.taille_poubelle[0]*50/250, self.taille_poubelle[1]*100/280]
        self.ouverture_loc = self.scale_ouverture[1];
        self.ecart = 180

        #jaune
        self.loc_pj = [830, 350]
        self.pjf = pygame.image.load('assets/images/poubelles/pjf.png')
        self.pjf = pygame.transform.scale(self.pjf, self.taille_poubelle)
        self.pjo = pygame.image.load('assets/images/poubelles/pjo.png')
        self.pjo = pygame.transform.scale(self.pjo, (self.taille_poubelle[0] + self.scale_ouverture[0], self.taille_poubelle[1] + self.scale_ouverture[1]))

        #vert
        self.loc_pv = [self.loc_pj[0] - self.ecart, self.loc_pj[1]]
        self.pvf = pygame.image.load('assets/images/poubelles/pvf.png')
        self.pvf = pygame.transform.scale(self.pvf, self.taille_poubelle)
        self.pvo = pygame.image.load('assets/images/poubelles/pvo.png')
        self.pvo = pygame.transform.scale(self.pvo, (self.taille_poubelle[0] + self.scale_ouverture[0], self.taille_poubelle[1] + self.scale_ouverture[1]))

        #bleu
        self.loc_pb = [self.loc_pv[0] - self.ecart, self.loc_pv[1]]
        self.pbf = pygame.image.load('assets/images/poubelles/pbf.png')
        self.pbf = pygame.transform.scale(self.pbf, self.taille_poubelle)
        self.pbo = pygame.image.load('assets/images/poubelles/pbo.png')
        self.pbo = pygame.transform.scale(self.pbo, (self.taille_poubelle[0] + self.scale_ouverture[0], self.taille_poubelle[1] + self.scale_ouverture[1]))

        #composte
        self.loc_pn = [self.loc_pb[0] - self.ecart, self.loc_pb[1]]
        self.pnf = pygame.image.load('assets/images/poubelles/pnf.png')
        self.pnf = pygame.transform.scale(self.pnf, self.taille_poubelle)
        self.pno = pygame.image.load('assets/images/poubelles/pno.png')
        self.pno = pygame.transform.scale(self.pno, (self.taille_poubelle[0] + self.scale_ouverture[0], self.taille_poubelle[1] + self.scale_ouverture[1]))