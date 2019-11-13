#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from solo_game import solo_game
from gamedifficulty_choose_window import*
#登录和注册成功后显示，被register_window和login_window调用
#调用了solo_game和dual_game

def gamemode_choose_window(screen, background, bg_color):
	screen.fill(bg_color)
	screen = pygame.display.set_mode((400,500),0,32)
	pygame.display.set_caption("Choose game mode")
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	button_solo = Button('Graphs/solo_btn_on.png','Graphs/solo_btn_off.png',(200,300))
	button_dual = Button('Graphs/dual_btn_on.png','Graphs/dual_btn_off.png',(200,400))
	font_big = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font_big.render("Choose your game mode",True,(50,150,255))#设定文本与颜色
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	textposition = text.get_rect(center = center)
	flag = True
	background.fill(bg_color)

	while flag:
		background.blit(text, textposition)
		screen.blit(background,(0,0))
		button_back.render(screen)
		button_solo.render(screen)
		button_dual.render(screen)
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				flag = False
				background.fill(bg_color)
			if event.type == pygame.MOUSEBUTTONDOWN and button_solo.isOver():
				background.fill(bg_color)
				gamedifficulty_choose_window(screen, background, bg_color)
			if event.type == pygame.MOUSEBUTTONDOWN and button_dual.isOver():
				print('into dual game')

		pygame.display.update()