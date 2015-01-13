__author__ = 'pedro'

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Objeto:

    def __init__(self, codigo):
        self.x, self.y, self.z = 0, 0, 0
        self.tamanho = 0
        self.codigo = codigo

    def executar(self):
        exec(self.codigo, globals())

    def transladar(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.codigo = "glPushMatrix()\n"+"glLoadIdentity\n"+"glTranslate({:f},{:f},{:f})".format(x, y, z)\
                      +self.codigo+"glPopMatrix()"

    def escalonar(self, tamanho):
        self.tamanho = tamanho
        self.codigo = "\nglScale(t,t,t)\n".replace('t', str(tamanho)) + self.codigo

    def colisao(self, x, z):
        if abs(self.x - x) < (self.x + x):
            if abs(self.z - z) < (self.z + z):
                return 'colisão'
        return 'ok'