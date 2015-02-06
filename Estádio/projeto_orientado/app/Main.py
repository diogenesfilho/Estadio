__author__ = 'pedro'
from model.Camera import *
from model.Objeto import *
from model.Complex import *
import pickle
from sys import argv

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Main:

    def __init__(self, objetos):
        self.objetos = objetos
        self.bola = Bola();self.camera = Camera();self.placar = Placar()
        self.campo = Campo()
        self.camera.obstaculos = self.objetos
        glutInit(argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutCreateWindow("Movimento Câmera")
        self.iluminacao_da_cena()
        glutDisplayFunc(self.tela)
        glutKeyboardFunc(self.bola.teclado)
        glutMouseFunc(self.camera.scroll)
        glutSpecialFunc(self.camera.teclas_especiais)
        glutMainLoop()

    def iluminacao_da_cena(self):
        luzAmbiente = [.2, .2, .2, 1]
        luzDifusa = [.7, .7, .7, 1]
        luzEspecular = [.1, .1, .1, 1]
        posicaoLuz = [0, 50.0, 50.0, 1.0]
        especularidade = [.2, .2, .2, .2]
        especMaterial = 1

        glClearColor(1.0, 1.0, 1.0, 1.0)
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
        glClearColor(.4, .4, .4, .2)
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
        glPushMatrix()
        glTranslatef(0,-1.2,0)
        glColor3f(0.9, 0.9, 0.9)
        glBegin(GL_QUADS)
        glVertex3f(-100.0, 0.0, -100.0)
        glVertex3f(-100.0, 0.0,  100.0)
        glVertex3f(100.0, 0.0,  100.0)
        glVertex3f(100.0, 0.0, -100.0)
        glEnd()
        glPopMatrix()
        self.campo.desenhar()
        self.placar.desenhar()
        self.bola.desenhar()
        glutSwapBuffers()

if __name__ == "__main__":
    objetos = [Objeto(pickle.load(open('../objs/arqGrade.pkl', 'rb'))),
               Objeto(pickle.load(open('../objs/arqAlta.pkl', 'rb'))),
               Objeto(pickle.load(open('../objs/Grade.pkl', 'rb'))),
               Objeto(pickle.load(open('../objs/arqFrente.pkl', 'rb'))),
               Objeto(pickle.load(open('../objs/arqTras.pkl', 'rb')))
    ]
    Main(objetos)