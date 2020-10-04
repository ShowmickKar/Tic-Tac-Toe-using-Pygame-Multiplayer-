import pygame
pygame.init()

(width, length) = (590, 590)
background_color = (0, 0, 0)

screen = pygame.display.set_mode((width, length))
screen.fill(background_color)
pygame.display.set_caption("TIC TAC TOE using Pygame(Multiplayer)")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
INDIGO = (70, 130, 255)

first = pygame.draw.rect(screen, WHITE, (20, 20, 170, 170))
second = pygame.draw.rect(screen, WHITE, (210, 20, 170, 170))
third = pygame.draw.rect(screen, WHITE, (400, 20, 170, 170))
fourth = pygame.draw.rect(screen, WHITE, (20, 210, 170, 170))
fifth = pygame.draw.rect(screen, WHITE, (210, 210, 170, 170))
sixth = pygame.draw.rect(screen, WHITE, (400, 210, 170, 170))
seventh = pygame.draw.rect(screen, WHITE, (20, 400, 170, 170))
eight = pygame.draw.rect(screen, WHITE, (210, 400, 170, 170))
ninth = pygame.draw.rect(screen, WHITE, (400, 400, 170, 170))

board_position_name = []
board_position = []
board_position_name.extend([0, first, second, third, fourth, fifth, sixth, seventh, eight, ninth])
board_position.extend([0, [20, 20], [210, 20], [400, 20], [20, 210], [210, 210], [400, 210], [20, 400], [210, 400], [400, 400]])

grid = [0, "", "", "", "", "", "", "", "", ""]


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


def check_draw():
	return not remaining_moves

toggle: bool = True

remaining_moves = 9

while True:
	pygame.time.delay(100)
	for event in pygame.event.get():
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
						board_position_name[position] = pygame.draw.rect(screen, (0, 255, 0), (
							board_position[position][0] + 30, board_position[position][1] + 30, 110, 110))
						toggle = False
					else:
						board_position_name[position] = pygame.draw.circle(screen, (255, 0, 0), (
							board_position[position][0] + 85, board_position[position][1] + 85), int(110 / 2))
						# might use the following line instead
						# board_position_name[position] = pygame.draw.rect(screen, (0, 255, 255), (board_position[position][0] + 30, board_position[position][1] + 30, 110, 110))
						toggle = True

					remaining_moves -= 1
						
		pygame.display.update()

		if check_win() == "First Player":
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface= pygame.image.load("first_player.win.png")
			screen.blit(text_surface, (0, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			pygame.quit()
			quit()
			raise SystemExit

		if check_win() == "Second Player":
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface = pygame.image.load("second_player_win.png")
			screen.blit(text_surface, (0, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			pygame.quit()
			quit()
			raise SystemExit

		if check_draw():
			pygame.time.delay(500)
			screen.fill((0, 0, 0))
			pygame.display.update()
			text_surface = pygame.image.load("draw.png")
			screen.blit(text_surface, (0, 0))
			pygame.display.update()
			pygame.time.delay(1000)
			pygame.quit()
			quit()
			raise SystemExit

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
			raise SystemExit

	pygame.display.flip()

pygame.quit()
