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


class Characters:
    """
    This class create a character and manage its position
    """
    def __init__(self):
        self.pixels_x = 0
        self.pixels_y = 420

    def move(self, direction):
        """
        This method manage the movement of the character
        """
        if direction == 'right':
            if self.pixels_x < (constants.number_pixel_side - constants.size_sprite):
                self.pixels_x += constants.size_sprite

        if direction == 'left':
            if self.pixels_x > 0:
                self.pixels_x -= constants.size_sprite

        if direction == 'up':
            if self.pixels_y > 0:
                self.pixels_y -= constants.size_sprite

        if direction == 'down':
            if self.pixels_y < (constants.number_pixel_side - constants.size_sprite):
                self.pixels_y += constants.size_sprite


class Bananas:
    """
    This class create a banana with a random position
    """
    def __init__(self):
        self.pixels_x = random.randint(0, 14) * constants.size_sprite
        self.pixels_y = random.randint(0, 14) * constants.size_sprite
