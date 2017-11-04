"""Alien invasion game"""

import sys
import pygame


def run_game():
    """Initialize pygame, create game window and start main loop"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        """Main game loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
