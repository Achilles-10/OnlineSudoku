import sys
import pygame
from Button import Button
from sudoku_grid import SudoCell
pbox = []
for i in range(1,10):
		for j in range(1,10):
			extra_x = int((j - 1)/ 3)
			extra_y = int((i - 1)/ 3)
			locals()['pcell' + str(i) + '_' + str(j)] = SudoCell(64 + (j - 1)*30 + extra_x, 150 + (i - 1) * 30 + extra_y, [i,j], 0, 0)
			pbox.append(locals()['pcell' + str(i) + '_' + str(j)])
def pause_window(screen, background, bg_color):
	
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((400,500),0,32)
	screen.fill((230,230,230))
	pygame.display.set_caption("Pause") #window name
	button_start = Button('Graphs/start_btn_on.png','Graphs/start_btn_off.png',(375,25))
	background.fill(bg_color)
	font_big = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font_big.render("Pausing",True,(50,150,255))
	center = (background.get_width()/2, background.get_height()/2-150)#get the corrdinates of the center
	textposition_big = text.get_rect(center = center)

	while True:
		for cell in pbox:
			cell.draw(screen, background)
		# button_back.render(screen)
		background.blit(text, textposition_big)
		screen.blit(background, (0,0))
		button_start.render(screen)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_start.isOver():
				background.fill(bg_color)
				return

		pygame.display.flip()
		clock.tick(30)