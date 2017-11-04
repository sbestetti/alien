import sys
import pygame


def check_key_down(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_key_up(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Respond to user input"""
    for event in pygame.event.get():
        """Event monitor"""
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(ship, event)
        elif event.type == pygame.KEYUP:
            check_key_up(ship, event)


def update_screen(screen, ship, ai_settings):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
