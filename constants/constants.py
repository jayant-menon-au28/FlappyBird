import pygame


class Display:
    HEIGHT, WIDTH  = 800, 600
    WIN = pygame.display.set_mode((HEIGHT, WIDTH))

class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)