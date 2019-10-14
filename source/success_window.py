#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from rank_window import *



def success_window(screen, background, bg_color, seconds, username, holes, difficulty):
	clock = pygame.time.Clock()
	screen.fill((230,230,230))
	pygame.display.set_caption("Congratulation!")
	#loading for coming 
	font = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font.render("You Win!",True,(50,150,255))#设定文本与颜色
	time = font.render('time:' + str(seconds),True,(50,150,255))
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	time_center = (background.get_width()/2 - 5, background.get_height()/2-50)
	textposition = text.get_rect(center = center)
	timeposition = text.get_rect(center = time_center)
	

	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	button_rank = Button('Graphs/rank_btn_on.png','Graphs/rank_btn_off.png',(200,350))
	while True:
		background.blit(time, timeposition)
		background.blit(text, textposition)#add text to background according to coordiante
		
		screen.blit(background,(0,0))
		button_rank.render(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				background.fill(bg_color)
				return
			if event.type == pygame.MOUSEBUTTONDOWN and button_rank.isOver():
				background.fill(bg_color)
				rank_window(screen, background, bg_color, seconds, username, holes, difficulty)




		button_back.render(screen)
		pygame.display.flip()
		clock.tick(30)