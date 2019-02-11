import pygame
from pygame.locals import *
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from camera import Camera
from mouse import Mouse

camera = Camera()

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

quad = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])
quad1 = Quad([[-1,-1,-1], [1,-1,-1], [1,1,-1], [-1,1,-1]])
quad2 = Quad([[-1,1,1], [-1,-1,1], [1,-1,1], [1,1,1]])
quad3 = Quad([[1,1,-1], [1,-1,-1], [1,-1,1], [1,1,1]])
quad4 = Quad([[1,1,-1], [1,1,1], [-1,1,1], [-1,1,-1]])
quad5 = Quad([[1,-1,-1], [1,-1,1], [-1,-1,1], [-1,-1,-1]])

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0] /  display[1]), 0.1, 50.0)
camera.translate(np.array([0,0,-5]))

mouse = Mouse([display[0] / 2, display[1] / 2])

glLightModelfv(GL_LIGHT_MODEL_AMBIENT, 0.2)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, (-4,0,0))

while True:
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45, (display[0] /  display[1]), 0.1, 50.0)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_w]:
		camera.translate(np.array([0,0,10000 / 60 / 60 / 1000 * 10]))

	if pressed[pygame.K_s]:
		camera.translate([0,0,-10000 / 60 / 60 / 1000 * 10])

	if pressed[pygame.K_d]:
		camera.translate([-10000 / 60 / 60 / 1000 * 10,0,0])

	if pressed[pygame.K_a]:
		camera.translate([10000 / 60 / 60 / 1000 * 10,0,0])

	mouse.update_mouse()
	camera.rotate(mouse.dx * 0.001, 0, 1, 0)
	camera.rotate(mouse.dy * 0.001, 1, 0, 0)

	camera.lookAt()




	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	quad.draw()
	quad1.draw()
	quad2.draw()
	quad3.draw()
	quad4.draw()
	quad5.draw()
	pygame.display.flip()
	pygame.time.wait(10)
