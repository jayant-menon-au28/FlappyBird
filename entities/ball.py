import pygame

class Ball:
    def __init__(self):
        self.image_path = "assets/images/ball.gif"
        self.ball_image = pygame.image.load(self.image_path)