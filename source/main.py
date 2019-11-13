#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from register_window import register_window
from login_window import login_window
#程序的main函数，调用登录和注册两个函数
def run_game():
	pygame.init()
	
	while True: #main loop for the game
		pygame.display.set_caption("Sudoku World") #window name
		screen = pygame.display.set_mode((400,500),0,32) #window size
		background = pygame.Surface(screen.get_size())#draw the background
		bg_color = (229,229,229)#designate the background's color
		background.fill(bg_color)
		font = pygame.font.Font('Calib.ttf',30)#设定字体
		text = font.render("Welcome to Sudoku World!",True,(50,150,255))#设定文本与颜色
		center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
		textposition = text.get_rect(center = center)
		button_register = Button('Graphs/register_btn_on.png','Graphs/register_btn_off.png',(200,300))
		button_login = Button('Graphs/login_btn_on.png','Graphs/login_btn_off.png',(200,400))
		background.blit(text, textposition)#add text to background according to coordiante
		screen.blit(background,(0,0))#paste backgroud to the screen
		button_register.render(screen)#render the button
		button_login.render(screen)#render the button

		for main_event in pygame.event.get():#event decision
			if main_event.type == pygame.QUIT:
				sys.exit()
			elif (main_event.type == pygame.MOUSEBUTTONDOWN and button_register.isOver() == True):
				register_window(screen,background,bg_color)
			elif (main_event.type == pygame.MOUSEBUTTONDOWN and button_login.isOver() == True):
				login_window(screen,background,bg_color)

		pygame.display.update()	#update the display

run_game()