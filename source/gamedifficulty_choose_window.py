#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from solo_game import solo_game
#登录和注册成功后显示，被register_window和login_window调用
#调用了solo_game和dual_game

def gamedifficulty_choose_window(screen, background, bg_color, username):
	#show this window
	screen.fill(bg_color)
	pygame.display.set_caption("Choose game level")
	#load the buttons
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	button_easy = Button('Graphs/easy_btn_on.png','Graphs/easy_btn_off.png',(200,250))
	button_medium = Button('Graphs/medium_btn_on.png','Graphs/medium_btn_off.png',(200,350))
	button_hard = Button('Graphs/hard_btn_on.png','Graphs/hard_btn_off.png',(200,450))
	font_big = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font_big.render("Choose your game level",True,(50,150,255))#设定文本与颜色
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	textposition = text.get_rect(center = center)
	flag = True
	background.fill(bg_color)

	while flag:
		screen = pygame.display.set_mode((400,500),0,32)
		background.blit(text, textposition)
		screen.blit(background,(0,0))
		button_back.render(screen)
		button_easy.render(screen)
		button_medium.render(screen)
		button_hard.render(screen)
		
		#handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				background.fill(bg_color)
				return
			#according to the choise, enter different level
			if event.type == pygame.MOUSEBUTTONDOWN and button_easy.isOver():
				background.fill(bg_color)
				solo_game(screen, background, bg_color, 1, username)
			if event.type == pygame.MOUSEBUTTONDOWN and button_medium.isOver():
				background.fill(bg_color)
				solo_game(screen, background, bg_color, 2, username)
			if event.type == pygame.MOUSEBUTTONDOWN and button_hard.isOver():
				background.fill(bg_color)
				solo_game(screen, background, bg_color, 3, username)

		pygame.display.update()