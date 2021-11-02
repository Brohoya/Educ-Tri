import pygame
import os

class Dechet:
    def __init__(self):
        self.dechets = []
        tailleMax = 130
        liste = os.listdir("assets/dechets")
        for i in liste:
            image = pygame.image.load('assets/dechets/' + i)
            width, height = image.get_size()

            #adaptation taille
            if width != tailleMax and height != tailleMax:
                if width > height:
                    if width > tailleMax:
                        taille = [tailleMax, height * tailleMax/width]
                    else: taille = [tailleMax, height * tailleMax/width]
                elif height > width:
                    if height > tailleMax:
                        taille = [width * tailleMax/height, tailleMax]
                    else: taille = [width * tailleMax/height, tailleMax]
                else: taille = [tailleMax, tailleMax]
                image = pygame.transform.scale(image, taille)
            else: taille = [width, height]

            nom = i.split("_")
            nom = ".".join(nom).split(".")
            self.dechets.append([[nom[1], taille, nom[0]], image])

        # print(self.dechets)
