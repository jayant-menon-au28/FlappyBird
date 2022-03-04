import pygame
from pygame.locals import *

from constants.constants import Display
from constants.constants import Colors
from key_mappings.key_map import KeyMap


pygame.init()
screen = pygame.display.set_mode((Display.HEIGHT, Display.HEIGHT))
background = Colors.GRAY
pygame.display.set_caption("Gubbalatha's Game")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(background)

        if event.type == KEYDOWN:
            if event.key in KeyMap.key_dict:
                background = KeyMap.key_dict[event.key]
        caption = "background is " + str(background)
        pygame.display.set_caption(caption)
        pygame.display.update()


pygame.quit()
