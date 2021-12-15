import pygame
from assets.classes.bouton import Bouton

class Menu():
    def __init__(self, jeu, reglages):
        fenetre = [1024, 600]

        #parametres sur les boutons
        bouton_central = 208
        boutons_lateraux = 158
        hauteur_bouton = 240
        ecart = 70
        
        #attributs
        self.lanced = False
        self.jeu = jeu
        self.background = pygame.image.load('assets/interface/fond_accueil.png')
        self.click = False
        self.reglages = reglages
        self.bouton_poubelle = Bouton("bouton_poubelle", [int(fenetre[0]/2 - bouton_central/2), hauteur_bouton])
        self.bouton_jouer = Bouton("bouton_jouer", [int(fenetre[0]/2 - bouton_central/2 - ecart - boutons_lateraux), hauteur_bouton + bouton_central - boutons_lateraux])
        self.bouton_apprendre = Bouton("bouton_apprendre", [int(fenetre[0]/2 + bouton_central/2 + ecart), hauteur_bouton + bouton_central - boutons_lateraux])
        self.bouton_maintenance = Bouton("bouton_maintenance", [20, 20])
        self.bouton_aide = Bouton("bouton_aide", [fenetre[0] - 20 - 88, 20])
        self.aide_maintenance = [pygame.image.load("assets/interface/affichages/aide_maintenance.png"), [110, 30]]
        self.aide_poubelle = [pygame.image.load("assets/interface/affichages/aide_poubelle.png"), [350, 130]]
        self.aide_jouer = [pygame.image.load("assets/interface/affichages/aide_jouer.png"), [185, 450]]
        self.aide_apprendre = [pygame.image.load("assets/interface/affichages/aide_apprendre.png"), [645, 450]]

    def update(self, fenetre):
        fenetre.blit(self.background, (0, 0))

        if self.bouton_jouer.isClicked(self.click, fenetre):
            self.jeu.lanced = True
            self.lanced = False

        if self.bouton_poubelle.isClicked(self.click, fenetre):
            a=2

        if self.bouton_apprendre.isClicked(self.click, fenetre):
            fenetre.blit(self.bouton_apprendre.clicked, self.bouton_apprendre.loc)

        if self.bouton_maintenance.isClicked(self.click, fenetre):
            self.reglages.lanced = True
            self.lanced = False

        if self.bouton_aide.isClicking(self.click):
            fenetre.blit(self.bouton_aide.clicked, self.bouton_aide.loc)
            fenetre.blit(self.aide_maintenance[0], self.aide_maintenance[1])
            fenetre.blit(self.aide_jouer[0], self.aide_jouer[1])
            fenetre.blit(self.aide_poubelle[0], self.aide_poubelle[1])
            fenetre.blit(self.aide_apprendre[0], self.aide_apprendre[1])
        else: fenetre.blit(self.bouton_aide.show, self.bouton_aide.loc)

            
        # self.bouton_poubelle.hover(track)
