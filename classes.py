"""
Mac Gyver Game classes 
"""

import pygame
from pygame.locals import *
from constants import *

class Labyrinth:
	# This class allows you to create a labyrinth from a text file
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = []

	def create(self):
		# Creating a list from the text file
		# Open the file
		with open(self.fichier, "r") as fichier:
			structure_lab = []
			# The lines of the file are scanned
			for line in fichier:
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

	def display(self, window):
		# This function allows to display the labyrinth according to the file
		# Images loading
		wall = pygame.image.load(IMAGE_GAME_WALL).convert()
		start = pygame.image.load(IMAGE_GAME_START).convert()
		end = pygame.image.load(IMAGE_GAME_END).convert_alpha()

		# Scan list
		numb_line = 0
		for line in self.structure:
			# Scan lists of lines
			numb_box = 0
			for sprite in line:
				# Position calculation
				x = numb_box * SIZE_SPRITE
				y = numb_line * SIZE_SPRITE
				if sprite == 'w':
					window.blit(wall, (x,y))
				elif sprite == 's':
					window.blit(start, (x,y))
				elif sprite == 'e':
					window.blit(end, (x,y))
				numb_box += 1
			numb_line += 1


class MacGyver:
	# MacGyver class
	def __init__(self, str_labyrinth):
		# MacGyver image
		self.himself = pygame.image.load(IMAGE_GAME_GYVER).convert_alpha()
		# initial position
		self.box_x = 0
		self.box_y = 0
		self.x = 0
		self.y = 0
		# Structure du labyrinth
		self.str_labyrinth = str_labyrinth

	def move(self, direction):
		# Method for changing position
		# Up move
		if direction == 'top':
			# Avoids going over the scren
			if self.box_y > 0:
				# Check that it is not a wall
				if self.str_labyrinth.structure[self.box_y-1][self.box_x] != 'w':
					# One box move
					self.box_y -= 1
					# Convert in pixels
					self.y = self.box_y * SIZE_SPRITE
		# Move to the right
		elif direction == 'right':
			if self.box_x < (NUMBER_SPRITE - 1):
				if self.str_labyrinth.structure[self.box_y][self.box_x+1] != 'w':
					self.box_x += 1
					self.x = self.box_x * SIZE_SPRITE
		# Down move
		elif direction == 'down':
			if self.box_y < (NUMBER_SPRITE - 1):
				if self.str_labyrinth.structure[self.box_y+1][self.box_x] != 'w':
					self.box_y += 1
					self.y = self.box_y * SIZE_SPRITE
		# Move to the left
		elif direction == 'left':
			if self.box_x > 0:
				if self.str_labyrinth.structure[self.box_y][self.box_x-1] != 'w':
					self.box_x -= 1
					self.x = self.box_x * SIZE_SPRITE