import pygame as pygame
#用于提供文本输入框
#被需要文本框输入的函数调用：register_window和login_window

pygame.init()
# screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
full_keyboard_allowed_input = [pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,
                               pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9,
                               pygame.K_KP0,pygame.K_KP1,pygame.K_KP2,pygame.K_KP3,pygame.K_KP4,
                               pygame.K_KP5,pygame.K_KP6,pygame.K_KP7,pygame.K_KP8,pygame.K_KP9,
                               pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,
                               pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,
                               pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z,
                               pygame.K_COMMA,pygame.K_PERIOD,pygame.K_SLASH,pygame.K_SEMICOLON,pygame.K_QUOTE,pygame.K_LEFTBRACKET,
                               pygame.K_RIGHTBRACKET,pygame.K_BACKSLASH,pygame.K_BACKQUOTE,pygame.K_MINUS,pygame.K_EQUALS]


class InputBox:

    def __init__(self, x, y, w, h, safemode, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.original_text = text
        self.safemode = safemode
        self.appearance_text = []

    def handle_event(self, event):
        if self.active and self.text == self.original_text:
            #when user click the box for the first time
            self.text = ''
        if self.active:
            #change the color of the box
            self.color = COLOR_ACTIVE
        else:
            self.color = COLOR_INACTIVE
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                #clear the box
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                #delet on charcter
                self.text = self.text[:-1]
            elif event.key in full_keyboard_allowed_input and len(self.text) < 16:
                #add one character
                self.text += event.unicode
            # Re-render the text.
        if self.safemode and self.text != self.original_text:
            self.appearance_text = '*' * len(self.text)
        else:
            self.appearance_text = self.text   
        self.txt_surface = FONT.render(self.appearance_text, True, self.color)
    


    def draw(self, screen,background):
        # Blit the text.
        pygame.draw.rect(background, self.color, self.rect, 2)
        # text_position = self.txt_surface.get_rect(center = (self.rect.x + self.rect.w / 2 ,self.rect.y + self.rect.h / 2))
        # background.blit(self.txt_surface, text_position)
        # # Blit the rect.
        background.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(background,(0,0))