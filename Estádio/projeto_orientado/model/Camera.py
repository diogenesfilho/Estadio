__author__ = 'pedro'
from math import sin, cos
from OpenGL.GLUT import *


class Camera:
    def __init__(self):
        self.x, self.z, self.y = 0, 5, 1
        self.lx, self.lz = 0.0, -1.0
        self.angulo = 0.0
        self.obstaculos = []
        self.distancia = 20

    def teclas_especiais(self, tecla, x, y):
        fraction = .5
        if tecla == GLUT_KEY_LEFT:
            self.angulo -= 0.05
            self.lx = sin(self.angulo)
            self.lz = -cos(self.angulo)
        if tecla == GLUT_KEY_RIGHT:
            self.angulo += 0.05
            self.lx = sin(self.angulo)
            self.lz = -cos(self.angulo)
        if tecla == GLUT_KEY_UP:
            self.x += self.lx * fraction
            self.z += self.lz * fraction
        if tecla == GLUT_KEY_DOWN:
            self.x -= self.lx * fraction
            self.z -= self.lz * fraction

        glutPostRedisplay()

    def teclas(self, tecla, x, y):
        if tecla == b's':
            self.y += .1
        if tecla == b'd':
            self.y -= .1
        glutPostRedisplay()
        
    def scroll(self, button,state,x,y):
        if(button == 3):
            self.distancia += 2
        elif(button == 4):
            self.distancia -= 4

        glutPostRedisplay()