"""
Mac Gyver game !
this game aims to get Mac Gyver out of the labyrinth.

Script Python
Files : gyverlabyrinthe.py, constants.py, classes.py
Dir: macgyver_ressources
"""

import pygame
from pygame.locals import QUIT, KEYDOWN, K_F1, K_ESCAPE, K_RIGHT, \
                          K_LEFT, K_DOWN, K_UP, K_RETURN, \
                          MOUSEBUTTONDOWN
from classes import Labyrinth, MacGyver
import constants as cst


# main programme
def main():
    pygame.init()

    # Open the Pygame window (square : width=heigh)
    window = pygame.display.set_mode((cst.SIZE_WINDOW, cst.SIZE_WINDOW))
    # Icon
    icon = pygame.image.load(cst.IMAGE_ICON)
    pygame.display.set_icon(icon)
    # Title
    pygame.display.set_caption(cst.TITLE_WINDOW)
    # Font
    font = pygame.font.SysFont("Comicsansms", 20)

    # Main loop
    main_loop = True
    while main_loop:
        # Variables home, game
        home = True
        game = False
        end_game = False

        # Home loop
        while home:
            # Limitation of the loop speed
            pygame.time.Clock().tick(30)

            # Display and loading of the home screen
            home = pygame.image.load(cst.IMAGE_HOME).convert()
            window.blit(home, (0, 0))

            # Refreshment
            pygame.display.flip()

            # Event management of the home page
            for event in pygame.event.get():
                # home to False if the user QUIT
                if (event.type == QUIT or event.type == KEYDOWN
                        and event.key == K_ESCAPE):
                    home = False
                    main_loop = False

                elif (event.type == KEYDOWN and event.key == K_F1
                        or event.type == MOUSEBUTTONDOWN and
                        event.button == 1):
                    # home to False and game to True
                    home = False
                    game = True

                    # Display and loading of the background
                    gm_bck = pygame.image.load(cst.IMAGE_GAME_BCKG).convert()
                    window.blit(gm_bck, (0, 0))

                    # Display and loading of the labyrinth
                    labyrinth = Labyrinth(cst.FILE_LABYRINTH)
                    labyrinth.create()
                    # Generate a random position for the objects
                    labyrinth.objects_pos()
                    # And display and loading images
                    labyrinth.display(window)

                    # Mac Gyver loading
                    macgyver = MacGyver(labyrinth)

        # Game loop
        while game:
            # Limitation of the loop speed
            pygame.time.Clock().tick(30)

            # Event management of the game screen
            for event in pygame.event.get():
                # If the user wants to quit the game
                if event.type == QUIT:
                    # Game to False and main_loop to False
                    game = False
                    main_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        # If the user press to escape, he returns
                        # to the main screen
                        game = False
                        home = True
                    # MacGyver's movements
                    elif event.key == K_UP and macgyver.win is None:
                        macgyver.move('top', labyrinth.objects)
                    elif event.key == K_RIGHT and macgyver.win is None:
                        macgyver.move('right', labyrinth.objects)
                    elif event.key == K_DOWN and macgyver.win is None:
                        macgyver.move('down', labyrinth.objects)
                    elif event.key == K_LEFT and macgyver.win is None:
                        macgyver.move('left', labyrinth.objects)

            macgyver.take_object(labyrinth.objects)
            # Display with new positions
            window.blit(gm_bck, (0, 0))
            window.blit(macgyver.himself, (macgyver.x, macgyver.y))
            labyrinth.display(window)
            pygame.draw.rect(window, (0, 0, 0),
                             (cst.SIZE_WINDOW - 60, 0, 60, 30))
            window.blit(font.render("{}/3".format(macgyver.counter),
                        True, (241, 248, 247)), (cst.SIZE_WINDOW - 45, 0))
            # Refreshment
            pygame.display.flip()

            # win is True or False
            if macgyver.win is not None:
                game = False
                end_game = True
                # win is True if Mac Gyver has all objects
                if macgyver.win is True:
                    home = pygame.image.load(cst.IMAGE_WIN).convert()
                # win is False if Mac Gyver has not all objects
                elif macgyver.win is False:
                    home = pygame.image.load(cst.IMAGE_LOSE).convert()
                    # Wait 1s
                    pygame.time.delay(1000)

        while end_game:
            # Limitation of the loop speed
            pygame.time.Clock().tick(30)
            window.blit(home, (0, 0))
            # Refreshment
            pygame.display.flip()

            # Event management of the end_game page
            for event in pygame.event.get():
                # main_loop to False and end_game to False if the user QUIT
                if event.type == QUIT:
                    end_game = False
                    main_loop = False
                # home to True and end_game to False if the user wants
                # to return to the home screen
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        home = True
                        end_game = False
                    elif event.key == K_RETURN:
                        end_game = False
                        game = True


if __name__ == "__main__":
    main()
