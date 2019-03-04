"""
Mac Gyver Game classes
"""

import pygame
import constants as cst
import random


class Labyrinth:
    # This class allows you to create a labyrinth from a text file
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.objects = {'needle': [], 'tube': [], 'ether': []}

    def create(self):
        # Creating a list from the text file
        # Open the file
        with open(self.file, "r") as file:
            structure_lab = []
            # The lines of the file are scanned
            for line in file:
                line_lab = []
                # The sprites of line are scanned
                for sprite in line:
                    # "/n" are not taken into account
                    if sprite != '\n':
                        # Adding sprite to the line_lab list
                        line_lab.append(sprite)
                # Adding lign to the structure_lab list
                structure_lab.append(line_lab)
            # struture_lab save
            self.structure = structure_lab

    def rand_pos(self):
        # This method allows to return a list with random positions
        # for x and y
        # Generate a random number between 0 and number of sprite -1
        rand_number_y = random.randint(0, cst.NUMBER_SPRITE-1)
        rand_number_x = random.randint(0, cst.NUMBER_SPRITE-1)
        # Pixel position x and y
        pos_x = 0
        pos_y = 0
        # Check that the element is not a wall
        while self.structure[rand_number_y][rand_number_x] != '0':
            rand_number_y = random.randint(0, cst.NUMBER_SPRITE-1)
            rand_number_x = random.randint(0, cst.NUMBER_SPRITE-1)
        # Calculation of the position in pixels
        pos_x = rand_number_x * cst.SIZE_SPRITE
        pos_y = rand_number_y * cst.SIZE_SPRITE
        position = [pos_x, pos_y]
        # return a random position that is not a wall
        return position

    def objects_pos(self):
        # This method avoids the overlapping of the images
        avoid_overl = []
        i = 0
        for key in self.objects:
            # Browse the dictionary and adds all the positions in
            # the avoid_overl list
            avoid_overl.append(self.rand_pos())
            # Verification of duplicate elements
            while avoid_overl.count(avoid_overl[i]) != 1:
                # If duplicate element, generate a new position
                avoid_overl[i] = self.rand_pos()
            # Add the position to the dictionary
            self.objects[key] = avoid_overl[i]
            i += 1

    def display(self, window):
        # This function allows to display the labyrinth and the objects
        # according to the file
        # Images loading
        wall = pygame.image.load(cst.IMAGE_GAME_WALL).convert()
        end = pygame.image.load(cst.IMAGE_GUARDIAN).convert_alpha()
        needle = pygame.image.load(cst.IMAGE_GAME_NEEDLE).convert()
        tube = pygame.image.load(cst.IMAGE_GAME_TUBE).convert()
        ether = pygame.image.load(cst.IMAGE_GAME_ETHER).convert()

        # Scan list
        numb_line = 0
        for line in self.structure:
            # Scan lists of lines
            numb_box = 0
            for sprite in line:
                # Position calculation
                x = numb_box * cst.SIZE_SPRITE
                y = numb_line * cst.SIZE_SPRITE
                if sprite == 'w':
                    window.blit(wall, (x, y))
                elif sprite == 'e':
                    window.blit(end, (x, y))
                numb_box += 1
            numb_line += 1

        # The images of objects are added to the labyrinth
        for key in self.objects:
            if key == 'needle':
                window.blit(needle,
                            (self.objects['needle'][0],
                                self.objects['needle'][1]))
            elif key == 'tube':
                window.blit(tube,
                            (self.objects['tube'][0],
                                self.objects['tube'][1]))
            elif key == 'ether':
                window.blit(ether,
                            (self.objects['ether'][0],
                                self.objects['ether'][1]))


class MacGyver:
    # MacGyver class
    def __init__(self, str_labyrinth):
        # MacGyver image
        self.himself = pygame.image.load(cst.IMAGE_GYVER).convert_alpha()
        # initial position
        self.box_x = 0
        self.box_y = 0
        self.x = 0
        self.y = 0
        # Labyrinth structure
        self.str_lab = str_labyrinth
        # Macgyver alives
        self.alive = True
        # Macgyver winner
        self.winner = False

    def move(self, direction, objects):
        # Method for changing position
        # Up move
        if direction == 'top':
            # Avoids going over the scren
            if self.box_y > 0:
                # When Mac Gyver is in front of the guard
                # and he has all the objects
                # all objects == objects dictionary empty
                if (self.str_lab.structure[self.box_y-1][self.box_x] == 'e'
                        and not objects):
                    self.winner = True
                # When Mac Gyver is in front of the guard
                # but he hasn't the objects
                elif self.str_lab.structure[self.box_y-1][self.box_x] == 'e':
                    self.himself = \
                            pygame.image.load(cst.GYVER_DEAD).convert_alpha()
                    self.alive = False
                # Check that it is not a wall
                elif self.str_lab.structure[self.box_y-1][self.box_x] != 'w':
                    # One box move
                    self.box_y -= 1
                    # Convert in pixels
                    self.y = self.box_y * cst.SIZE_SPRITE
        # Move to the right
        elif direction == 'right':
            if self.box_x < (cst.NUMBER_SPRITE - 1):
                if (self.str_lab.structure[self.box_y][self.box_x+1] == 'e'
                        and not objects):
                    self.winner = True
                elif self.str_lab.structure[self.box_y][self.box_x+1] == 'e':
                    self.himself = \
                            pygame.image.load(cst.GYVER_DEAD).convert_alpha()
                    self.alive = False
                elif self.str_lab.structure[self.box_y][self.box_x+1] != 'w':
                    self.box_x += 1
                    self.x = self.box_x * cst.SIZE_SPRITE
        # Down move
        elif direction == 'down':
            if self.box_y < (cst.NUMBER_SPRITE - 1):
                if (self.str_lab.structure[self.box_y+1][self.box_x] == 'e'
                        and not objects):
                    self.winner = True
                elif self.str_lab.structure[self.box_y+1][self.box_x] == 'e':
                    self.himself = \
                            pygame.image.load(cst.GYVER_DEAD).convert_alpha()
                    self.alive = False
                elif self.str_lab.structure[self.box_y+1][self.box_x] != 'w':
                    self.box_y += 1
                    self.y = self.box_y * cst.SIZE_SPRITE
        # Move to the left
        elif direction == 'left':
            if self.box_x > 0:
                if (self.str_lab.structure[self.box_y][self.box_x-1] == 'e'
                        and not objects):
                    self.winner = True
                elif self.str_lab.structure[self.box_y][self.box_x-1] == 'e':
                    self.himself = \
                            pygame.image.load(cst.GYVER_DEAD).convert_alpha()
                    self.alive = False
                elif self.str_lab.structure[self.box_y][self.box_x-1] != 'w':
                    self.box_x -= 1
                    self.x = self.box_x * cst.SIZE_SPRITE

    def take_object(self, objects):
        # This method allows to take the objects
        for key, values in list(objects.items()):
            if [self.x, self.y] == values:
                # if the Mac Gyver position corresponds to the position of
                # the object, the object is removed from the dictionary
                objects.pop(key)
            elif [self.x, self.y] == values:
                objects.pop(key)
            elif [self.x, self.y] == values:
                objects.pop(key)
