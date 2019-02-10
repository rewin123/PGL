import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

def vector_mul(v1, v2):
	return np.array([v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]])

class Camera():
	def __init__(self):
		self.pos = np.zeros((3,))
		self.frw = np.array([0.0,0.0,1.0])
		self.up = np.array([0.0,1.0,0.0])

	#Операция установки мира для корректного отображения камеры
	def lookAt(self):
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		trgt = self.pos + self.frw

		self.view = gluLookAt(self.pos[0],self.pos[1], self.pos[2], 
			trgt[0],trgt[1], trgt[2], 
			self.up[0], self.up[1], self.up[2])




	#Сдвигаем камеру на значение move
	def translate(self, move):
		rgt = vector_mul(self.frw, self.up)
		self.pos += move[2] * self.frw + move[1] * self.up - move[0] * rgt

	def rotate(self, angle, x, y, z):
		rgt = vector_mul(self.frw, self.up)
		self.frw += rgt * y * angle - self.up * x * angle
		self.frw /= np.linalg.norm(self.frw)

