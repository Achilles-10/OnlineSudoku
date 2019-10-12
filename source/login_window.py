#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame
from Button import Button
from input_text_box import InputBox
from confirm_username_password import confirm
#登录界面，在confirm()上需要等待套接字编程进一步修改，其余内容无误
def login_window(screen,background,bg_color):
	clock = pygame.time.Clock()
	screen.fill((230,230,230))
	pygame.display.set_caption("Log in") #window name
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))
	button_confirm = Button('Graphs/confirm_btn_on.png','Graphs/confirm_btn_off.png',(342,415))
	flag = True
	background.fill(bg_color)
	font = pygame.font.Font('Calib.ttf',30)#设定字体
	font_small = pygame.font.Font('Calib.ttf',20)
	text = font.render("Log in",True,(50,150,255))#设定文本与颜色
	text_name = font_small.render("User Name:", True, (50,150,255))
	text_password = font_small.render("Password:", True, (50,150,255))
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	textposition = text.get_rect(center = center)
	textposition_name = text.get_rect(center = (110,320))
	textposition_pass = text.get_rect(center = (123,370))
	name_box = InputBox(175, 300, 213, 32,0,'Username')
	password_box = InputBox(175, 350, 213, 32,1,'Password')
	input_boxes = [name_box, password_box]
	while flag:
		background.blit(text, textposition)#add text to background
		background.blit(text_name, textposition_name)
		background.blit(text_password, textposition_pass)	
		button_back.render(screen)#show the button
		button_confirm.render(screen)#show the button
		screen.blit(background,(0,0))#paste background to the screen

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
				flag = False
				background.fill(bg_color)
			if login_event.type == pygame.MOUSEBUTTONDOWN and \
			password_box.rect.collidepoint(login_event.pos) == False and \
			name_box.rect.collidepoint(login_event.pos) == False and \
			button_confirm.isOver():
			# if the mouse click on the confirm button
				name_box.active = False
				password_box.active = False
				flag = confirm(name_box.text, password_box.text, '', 0)
				background.fill(bg_color)
				print(name_box.text)
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
		for box in input_boxes:
			box.draw(screen,background)

		button_back.render(screen)#show the button
		button_confirm.render(screen)#show the button
		pygame.display.flip()	
		clock.tick(30)