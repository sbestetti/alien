"""Alien invasion game"""

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    """Initialize pygame, create game window and start main loop"""
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()

    while True:
        """Main game loop"""

        """Events monitor"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        """Screen re-drawing"""
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
