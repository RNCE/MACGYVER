"""
Mac Gyver game !
this game aims to get Mac Gyver out of the labyrinth.

Script Python
Files : gyverlabyrinthe.py, constantes.py, classes.py
Dir: macgyver_ressources
"""

import pygame
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

# Open the Pygame window (square : width=heigh)
window = pygame.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
# Icon
icon = pygame.image.load(IMAGE_ICON)
pygame.display.set_icon(icon)
# Title
pygame.display.set_caption(TITLE_WINDOW)