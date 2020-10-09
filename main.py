# This is a multiplayer Tic Tac Toe game I made using the module Pygame
# To run the source coude, you need to have python3 and pygame installed on your computer
# If you are on windows, you can simply download this executable file(link is given below) to run it directly on you PC
# Executable file link: https://github.com/ShowmickKar/Tic-Tac-Toe-using-Pygame-Multiplayer-/blob/main/TIC-TAC_Toe_Executable.rar
# I hope you enjoy!

import pygame
import sys

pygame.init()

(width, length) = (590, 590)
background_color = (0, 0, 0)

# Initialized a varible that changes the player after each move
toggle: bool = True

screen = pygame.display.set_mode((width, length))
screen.fill(background_color)
pygame.display.set_caption("TIC TAC TOE using Pygame(Multiplayer)")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INDIGO = (70, 130, 255)
GREEN = (0, 255, 0)


# Initialized attributes of nine squares of the board including their positions and colors
first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))


# Initialize two lists to keep track of the 9 sqares in the game
board_position_name = []
board_position = []

# This list keeps track of all the nine squares and their atributes
board_position_name.extend([0, first, second, third, fourth, fifth, sixth, seventh, eight, ninth])

# This square keeps track of the positions of all of the nine sqaures
board_position.extend([0, [20, 20], [210, 20], [400, 20], [20, 210], [210, 210], [400, 210], [20, 400], [210, 400], [400, 400]])

grid = [0, "", "", "", "", "", "", "", "", ""]

# Determine if someone has won and if so return the winner

def check_win():
	if grid[1] == "X" and grid[5] == "X" and grid[9] == "X":
		return "First Player"
	elif grid[3] == "X" and grid[5] == "X" and grid[7] == "X":
		return "First Player"
	elif grid[1] == "X" and grid[4] == "X" and grid[7] == "X":
		return "First Player"
	elif grid[1] == "X" and grid[2] == "X" and grid[3] == "X":
		return "First Player"
	elif grid[3] == "X" and grid[6] == "X" and grid[9] == "X":
		return "First Player"
	elif grid[7] == "X" and grid[8] == "X" and grid[9] == "X":
		return "First Player"
	elif grid[2] == "X" and grid[5] == "X" and grid[8] == "X":
		return "First Player"
	elif grid[4] == "X" and grid[5] == "X" and grid[6] == "X":
		return "First Player"

	elif grid[1] == "O" and grid[5] == "O" and grid[9] == "O":
		return "Second Player"
	elif grid[3] == "O" and grid[5] == "O" and grid[7] == "O":
		return "Second Player"
	elif grid[1] == "O" and grid[4] == "O" and grid[7] == "O":
		return "Second Player"
	elif grid[1] == "O" and grid[2] == "O" and grid[3] == "O":
		return "Second Player"
	elif grid[3] == "O" and grid[6] == "O" and grid[9] == "O":
		return "Second Player"
	elif grid[7] == "O" and grid[8] == "O" and grid[9] == "O":
		return "Second Player"
	elif grid[2] == "O" and grid[5] == "O" and grid[8] == "O":
		return "Second Player"
	elif grid[4] == "O" and grid[5] == "O" and grid[6] == "O":
		return "Second Player"
	else:
		return "No one"

# Determine if it's a draw
def check_draw():
	# If the remaining moves is zero then two things can happen
	# 1. Either Player 1 or Player 2 has won
	# 2. It's a draw
	# We take care of case when it's not a draw before calling this function
	# That is, if this function return True, it's definitely a draw
	return not remaining_moves


# Setting up a rematch
def setup():
	grid = [None, "", "", "", "", "", "", "", "", ""]
	board_position_name = []
	board_position = []
	board_position_name.extend([None, first, second, third, fourth, fifth, sixth, seventh, eight, ninth])
	board_position.extend([None, [20, 20], [210, 20], [400, 20], [20, 210], [210, 210], [400, 210], [20, 400], [210, 400], [400, 400]])
	return (grid, board_position_name, board_position)

remaining_moves = 9

flag = False

while True:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if flag and event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				flag = False
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
			raise SystemExit

		if pygame.MOUSEBUTTONUP == event.type:
			click_position = pygame.mouse.get_pos()
			for position in range(1, len(board_position_name)):
				if board_position_name[position].collidepoint(click_position):
					if grid[position] != "":
						continue
					elif toggle:
						grid[position] = "X"
					else:
						grid[position] = "O"

					if toggle:
						img = pygame.image.load("cross_icon.png")
						img = pygame.transform.scale(img, (120, 120))
						screen.blit(img, (board_position[position][0] + 27, board_position[position][1] + 27))
						pygame.display.update()
						toggle = False
					else:
						img = pygame.image.load("circle_icon.png")
						img = pygame.transform.scale(img, (120, 120))
						screen.blit(img, (board_position[position][0] + 27, board_position[position][1] + 27))
						pygame.display.update()
						toggle = True

					remaining_moves -= 1
						
		pygame.display.update()

		if check_win() == "First Player":
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface= pygame.image.load("first_player.win.png")
			screen.blit(text_surface, (20, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			print(grid)
			toggle  = not toggle
			(grid, board_position_name, board_position) = setup()
			screen.fill(background_color)
			remaining_moves = 9
			first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
			second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
			third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
			fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
			fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
			sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
			seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
			eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
			ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
			pygame.display.update()
			continue

		if check_win() == "Second Player":
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface = pygame.image.load("second_player_win.png")
			screen.blit(text_surface, (20, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			print(grid)
			toggle  = not toggle
			(grid, board_position_name, board_position) = setup()
			screen.fill(background_color)
			remaining_moves = 9
			first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
			second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
			third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
			fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
			fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
			sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
			seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
			eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
			ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
			pygame.display.update()
			continue

		if check_draw():
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface = pygame.image.load("draw.png")
			screen.blit(text_surface, (20, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			print(grid)
			toggle  = not toggle
			(grid, board_position_name, board_position) = setup()
			screen.fill(background_color)
			remaining_moves = 9
			first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
			second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
			third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
			fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
			fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
			sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
			seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
			eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
			ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))
			pygame.display.update()
			continue

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
			raise SystemExit

	pygame.display.flip()

pygame.quit()
