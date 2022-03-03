import pygame
from constants.constants import Constants
from constants.constants import Colors

pygame.init()
screen = pygame.display.set_mode((Constants.HEIGHT, Constants.HEIGHT))
background = Colors.GRAY

running = True
while running:
    for event in pygame.event.get():
        # print(event) 
        if event.type == pygame.QUIT:
            running = False

        screen.fill(background)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                background = Colors.RED
            if event.key == pygame.K_LEFT:
                background = Colors.GREEN



        # keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_RIGHT]:
        #     background = Colors.RED
        
        
        pygame.display.update()


pygame.quit()
