#!/usr/bin/python3
# -*- conding:utf-8 -*-
import pygame
import sys
#用于提示登陆中出现的错误和问题，在套接字之后修改较好
def popupwindow(message):
	while True:
		pygame.display.set_caption(message)
		screen = pygame.display.set_mode((400,500),0,32)
		background = pygame.Surface(screen.get_size())#draw the background
		bg_color = (230,230,230)#designate the background's color
		background.fill(bg_color)
		center = (background.get_width()/2, background.get_height()/2)
		font = pygame.font.Font('Calib.ttf',20)
		text = font.render(message,True,(50,150,255))
		position = text.get_rect(center = center)
		background.blit(text, position)
		screen.blit(background,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()