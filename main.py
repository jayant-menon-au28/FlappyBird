import pygame
from pygame.locals import *

from constants.display import Display
from entities.ball import Ball
from key_mappings.key_map import KeyMap


def main():

    pygame.init()
    Display.WIN
    Display.CAPTION
    Display.BACKGROUND

    run = True
    while run:
        for event in pygame.event.get():  # lines 16-18 are boilerplate for pygame. 
            if event.type == pygame.QUIT:  # the first event we usually check for is whether the user has quit the game
                run = False

            Display.WIN.fill(Display.BACKGROUND)
        

            if event.type == KEYDOWN:
                if event.key in KeyMap.key_dict:
                    Display.BACKGROUND = KeyMap.key_dict[event.key]

            pygame.display.update()

    pygame.quit()  # if run is False, the while loop will terminate, as will pygame, exiting the game 


if __name__ == "__main__":
    main()










# import pygame
# from pygame.locals import *

# size = 640, 320
# width, height = size
# GREEN = (150, 255, 150)
# RED = (255, 0, 0)

# pygame.init()
# screen = pygame.display.set_mode(size)
# running = True

# ball = pygame.image.load("ball.gif")
# rect = ball.get_rect()
# speed = [2, 2]

# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT: 
#             running = False

#     rect = rect.move(speed)
#     if rect.left < 0 or rect.right > width:
#         speed[0] = -speed[0]
#     if rect.top < 0 or rect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(GREEN)
#     pygame.draw.rect(screen, RED, rect, 1)
#     screen.blit(ball, rect)
#     pygame.display.update()

# pygame.quit()