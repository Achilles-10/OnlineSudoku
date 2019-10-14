import pygame as pygame

pygame.init()
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = (0,100,255)#pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
orient_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
number_keys = [pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,
              pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,pygame.K_KP8,pygame.K_KP9,
			  pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,
              pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]

class SudoCell:
	def __init__(self, x, y, loca, lock, ini_active):
		self.rect = pygame.Rect(x, y, 30, 30)
		self.num = 0
		self.text = ''
		self.text_surface = FONT.render('', True, COLOR_INACTIVE)
		self.lock = lock
		self.active = ini_active
		self.location = loca
		if self.active:
			self.color = COLOR_ACTIVE
		else:
			self.color = COLOR_INACTIVE

	def handle_event(self, event, current_place):
		if event.type == pygame.KEYDOWN and event.key in orient_keys:
			if self.active:
			#当激活的cell收到移动的命令时，激活位置相应变化

				if event.key == pygame.K_UP and current_place[0] > 1:
					self.active = False
					current_place[0] -= 1
				if event.key == pygame.K_DOWN and current_place[0] < 9:
					self.active = False
					current_place[0] += 1	
				if event.key == pygame.K_LEFT and current_place[1] > 1:
					self.active = False
					current_place[1] -= 1
				if event.key == pygame.K_RIGHT and current_place[1] < 9:
					self.active = False
					current_place[1] += 1
				# print('remove active:', self.location,"->", current_place)
			if self.active == False and self.location == current_place:
				self.active = True
				# print('become active', current_place, self.location)
		if event.type == pygame.KEYDOWN and event.key in number_keys and\
		self.active and len(self.text) == 0 and self.lock == 0:
		#当数字键按下 & cell激活 & cell中空白 时，加入数字
			self.text += event.unicode
			# print(self.text)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and\
		self.active and self.lock == 0:
		#当数字键按下 & cell激活 时，删除数字
			self.text = self.text[:-1]
		if self.active:
			self.color = COLOR_ACTIVE
		else:
			self.color = COLOR_INACTIVE
		

	
	def draw(self, screen, background):
		
		if self.lock == 1:
			self.text_surface = FONT.render(self.text, True, COLOR_ACTIVE)
		else:
			self.text_surface = FONT.render(self.text, True, COLOR_INACTIVE)
		pygame.draw.rect(background, self.color, self.rect, 2)
		text_position = self.text_surface.get_rect(center = (self.rect.x + self.rect.h/2, self.rect.y + self.rect.h/2 + 2))
		background.blit(self.text_surface, text_position)
		screen.blit(background, (0, 0))

