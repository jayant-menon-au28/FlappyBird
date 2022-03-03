import pygame
from constants.constants import Constants
from constants.constants import Colors

pygame.init()
screen = pygame.display.set_mode((Constants.HEIGHT, Constants.HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        # print(event) 
        if event.type == pygame.QUIT:
            running = False
        screen.fill(Colors.GRAY)
        pygame.display.update()


pygame.quit()
