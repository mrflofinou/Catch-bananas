#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *

import game
import constants

def main():
    """
    Main function of programm
    """

    dk = game.aracters()
    bananas = game.Bananas()
    pygame.init()
    window = pygame.display.set_mode((450, 450))
    pygame.display.set_caption(constants.title)
    background = pygame.image.load(constants.ground).convert()
    avatar = pygame.image.load(constants.character).convert_alpha()
    picture_banana = pygame.image.load(constants.banana).convert_alpha()
    pygame.key.set_repeat(400, 30)
    start_ticks=pygame.time.get_ticks() #starter tick

    score = 0
    loop = 1
    while loop:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    dk.move('right')
                if event.key == K_LEFT:
                    dk.move('left')
                if event.key == K_UP:
                    dk.move('up')
                if event.key == K_DOWN:
                    dk.move('down')


        window.blit(background, (0, 0))
        window.blit(avatar, (dk.x, dk.y))
        window.blit(picture_banana, (bananas.x, bananas.y))
        pygame.display.flip()
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds

        if seconds>20: # if more than 10 seconds close the game
            break
        if dk.x == bananas.x and dk.y == bananas.y:
            bananas = game.Bananas()
            score += 1

    print("Vous avez {} points".format(score))


if __name__ == "__main__":
    main()
