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

quad = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])c
quad1 = Quad([[-1,-1,-1], [1,-1,-1], [-1,1,1], [-1,1,1]])d
quad2 = Quad([[-1,1,www1], [-1,-1,1], [1,-1,1], [1,1,1]])sd
quad3 = Quad([[1,1,-1], [1,-1,-1], [1,-1,1], [1,1,1]])s
quad4 = Quad([[1,1,-1], [1,1,1], [-1,1,1], [-1,1,-1]])c
quad5 = Quad([[1,-1,-1], [1,-1,1], [-1,-1,1], [-1,-1,-1]])sd

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

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]:
		glTranslatef(0,0,5000 / 60 / 60 / 1000 * 10)

	if pressed[pygame.K_s]:
		glTranslatef(0,0,-5000 / 60 / 60 / 1000 * 10)

	if pressed[pygame.K_d]:
		glTranslatef(-5000 / 60 / 60 / 1000 * 10,0,0)

	if pressed[pygame.K_a]:
		glTranslatef(5000 / 60 / 60 / 1000 * 10,0,0)

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	quad.draw()
	quad1.draw()
	quad2.draw()
	quad3.draw()
	quad4.draw()
	quad5.draw()
	pygame.display.flip()
	pygame.time.wait(10)
