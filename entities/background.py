import pygame

class Background:
    def __init__(self):
        self.image_path = "assets/images/background.png"
        self.background_image = pygame.image.load(self.image_path)
    
    def display_background(self, screen):
        screen.blit(self.background_image, (0,0))
