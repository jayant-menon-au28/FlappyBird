import pygame
from entities.background import Background

class Display:
    HEIGHT, WIDTH  = 768, 896
    WIN = pygame.display.set_mode((HEIGHT, WIDTH))
    CAPTION = pygame.display.set_caption("Flappy Bird")
    BACKGROUND = WIN.blit(Background.background_image, (0,0))