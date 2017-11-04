import pygame


class Ship:
    """Class to represent the player's ship"""

    def __init__(self, screen):

        self.screen = screen

        """Load ship image and set it's rectangle"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        """Center created ships"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.rect)
