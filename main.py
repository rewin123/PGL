import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Quad():
	def __init__(self, verts):
		self.verts = verts
		self.edges = [[0,1], [0,3], [1,2], [2,3]]

	def draw_con(self):
		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.verts[vertex])

	def draw(self):
		glBegin(GL_LINES)
		self.draw_con()
		glEnd()

quad = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0] /  display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(0,0,0,0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	quad.draw()
	pygame.display.flip()
	pygame.time.wait(10)
