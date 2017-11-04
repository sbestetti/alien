import sys
import pygame


def check_events(ship):
    """Respond to user input"""
    for event in pygame.event.get():
        """Event monitor"""
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(screen, ship, ai_settings):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
