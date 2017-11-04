import sys
import pygame


def check_events():
    """Respond to user input"""
    for event in pygame.event.get():
        """Event monitor"""
        if event.type == pygame.QUIT:
            sys.exit()
