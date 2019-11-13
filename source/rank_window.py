import sys
import pygame
from Button import Button
import json

def rank_window(screen, background, bg_color, seconds, username, holes, difficulty):
	screen.fill((230,230,230))
	rank_sheet = Button('Graphs/rank_sheet.png', 'Graphs/rank_sheet.png', (200,325))
	sheet_position = (200,250)
	font = pygame.font.Font('Calib.ttf',30)#设定字体
	text = font.render("Rank",True,(50,150,255))#设定文本与颜色
	center = (background.get_width()/2, background.get_height()/2-100)#get the corrdinates of the center
	textposition = text.get_rect(center = center)
	button_back = Button('Graphs/back_btn_on.png','Graphs/back_btn_off.png',(25,25))

	if difficulty == 1:
		pygame.display.set_caption("Rank for easy")
		with open('rank_for_easy.json') as file:
			dictionary_of_records = json.load(file)
	elif difficulty == 2:
		pygame.display.set_caption("Rank for medium")
		with open('rank_for_medium.json') as file:
			dictionary_of_records = json.load(file)
	else:
		pygame.display.set_caption("Rank for hard")
		with open('rank_for_hard.json') as file:
			dictionary_of_records = json.load(file)
	#loading for coming 
	list_of_records = dic_to_list(dictionary_of_records)
	list_of_records.append((username, seconds/holes))
	sorted_list_of_records = sorted(list_of_records,key=lambda t:t[1])
	while len(sorted_list_of_records) > 5:
		sorted_list_of_records.pop()
	#list改成dict，将记录写回文档
	dictionary_of_records = list_to_dic(list_of_records)
	if difficulty == 1:
		with open('rank_for_easy.json', 'w') as file:
			json.dump(dictionary_of_records,file)
	elif difficulty == 2:
		with open('rank_for_medium.json', 'w') as file:
			json.dump(dictionary_of_records,file)
	else:
		with open('rank_for_hard.json', 'w') as file:
			json.dump(dictionary_of_records,file)
	
	names = []
	times = []
	names_render = []
	times_render = []

	for tuple in sorted_list_of_records:
		names.append(tuple[0])
		times.append(str(round(tuple[1], 2)))
	for name in names:
		names_render.append(font.render(name, True, (0,0,255)))

	for time in times:
		times_render.append(font.render(time, True, (0,0,255)))

	base_height = 230
	while True:
		i = 0
		for time_render in times_render:
			background.blit(time_render, (275, base_height + i * 50))
			i += 1
		i = 0
		for name_render in names_render:
			background.blit(name_render, (75, base_height + i * 50))
			i += 1

		background.blit(text, textposition)#add text to background according to coordiante
		button_back.render(screen)
		rank_sheet.render(screen)
		screen.blit(background,(0,0))

		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and button_back.isOver():
				background.fill(bg_color)
				return
			


		button_back.render(screen)
		rank_sheet.render(screen)		
		pygame.display.flip()

def dic_to_list(dictionary):
	list_of_tuple = []
	for k,v in dictionary.items():
		list_of_tuple.append((k,v))

	return list_of_tuple

def list_to_dic(list):
	dictionary = {}
	for tuple in list:
		dictionary[tuple[0]] = tuple[1]

	return dictionary