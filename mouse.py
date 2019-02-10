import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class Mouse():

	def __init__(self, fix_pos = None):
		self.fix_pos = fix_pos
		self.x, self.y = pygame.mouse.get_pos()
		self.dx = 0
		self.dy = 0

	def update_mouse(self):
		if self.fix_pos is not None:
			if pygame.mouse.get_focused():
				x,y = pygame.mouse.get_pos()
				self.dx = x - self.fix_pos[0]
				self.dy = y - self.fix_pos[1]
				self.x = self.fix_pos[0]
				self.y = self.fix_pos[1]
				pygame.mouse.set_pos(self.fix_pos)
			else:
				self.dx = 0
				self.dy = 0
		else:
			x, y = pygame.mouse.get_pos()
			self.dx = x - self.x
			self.dy = y - self.y
			self.x = x
			self.y = y
		
