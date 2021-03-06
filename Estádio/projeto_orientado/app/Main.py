# -*- coding: utf-8 -*- 
from Camera import *
from Objeto import *
from Complex import *
import pygame
import pickle
from sys import argv

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Main:

    def __init__(self, objetos):
        self.objetos = objetos
        self.bola = Bola()
        self.camera = Camera()
        self.camera.obstaculos = self.objetos
        glutInit(argv)
        
        glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(1000, 800)
        glutCreateWindow("Estadio Coaracy da Mata Fonseca")
        self.iluminacao_da_cena()
        for i in self.objetos:
            i.desenhar()
        glutDisplayFunc(self.tela)
        glutKeyboardFunc(self.bola.teclado)
        glutMouseFunc(self.camera.scroll)
        glutSpecialFunc(self.camera.teclas_especiais)
        glutReshapeFunc(self.resize)
        glutMainLoop()

    def resize(self, width, height):
        if height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small
            height = 1

        glViewport(0, 0, width, height)        # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def iluminacao_da_cena(self):
        luzAmbiente = [.5, .5, .5, .9]
        luzDifusa = [.7, .7, .7, 1]
        luzEspecular = [.5, .5, .5, .3]
        posicaoLuz = [0, 50.0, 50.0, 1.0]
        especularidade = [.2, .2, .2, .2]
        especMaterial = 1

        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_SMOOTH)
        glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
        glMateriali(GL_FRONT, GL_SHININESS, especMaterial)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)
        glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
        glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
        glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)

    def tela(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glClearColor(1, 1, 1, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.camera.distancia, 1, 0.1, 500)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.camera.x, self.camera.y, self.camera.z, self.camera.x+self.camera.lx,
                  self.camera.y, self.camera.z+self.camera.lz, 0.0, 1.0,  0.0)

        glPushMatrix()
        for i in self.objetos:
            i.executar()
        glPopMatrix()

        self.bola.desenhar()
        glutSwapBuffers()

if __name__ == "__main__":
    pygame.init()
    objetos = [Terreno(), ArqAlta(), Grade(), Placar(), Campo(), ArqGrade(),BancoReserva(),
               ArqFrente(), ArqTras(), Ceu()]
    Main(objetos)