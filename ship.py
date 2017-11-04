import pygame


class Ship:
    """Class to represent the player's ship"""

    def __init__(self, screen, ai_settings):

        self.screen = screen
        self.ai_settings = ai_settings

        """Load ship image and set it's rectangle"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        """Center created ships"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        """Half the ship rectangle size used to limit lateral movement"""
        self.half_size = float(self.rect[2] / 2)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.center < (self.screen_rect.right - self.half_size):
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.center > self.half_size:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
