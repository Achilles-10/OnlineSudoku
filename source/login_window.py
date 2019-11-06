#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from input_text_box import InputBox
from confirm_username_password import confirm
from gamedifficulty_choose_window import *
#登录界面，在confirm()上需要等待套接字编程进一步修改，其余内容无误
def login_window(screen,background,bg_color):
	#inite the window
	clock = pygame.time.Clock()
	screen.fill((230,230,230))
	pygame.display.set_caption("Log in") #window name
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	button_confirm = Button('Graphs/confirm_btn_on.png','Graphs/confirm_btn_off.png',(342,415))
	flag = True
	background.fill(bg_color)
	#set the font of the wrods
	font = pygame.font.Font('Calib.ttf',30)#设定字体
	font_small = pygame.font.Font('Calib.ttf',20)
	text = font.render("Log in",True,(50,150,255))#设定文本与颜色
	text_name = font_small.render("User Name:", True, (50,150,255))
	text_password = font_small.render("Password:", True, (50,150,255))
	hint = ''
	text_hint = font_small.render(hint, True, (255,0,0))
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	#set the positions of the text
	textposition = text.get_rect(center = center)
	textposition_name = text.get_rect(center = (110,320))
	textposition_pass = text.get_rect(center = (123,370))
	textposition_hint = text.get_rect(center = (210,290))
	#create 3 enter boxes
	name_box = InputBox(175, 300, 213, 32,0,'Username')
	password_box = InputBox(175, 350, 213, 32,1,'Password')
	input_boxes = [name_box, password_box]
	while flag:
		background.blit(text, textposition)#add text to background
		background.blit(text_name, textposition_name)
		background.blit(text_password, textposition_pass)
		background.blit(text_hint,textposition_hint)	
		button_back.render(screen)#show the button
		button_confirm.render(screen)#show the button
		screen.blit(background,(0,0))#paste background to the screen

		#handle events
		for login_event in pygame.event.get():
			if login_event.type == pygame.QUIT:
				sys.exit()
			if login_event.type == pygame.MOUSEBUTTONDOWN and name_box.rect.collidepoint(login_event.pos):
				#if the mouse click on the name box, activae the name box
				name_box.active = True
				password_box.active = False
				for box in input_boxes:
					box.handle_event(login_event)
			if login_event.type == pygame.MOUSEBUTTONDOWN and password_box.rect.collidepoint(login_event.pos):
				#if the mouse click on password box, activate the password box
				name_box.active = False
				password_box.active = True
				for box in input_boxes:
					box.handle_event(login_event)
			if login_event.type == pygame.MOUSEBUTTONDOWN and \
			password_box.rect.collidepoint(login_event.pos) == False and \
			name_box.rect.collidepoint(login_event.pos) == False and \
			button_back.isOver():
			# if the mouse click on the back button
				name_box.active = False
				password_box.active = False
				# flag = False
				background.fill(bg_color)
				return
			if login_event.type == pygame.MOUSEBUTTONDOWN and \
			password_box.rect.collidepoint(login_event.pos) == False and \
			name_box.rect.collidepoint(login_event.pos) == False and \
			button_confirm.isOver():
			# if the mouse click on the confirm button
				name_box.active = False
				password_box.active = False
				result = confirm(name_box.text, password_box.text, '', 0)
				# print('result= ', result)
				if result == 5:
					hint = 'Wrong password'
					text_hint = font_small.render(hint, True, (255,0,0))
				elif result == 6:
					hint = 'Username doesn\'t exist'
					text_hint = font_small.render(hint, True, (255,0,0))
				elif result == 1:
					background.fill(bg_color)
					gamedifficulty_choose_window(screen, background, bg_color,name_box.text)
					return
				# print(name_box.text)
			if login_event.type == pygame.MOUSEBUTTONDOWN and \
			password_box.rect.collidepoint(login_event.pos) == False and \
			name_box.rect.collidepoint(login_event.pos) == False and \
			button_confirm.isOver() == False and \
			button_back.isOver() == False:
			#the mouse click on the blank place
				name_box.active = False
				password_box.active = False
				for box in input_boxes:
					box.handle_event(login_event)
			if login_event.type == pygame.KEYDOWN:
				for box in input_boxes:
					box.handle_event(login_event)

		background.fill(bg_color)
		background.blit(text, textposition)#add text to background
		background.blit(text_name, textposition_name)
		background.blit(text_password, textposition_pass)
		background.blit(text_hint,textposition_hint)
		#draw boxes
		for box in input_boxes:
			box.draw(screen,background)

		button_back.render(screen)#show the button
		button_confirm.render(screen)#show the button
		pygame.display.flip()	
		clock.tick(30)