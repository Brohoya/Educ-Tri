import pygame

class Bouton:

    def __init__(self, nomBouton, loc):
        self.loc = loc
        self.drag = False
        self.show = pygame.image.load('assets/interface/boutons/' + nomBouton + '.png')
        self.clicked = pygame.image.load('assets/interface/boutons/' + nomBouton + '_clicked.png')
        self.width, self.height = self.show.get_size()

    def isClicked(self, click, fenetre):
        track = pygame.mouse.get_pos()
        if click and track[0] in range(self.loc[0], self.loc[0] + self.width) and track[1] in range(self.loc[1], self.loc[1] + self.height):
            self.drag = True
            fenetre.blit(self.clicked, self.loc)
            return False
        elif not click and self.drag and track[0] in range(self.loc[0], self.loc[0] + self.width) and track[1] in range(self.loc[1], self.loc[1] + self.height):
            self.drag = False
            fenetre.blit(self.clicked, self.loc)
            return True
        else: 
            fenetre.blit(self.show, self.loc)
            self.drag = False
            return False

    def isClicking(self, click):
        track = pygame.mouse.get_pos()
        if click and track[0] in range(self.loc[0], self.loc[0] + self.width) and track[1] in range(self.loc[1], self.loc[1] + self.height):
            return True
        else: return False
        

