import sys

import pygame

from settings import Settings
from ship import Ship

class BballGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and resources"""

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Shooting Contest")

        self.ship = Ship(self)

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set background color
        self.bg_color = (193,154,107)
    
    def run_game(self):
        """Start the main loop for game"""
        while True:
            self._check_events()
            self._update_screen()          
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to KB/M events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.rect.x += 1
    
    def _update_screen(self):
         # Redraw screen during each pass
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = BballGame()
    ai.run_game()        