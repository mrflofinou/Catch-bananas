"""
This file contains the classes of the programm
There are two classes:
- Characters
- Board
"""
import random

import pygame
from pygame.locals import *

import constants

#class Board:
#    def affichage(self, window):
#        background = pygame.image.load(floar).convert()
#        window.blit(background, (0, 0))


class Characters:
    def __init__(self):
        #self.avatar = pygame.image.load(perso).convert_alpha()
        self.case_x = 0
        self.case_y = 14
        self.x = 0
        self.y = 420

    def move(self, direction):
        if direction == 'right':
            if self.case_x < (constants.number_cases_side - 1):
                self.case_x += 1
                self.x = self.case_x * constants.size_case

        if direction == 'left':
            if self.case_x > 0:
                self.case_x -= 1
                self.x = self.case_x * constants.size_case

        if direction == 'up':
            if self.case_y > 0:
                self.case_y -= 1
                self.y = self.case_y * constants.size_case

        if direction == 'down':
            if self.case_y < (constantes.number_cases_side - 1):
                self.case_y +=
                self.y = self.case_y * constants.size_case

class Bananas:
    def __init__(self):
        #self.avatar = pygame.image.load(banane).convert_alpha()
        self.case_x = random.randint(0, 14)
        self.case_y = random.randint(0, 14)
        self.x = self.case_x * constants.size_case
        self.y = self.case_y * constants.size_case
