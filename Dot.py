import pygame as pg
from settings import *

class Dot:
	def __init__(self,x,y,radius = RADIUS,color = BLACK,hover_color = RED,clicked_color = GRAY,option_color = GREEN):
		self.x = x
		self.y = y
		self.radius = radius
		
		self.clicked_color = clicked_color
		self.default_color = self.color = color
		self.hover_color = hover_color
		self.option_color = option_color
		
		self.rect = pg.Rect(x,y,2 * self.radius,2 * self.radius)

		self.is_option = False
		self.is_clicked = False

		self.used = [False,False,False,False]
		self.adjacent_dots = [None,None,None,None]
	
	def make_unactive(self):
		self.is_active = False
		self.color = self.default_color

	def make_option(self):
		self.is_option = True
		self.color = self.option_color
	
	def make_normal(self):
		self.is_option = False
		self.color = self.default_color
	
	def add_adjacent_dot(self,dot):
		self.adjacent_dots.append(dot)

	def hover(self,mouseX,mouseY):
		if not self.is_clicked:
			mouseRect = pg.Rect(mouseX,mouseY,MOUSE_RECT_WIDTH,MOUSE_RECT_HEIGHT)
			if self.rect.colliderect(mouseRect):
				self.color = self.hover_color
			elif self.is_option:
				self.color = self.option_color
			else:
				self.color = self.default_color
	
	def handle_right_click(self,mouseX,mouseY):
		mouseRect = pg.Rect(mouseX,mouseY,MOUSE_RECT_WIDTH,MOUSE_RECT_HEIGHT)
		if self.rect.colliderect(mouseRect):
			self.is_clicked = False
			self.color = self.default_color
			return True
		return False

	def handle_left_click(self,mouseX,mouseY):
		mouseRect = pg.Rect(mouseX,mouseY,MOUSE_RECT_WIDTH,MOUSE_RECT_HEIGHT)
		if self.rect.colliderect(mouseRect):
			self.is_clicked = True
			self.color = self.clicked_color
			return True
		return False

	def draw(self,screen):
		pg.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
