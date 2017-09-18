#! /usr/bin/env python3
# coding: utf-8
import pygame
from pygame.locals import *

from classes import *
from constantes import *

def main():
    """
    Fonction principale du programmes
    """

    dk = Personnage()
    bananes = Bananes()
    pygame.init()
    fenetre = pygame.display.set_mode((450, 450))
    pygame.display.set_caption(titre)
    fond = pygame.image.load(sol).convert()
    avatar = pygame.image.load(perso).convert_alpha()
    image_banane = pygame.image.load(banane).convert_alpha()
    pygame.key.set_repeat(400, 30)
    start_ticks=pygame.time.get_ticks() #starter tick

    gain = 0
    continuer = 1
    while continuer:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    dk.deplacement('droite')
                if event.key == K_LEFT:
                    dk.deplacement('gauche')
                if event.key == K_UP:
                    dk.deplacement('haut')
                if event.key == K_DOWN:
                    dk.deplacement('bas')


        fenetre.blit(fond, (0, 0))
        fenetre.blit(avatar, (dk.x, dk.y))
        fenetre.blit(image_banane, (bananes.x, bananes.y))
        pygame.display.flip()
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds

        if seconds>20: # if more than 10 seconds close the game
            break
        if dk.x == bananes.x and dk.y == bananes.y:
            bananes = Bananes()
            gain += 1

    print("Vous avez {} points".format(gain))


if __name__ == "__main__":
    main()