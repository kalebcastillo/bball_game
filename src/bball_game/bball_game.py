import sys

import pygame

class BballGame:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and resources"""

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Shooting Contest")
    
    def run_game(self):
        """Start the main loop for game"""
        while True:
            # Watch for KB/M events, add quit logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            # Make the most recently drawn screen visible.
            pygame.display.flip()