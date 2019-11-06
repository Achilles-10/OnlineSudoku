#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from sudoku_grid import SudoCell
from sudoku_generate import *
from success_window import *
from pause_window import *
def solo_game(screen, background, bg_color, difficulty, username):
	#create cells
	cell1_1 = SudoCell(64,200,[1,1],0,1)
	cell1_2 = SudoCell(94,200,[1,2],0,0)
	cell1_3 = SudoCell(124,200,[1,3],0,0)
	cell1_4 = SudoCell(155,200,[1,4],0,0)
	cell1_5 = SudoCell(185,200,[1,5],0,0)
	cell1_6 = SudoCell(215,200,[1,6],0,0)
	cell1_7 = SudoCell(246,200,[1,7],0,0)
	cell1_8 = SudoCell(276,200,[1,8],0,0)
	cell1_9 = SudoCell(306,200,[1,9],0,0)
	
	cell2_1 = SudoCell(64,230,[2,1],0,0)
	cell2_2 = SudoCell(94,230,[2,2],0,0)
	cell2_3 = SudoCell(124,230,[2,3],0,0)
	cell2_4 = SudoCell(155,230,[2,4],0,0)
	cell2_5 = SudoCell(185,230,[2,5],0,0)
	cell2_6 = SudoCell(215,230,[2,6],0,0)
	cell2_7 = SudoCell(246,230,[2,7],0,0)
	cell2_8 = SudoCell(276,230,[2,8],0,0)
	cell2_9 = SudoCell(306,230,[2,9],0,0)

	cell3_1 = SudoCell(64,260,[3,1],0,0)
	cell3_2 = SudoCell(94,260,[3,2],0,0)
	cell3_3 = SudoCell(124,260,[3,3],0,0)
	cell3_4 = SudoCell(155,260,[3,4],0,0)
	cell3_5 = SudoCell(185,260,[3,5],0,0)
	cell3_6 = SudoCell(215,260,[3,6],0,0)
	cell3_7 = SudoCell(246,260,[3,7],0,0)
	cell3_8 = SudoCell(276,260,[3,8],0,0)
	cell3_9 = SudoCell(306,260,[3,9],0,0)
	
	cell4_1 = SudoCell(64,291,[4,1],0,0)
	cell4_2 = SudoCell(94,291,[4,2],0,0)
	cell4_3 = SudoCell(124,291,[4,3],0,0)
	cell4_4 = SudoCell(155,291,[4,4],0,0)
	cell4_5 = SudoCell(185,291,[4,5],0,0)
	cell4_6 = SudoCell(215,291,[4,6],0,0)
	cell4_7 = SudoCell(246,291,[4,7],0,0)
	cell4_8 = SudoCell(276,291,[4,8],0,0)
	cell4_9 = SudoCell(306,291,[4,9],0,0)
	
	cell5_1 = SudoCell(64,321,[5,1],0,0)
	cell5_2 = SudoCell(94,321,[5,2],0,0)
	cell5_3 = SudoCell(124,321,[5,3],0,0)
	cell5_4 = SudoCell(155,321,[5,4],0,0)
	cell5_5 = SudoCell(185,321,[5,5],0,0)
	cell5_6 = SudoCell(215,321,[5,6],0,0)
	cell5_7 = SudoCell(246,321,[5,7],0,0)
	cell5_8 = SudoCell(276,321,[5,8],0,0)
	cell5_9 = SudoCell(306,321,[5,9],0,0)

	cell6_1 = SudoCell(64,351,[6,1],0,0)
	cell6_2 = SudoCell(94,351,[6,2],0,0)
	cell6_3 = SudoCell(124,351,[6,3],0,0)
	cell6_4 = SudoCell(155,351,[6,4],0,0)
	cell6_5 = SudoCell(185,351,[6,5],0,0)
	cell6_6 = SudoCell(215,351,[6,6],0,0)
	cell6_7 = SudoCell(246,351,[6,7],0,0)
	cell6_8 = SudoCell(276,351,[6,8],0,0)
	cell6_9 = SudoCell(306,351,[6,9],0,0)

	cell7_1 = SudoCell(64,382,[7,1],0,0)
	cell7_2 = SudoCell(94,382,[7,2],0,0)
	cell7_3 = SudoCell(124,382,[7,3],0,0)
	cell7_4 = SudoCell(155,382,[7,4],0,0)
	cell7_5 = SudoCell(185,382,[7,5],0,0)
	cell7_6 = SudoCell(215,382,[7,6],0,0)
	cell7_7 = SudoCell(246,382,[7,7],0,0)
	cell7_8 = SudoCell(276,382,[7,8],0,0)
	cell7_9 = SudoCell(306,382,[7,9],0,0)
	
	cell8_1 = SudoCell(64,412,[8,1],0,0)
	cell8_2 = SudoCell(94,412,[8,2],0,0)
	cell8_3 = SudoCell(124,412,[8,3],0,0)
	cell8_4 = SudoCell(155,412,[8,4],0,0)
	cell8_5 = SudoCell(185,412,[8,5],0,0)
	cell8_6 = SudoCell(215,412,[8,6],0,0)
	cell8_7 = SudoCell(246,412,[8,7],0,0)
	cell8_8 = SudoCell(276,412,[8,8],0,0)
	cell8_9 = SudoCell(306,412,[8,9],0,0)

	cell9_1 = SudoCell(64,442,[9,1],0,0)
	cell9_2 = SudoCell(94,442,[9,2],0,0)
	cell9_3 = SudoCell(124,442,[9,3],0,0)
	cell9_4 = SudoCell(155,442,[9,4],0,0)
	cell9_5 = SudoCell(185,442,[9,5],0,0)
	cell9_6 = SudoCell(215,442,[9,6],0,0)
	cell9_7 = SudoCell(246,442,[9,7],0,0)
	cell9_8 = SudoCell(276,442,[9,8],0,0)
	cell9_9 = SudoCell(306,442,[9,9],0,0)
	box = [cell1_1, cell1_2, cell1_3, cell1_4, cell1_5, cell1_6, cell1_7, cell1_8, cell1_9,
		   cell2_1, cell2_2, cell2_3, cell2_4, cell2_5, cell2_6, cell2_7, cell2_8, cell2_9,
		   cell3_1, cell3_2, cell3_3, cell3_4, cell3_5, cell3_6, cell3_7, cell3_8, cell3_9,
		   cell4_1, cell4_2, cell4_3, cell4_4, cell4_5, cell4_6, cell4_7, cell4_8, cell4_9,
		   cell5_1, cell5_2, cell5_3, cell5_4, cell5_5, cell5_6, cell5_7, cell5_8, cell5_9,
		   cell6_1, cell6_2, cell6_3, cell6_4, cell6_5, cell6_6, cell6_7, cell6_8, cell6_9,
		   cell7_1, cell7_2, cell7_3, cell7_4, cell7_5, cell7_6, cell7_7, cell7_8, cell7_9,
		   cell8_1, cell8_2, cell8_3, cell8_4, cell8_5, cell8_6, cell8_7, cell8_8, cell8_9,
		   cell9_1, cell9_2, cell9_3, cell9_4, cell9_5, cell9_6, cell9_7, cell9_8, cell9_9]

	#initiate the window
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
	#create the buttons
	button_pause = Button('Graphs/pause_btn_on.png','Graphs/pause_btn_off.png',(375,25))
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	sudo_result = sudoku_generate_backtracking()# create the sudoku
	dibble_sudo_result = sudoku_puzzle_dibble(sudo_result, difficulty)#dig holes
	full_sudo = [[],[],[],[],[],[],[],[],[]]
	half_sudo = [[],[],[],[],[],[],[],[],[]]
	holes  = 0
	for i in range(0,9):
		full_sudo[i] = sudo_result[i*9 : i * 9 + 9].copy() 
		half_sudo[i] = dibble_sudo_result[i*9 : i * 9 + 9].copy() 
	# print(half_sudo)
	# print(full_sudo)
	for cell in box:
		#load the numbers of the sudoku in to 81 cells
		cell.rect.y -= 50
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

		#handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				background.fill(bg_color)
				return
			if event.type == pygame.MOUSEBUTTONDOWN and button_pause.isOver():
				#if click on pause button
				before_time = pygame.time.get_ticks()
				background.fill(bg_color)
				pause_window(screen, background, bg_color)
				after_time = pygame.time.get_ticks()
				pause_time = after_time - before_time
				general_pause_time += pause_time#make sure the time is correct
			if event.type == pygame.KEYDOWN:
				#accept keyboard events to adjust the cells' parameters
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
			#decide if game has finished or not
			user_ans = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
			for cell in box:
				user_ans[cell.location[0] - 1][cell.location[1] - 1] = int(cell.text)
			if user_ans == full_sudo:
				#if finished, go to success window
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