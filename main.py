import pygame
from pygame.locals import *

from constants.constants import *
from entities.ball import Ball
from key_mappings.key_map import KeyMap



def main():

    pygame.init()
    Display.WIN
    background = Colors.GRAY
    pygame.display.set_caption("Gubbalatha's Game")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            Display.WIN.fill(background)

            ball = Ball()
        

            if event.type == KEYDOWN:
                if event.key in KeyMap.key_dict:
                    background = KeyMap.key_dict[event.key]
            caption = "background is " + str(background)
            pygame.display.set_caption(caption)
            pygame.display.update()

    pygame.quit()


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