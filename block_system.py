import pygame
from pygame.locals import *
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Quad():
	def __init__(self, verts):
		self.verts = verts
		self.edges = [[0,1,2],[2,3,0]]

	def draw_con(self):
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.verts[vertex])

	def draw(self):
		glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1,0,0))
		glBegin(GL_TRIANGLES)
		self.draw_con()
		glEnd()


class Cube():
	def __init__(self):
		self.quad1 = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])
		self.quad2 = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])
		self.quad3 = Quad([[-1,1,1], [-1,-1,1], [1,-1,1], [1,1,1]])
		self.quad4 = Quad([[1,1,-1], [1,-1,-1], [1,-1,1], [1,1,1]])
		self.quad5 = Quad([[1,1,-1], [1,1,1], [-1,1,1], [-1,1,-1]])
		self.quad6 = Quad([[1,-1,-1], [1,-1,1], [-1,-1,1], [-1,-1,-1]])
		
		
	def draw(self):
		self.quad1.draw() 
		self.quad2.draw()
		self.quad3.draw()
		self.quad4.draw()
		self.quad5.draw()
		self.quad6.draw()
		