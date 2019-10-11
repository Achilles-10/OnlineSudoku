#!/usr/bin/python3
# -*- conding:utf-8 -*-
import sys
import pygame

class Button(object):
    def __init__(self, upimage, downimage,position):
        #upload image of button up
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        #upload image of button down
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        #acquire position
        self.position = position

    def isOver(self):#decide if the mouse is on the button
        #get the position of the mouse
        point_x,point_y = pygame.mouse.get_pos()
        #x & y is the position of the image
        x, y = self. position
        #w & h is image's width and height
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y #return True or False

    def render(self,screen):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            #if mouse is on the image, show imagedown
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            #else show image up
            screen.blit(self.imageUp, (x-w/2, y-h/2))