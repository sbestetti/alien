import sys
import pygame


def check_events():
    """Respond to user input"""
    for event in pygame.event.get():
        """Event monitor"""
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ship, ai_settings):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
