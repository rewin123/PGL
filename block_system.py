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

	def move(self,x,y,z):
		for index in range(0, len(self.verts)):
			v = self.verts[index]
			self.verts[index] = [v[0] + x, v[1] + y, v[2] + z]




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


	def move(self,x,y,z):
		self.quad1.move(x,y,z)
		self.quad2.move(x,y,z)
		self.quad3.move(x,y,z)
		self.quad4.move(x,y,z)
		self.quad5.move(x,y,z)
		self.quad6.move(x,y,z)

		
		
	def draw(self):
		self.quad1.draw() 
		self.quad2.draw()
		self.quad3.draw()
		self.quad4.draw()
		self.quad5.draw()
		self.quad6.draw()
