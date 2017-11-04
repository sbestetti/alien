"""Alien invasion game"""

import sys
import pygame

from settings import Settings


def run_game():
    """Initialize pygame, create game window and start main loop"""
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")

    while True:
        """Main game loop"""

        for event in pygame.event.get():
            """Event monitor"""
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)

        pygame.display.flip()


run_game()
