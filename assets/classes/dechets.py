import pygame
import os
import json


class Dechet:
    def __init__(self):
        self.dechets = []
        self.database = json.load(open('assets/database.json'))
        tailleMax = 130
        # liste = os.listdir("assets/dechets")
        for i in self.database['dechets']:
            image = pygame.image.load('assets/images/dechets/' + i['image'])
            # print(self.database['infos'])
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

            self.dechets.append([[i['nom'], taille, i['type']], image])

        # print(self.dechets)
