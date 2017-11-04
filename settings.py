class Settings:
    """Class to store all game settings"""

    def __init__(self):
        """Screen settings"""
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)

        """Ship settings"""
        self.ship_speed_factor = 4.00

        """Bullet settings"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
