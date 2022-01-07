import pygame
from assets.classes.bouton import Bouton
import json

class Pincode:
    def __init__(self, code):
        self.show = False
        self.back = False
        self.code = str(code)
        self.pin = ""
        self.ecran = pygame.image.load('assets/images/interface/affichages/ecran.png')
        ecart = 15
        self.fenetre = [1024, 600]
        self.font_pin = pygame.font.Font("assets/images/interface/Acme-Regular.ttf", 110)
        self.font_mdp = pygame.font.Font("assets/images/interface/Acme-Regular.ttf", 25)
        # print(pygame.font.get_fonts())
        width = pygame.image.load('assets/images/interface/boutons/huit.png').get_size()[0]
        self.huit = Bouton("huit", [int(self.fenetre[0]/2 - width/2), 210])
        self.neuf = Bouton("neuf", [int(self.fenetre[0]/2 + width/2 + ecart), self.huit.loc[1]])
        self.sept = Bouton("sept", [int(self.fenetre[0]/2 - (3*width/2) - ecart), self.huit.loc[1]])
        self.cinq = Bouton("cinq", [int(self.fenetre[0]/2 - width/2), self.huit.loc[1] + self.huit.height + ecart])
        self.six = Bouton("six", [int(self.fenetre[0]/2 + width/2 + ecart), self.huit.loc[1] + self.huit.height + ecart])
        self.quatre = Bouton("quatre", [int(self.fenetre[0]/2 - (3*width/2) - ecart), self.huit.loc[1] + self.huit.height + ecart])
        self.deux = Bouton("deux", [int(self.fenetre[0]/2 - width/2), self.huit.loc[1] + 2 * (self.huit.height + ecart)])
        self.trois = Bouton("trois", [int(self.fenetre[0]/2 + width/2 + ecart), self.huit.loc[1] + 2 * (self.huit.height + ecart)])
        self.un = Bouton("un", [int(self.fenetre[0]/2 - (3*width/2) - ecart), self.huit.loc[1] + 2 * (self.huit.height + ecart)])
        self.zero = Bouton("zero", [int(self.fenetre[0]/2 + width/2 + ecart), self.huit.loc[1] + 3 * (self.huit.height + ecart)])
        self.retour = Bouton("retour", [int(self.fenetre[0]/2 - (3*width/2) - ecart), self.huit.loc[1] + 3 * (self.huit.height + ecart)])
        self.retenter = Bouton("retour", [int(self.fenetre[0]/2 - width), 3 * (self.huit.height + ecart)])

    def update(self, fenetre, click):
        # print("HAAAAAAAAAAAAAAAAAAAAAAA ", self.retour.loc)

        if self.pin != self.code:

            if len(self.pin) < 4:

                if self.retour.isClicked(click, fenetre):
                    self.back = True 

                if self.zero.isClicked(click, fenetre):
                    self.pin += "0"

                if self.un.isClicked(click, fenetre):
                    self.pin += "1"

                if self.deux.isClicked(click, fenetre):
                    self.pin += "2"

                if self.trois.isClicked(click, fenetre):
                    self.pin += "3"

                if self.quatre.isClicked(click, fenetre):
                    self.pin += "4"

                if self.cinq.isClicked(click, fenetre):
                    self.pin += "5"

                if self.six.isClicked(click, fenetre):
                    self.pin += "6"

                if self.sept.isClicked(click, fenetre):
                    self.pin += "7"

                if self.huit.isClicked(click, fenetre):
                    self.pin += "8"

                if self.neuf.isClicked(click, fenetre):
                    self.pin += "9"

                self.text = self.font_pin.render(str("• " * len(self.pin)), True, (0, 0, 0))
                text_rect = self.text.get_rect(center=(self.fenetre[0]/2, 140))
            else:
                self.text = self.font_mdp.render("Mot de passe incorrect", True, (0, 0, 0))
                text_rect = self.text.get_rect(center=(self.fenetre[0]/2, 145))
                
                if self.retenter.isClicked(click, fenetre):
                    self.pin = ""
            
            fenetre.blit(self.ecran, (360, 105))
            fenetre.blit(self.text, text_rect)

        else: 
            self.show = False
            self.clear()



    
    def Retour(self):
        if self.back:
            return True
        else: return False

    def clear(self):
        self.pin = ""
        self.back = False