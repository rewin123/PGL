import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def load_shaders():
	with open('vertex.c', 'r') as file:
		s = file.read()
		VERTEX_SHADER = shaders.compileShader(s, GL_VERTEX_SHADER)

	with open('fragment.c', 'r') as file:
		FRAGMENT_SHADER = shaders.compileShader(file.read(), GL_FRAGMENT_SHADER)
	shader = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
	shaders.glUseProgram(shader)
	return VERTEX_SHADER, FRAGMENT_SHADER, shader

class  ShaderLoader():
	"""docstring for  """
	def __init__(self):
		self.vs, self.fs, self.s = load_shaders()
		self.vec_locations = {'objectColor' : glGetUniformLocation(self.s, 'objectColor'),
		'lightColor' : glGetUniformLocation(self.s, 'lightColor')}

	def draw(self):
		glUniform3f(self.vec_locations['objectColor'], 1,0,0)
		glUniform3f(self.vec_locations['lightColor'], 1,1,1)

