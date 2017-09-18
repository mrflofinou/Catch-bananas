"""
Ce fichier contient les classes du programmes
Il y a deux classes:
La classe : personnage
La classe Plateau
"""
import random

import pygame
from pygame.locals import *

from constantes import *

#class Plateau:
#    def affichage(self, fenetre):
#        fond = pygame.image.load(sol).convert()
#        fenetre.blit(fond, (0, 0))


class Personnage:
    def __init__(self):
        #self.avatar = pygame.image.load(perso).convert_alpha()
        self.case_x = 0
        self.case_y = 14
        self.x = 0
        self.y = 420

    def deplacement(self, direction):
        if direction == 'droite':
            if self.case_x < (nombre_sprite_cote - 1):
                self.case_x += 1
                self.x = self.case_x * taille_sprite

        if direction == 'gauche':
            if self.case_x > 0:
                self.case_x -= 1
                self.x = self.case_x * taille_sprite

        if direction == 'haut':
            if self.case_y > 0:
                self.case_y -= 1
                self.y = self.case_y * taille_sprite

        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                self.case_y += 1
                self.y = self.case_y * taille_sprite

class Bananes:
    def __init__(self):
        #self.avatar = pygame.image.load(banane).convert_alpha()
        self.case_x = random.randint(0, 14)
        self.case_y = random.randint(0, 14)
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite
