import pygame
from assets.classes.pincode import Pincode

class Reglages:
    def __init__(self):
        self.lanced = False
        self.code = 6666
        self.pincode = Pincode(self.code)
        self.pincode.show = True
        self.click = False
        self.background = pygame.image.load('assets/interface/fond_accueil.png')
        self.back = pygame.image.load('assets/interface/boutons/bouton_maintenance_clicked.png')
    def update(self, fenetre):
        fenetre.blit(self.background, (0, 0))
        fenetre.blit(self.back, (20, 20))
        if self.pincode.show and not self.pincode.Retour():
            self.pincode.update(fenetre, self.click)
        elif self.pincode.Retour():
            self.pincode = Pincode(self.code)
            self.lanced = False
            self.pincode.show = True
        else:
            fenetre.blit(self.back, (50, 50))
            