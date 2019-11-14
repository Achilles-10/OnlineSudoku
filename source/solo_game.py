#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from sudoku_grid import SudoCell
from sudoku_generate import *
from success_window import *
from pause_window import *
box = []
for i in range(1,10):
		for j in range(1,10):
			extra_x = int((j - 1)/ 3)
			extra_y = int((i - 1)/ 3)
			if i == 1 and j == 1:
				locals()['cell' + str(i) + '_' + str(j)] = SudoCell(64 + (j - 1)*30 + extra_x, 150 + (i - 1) * 30 + extra_y, [i,j], 0, 1)
			else:
				locals()['cell' + str(i) + '_' + str(j)] = SudoCell(64 + (j - 1)*30 + extra_x, 150 + (i - 1) * 30 + extra_y, [i,j], 0, 0)
			box.append(locals()['cell' + str(i) + '_' + str(j)])
def solo_game(screen, background, bg_color, difficulty, username):
	global current_place
	pygame.init()
	clock = pygame.time.Clock()
	# screen = pygame.display.set_mode((800,500),0,32) #window size
	start_time = pygame.time.get_ticks()
	screen.fill((230,230,230))
	pygame.display.set_caption("Solo Game")
	#loading for coming 
	font = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font.render("Loading ...",True,(50,150,255))#设定文本与颜色
	time = '0.000'
	text_time = font.render(time, True, (50,150,255))
	time_position = text_time.get_rect(center = (background.get_width()/2, 25))
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	textposition = text.get_rect(center = center)
	background.blit(text_time, time_position)
	background.blit(text, textposition)#add text to background according to coordiante
	screen.blit(background,(0,0))
	pygame.display.flip()
	button_pause = Button('Graphs/pause_btn_on.png','Graphs/pause_btn_off.png',(375,25))
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	sudo_result = sudoku_generate_backtracking()
	dibble_sudo_result = sudoku_puzzle_dibble(sudo_result, difficulty)
	full_sudo = [[],[],[],[],[],[],[],[],[]]
	half_sudo = [[],[],[],[],[],[],[],[],[]]
	holes  = 0
	for i in range(0,9):
		full_sudo[i] = sudo_result[i*9 : i * 9 + 9].copy() 
		half_sudo[i] = dibble_sudo_result[i*9 : i * 9 + 9].copy() 
	# print(half_sudo)
	# print(full_sudo)
	for cell in box:
		cell.text = ''
		cell.lock = 0

	for cell in box:
		if half_sudo[cell.location[0] - 1][cell.location[1] - 1] != 0:
			cell.text = str(half_sudo[cell.location[0] - 1][cell.location[1] - 1])
			cell.lock = 1
		else:
			holes += 1
	general_pause_time = pygame.time.get_ticks()-start_time
		# print('(',cell.location[0],',', cell.location[1],'):', cell.text)
		
	while True:
		pygame.display.set_caption("Solo Game")
		seconds = (pygame.time.get_ticks()-start_time - general_pause_time)/1000
		time = str(round(seconds, 2))
		text_time = font.render(time, True, (50,150,255))
		background.blit(text_time, time_position)
		button_back.render(screen)
		button_pause.render(screen)
		screen.blit(background, (0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				background.fill(bg_color)
				return
			if event.type == pygame.MOUSEBUTTONDOWN and button_pause.isOver():
				before_time = pygame.time.get_ticks()
				background.fill(bg_color)
				pause_window(screen, background, bg_color)
				after_time = pygame.time.get_ticks()
				pause_time = after_time - before_time
				general_pause_time += pause_time
			if event.type == pygame.KEYDOWN:
				for cell in box:
					if cell.active:
						current_place = cell.location.copy()
				for cell in box:
					cell.handle_event(event, current_place)
				if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
					for cell in box:
						cell.handle_event(event, current_place)
		
		is_full = True
		for cell in box:
			if cell.text == '':
				is_full = False
		
		if is_full:
			user_ans = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
			for cell in box:
				user_ans[cell.location[0] - 1][cell.location[1] - 1] = int(cell.text)
			if user_ans == full_sudo:
				background.fill(bg_color)
				success_window(screen,background,bg_color,seconds, username, holes, difficulty)
				return


		background.fill(bg_color)
		background.blit(text_time, time_position)
		for cell in box:
			cell.draw(screen, background)

		button_pause.render(screen)
		button_back.render(screen)
		pygame.display.flip()
		clock.tick(30)