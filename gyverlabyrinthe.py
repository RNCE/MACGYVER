"""
Mac Gyver game !
this game aims to get Mac Gyver out of the labyrinth.

Script Python
Files : gyverlabyrinthe.py, constantes.py, classes.py
Dir: macgyver_ressources
"""

import pygame
from pygame.locals import *

from classes import Labyrinth, MacGyver
from constants import *


# main programme
def main():
	pygame.init()

	# Open the Pygame window (square : width=heigh)
	window = pygame.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))
	# Icon
	icon = pygame.image.load(IMAGE_ICON)
	pygame.display.set_icon(icon)
	# Title
	pygame.display.set_caption(TITLE_WINDOW)

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
			home = pygame.image.load(IMAGE_HOME).convert()
			window.blit(home, (0,0))

			# Refreshment
			pygame.display.flip()

			# Event management of the home page
			for event in pygame.event.get():
				# home to False if the user QUIT
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					home = False
					main_loop = False

				elif event.type == KEYDOWN and event.key == K_F1:
					# home to False and game to True 
					home = False
					game = True

					# Display and loading of the background
					game_background = pygame.image.load(IMAGE_GAME_BACKGROUND).convert()
					window.blit(game_background, (0,0))

					# Display and loading of the labyrinth
					labyrinth = Labyrinth(FILE_LABYRINTH)
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
						# If the user press to escape, he returns to the main screen
						game = False
						home = True
					# MacGyver's movements
					elif event.key == K_UP:
						macgyver.move('top', labyrinth.objects)
					elif event.key == K_RIGHT:
						macgyver.move('right', labyrinth.objects)
					elif event.key == K_DOWN:
						macgyver.move('down', labyrinth.objects)
					elif event.key == K_LEFT:
						macgyver.move('left', labyrinth.objects)

			macgyver.take_object(labyrinth.objects)

			if macgyver.alive and macgyver.winner == True:
				game = False
				end_game = True
			# Display with new positions
			window.blit(game_background, (0,0))
			labyrinth.display(window)
			window.blit(macgyver.himself, (macgyver.x, macgyver.y))

			# Refreshment
			pygame.display.flip()

		while end_game:
			# Limitation of the loop speed
			pygame.time.Clock().tick(30)

			# Display and loading of the home screen
			home = pygame.image.load(IMAGE_END).convert()
			window.blit(home, (0,0))

			# Refreshment
			pygame.display.flip()

			# Event management of the home page
			for event in pygame.event.get():
				# home to False if the user QUIT
				if event.type == QUIT:
					end_game = False
					main_loop = False
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					home = True
					end_game = False


if __name__=="__main__":
	main()