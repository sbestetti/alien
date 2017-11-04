"""Alien invasion game"""

import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    """Initialize pygame, create game window and start main loop"""
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:
        """Main game loop"""

        for event in pygame.event.get():
            """Event monitor"""
            if event.type == pygame.QUIT:
                sys.exit()

        """Screen re-drawing"""
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()
