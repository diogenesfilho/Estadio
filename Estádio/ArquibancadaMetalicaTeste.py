# -*- coding: utf-8 -*- 

from math import cos
from math import pi
from math import sin
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir,cimabaixo
global mouseX, mouseY,mouseX_ant, mouseY_ant
global distancia
global obj

esqdir,cimabaixo = 0,0
mouseY,mouseX,mouseX_ant,mouseY_ant = .0,.0,.0,.0
distancia = 20
obj = GLuint()


def grade(qtd):
    glRotate(-90,1,0,0)
    glPushMatrix()
    glColor(0,0,0)
    for i in range(qtd):
        glutSolidCylinder(0.08,(i+1),10,10)
        glTranslate(1,0,0)
    glPopMatrix()
    glRotate(90,1,0,0)

def bancos(qtd):
    glPushMatrix()
    glScale(.5,.4,2)
    
    for i in range(qtd):
        glutSolidCube(0.5)
        glTranslate(0.5,0,0)
    glPopMatrix()

def corrimao():
    # CORRIMÃO

    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glTranslate(-0.6,3.5,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8,0.8,0.8)
    glTranslate(-0.6,3.4,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8,0.8,0.8)
    glTranslate(-0.6,3.3,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glRotate(90, 1.0, 0.0, 0.0)
    glTranslate(-0.6,18,-3.5)
    glutSolidCylinder(0.02, 0.5, 40, 10)
    glPopMatrix()

def desenho():
    global obj
    obj = glGenLists(1)
    glNewList(obj, GL_COMPILE)

    # PISO PASSAGEM

    glPushMatrix()
    glTranslate(0,1,99.9)
    glRotate(90,0,1,0)
    for i in range(1):
        glScale(1,1,2)
        bancos(400)
        glTranslate(0,1,1)
        glColor3f(3,0,0) # <- Apague o chapéu aqui.
        glRotate(90,1,0,0)
        glTranslate(0,3.5,-8)
        bancos(400)
    glPopMatrix()

    glPushMatrix()
    glTranslate(2,-15,-85)
    glScale(5,5,5)
    for i in range(15):
        corrimao()
        glTranslate(0,0,1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.4,1,100)
    glRotate(90,0,1,0)
    for i in range(9):
        if i % 2 == 0:
            glColor3f(0.2,0.2,0.2)
        else:
            glColor3f(0.8,0.8,0.8)
        bancos(400)
        glTranslate(0,1,1)

    glPopMatrix()

    for i in range(50):
        glPushMatrix()
        grade(10)
        glRotate(-180,0,1,0)
        glRotate(-90,0,0,1)
        glTranslate(-9,-9,0)
        grade(10)
        glPopMatrix()
        glTranslate(0,0,2)

    glEndList()

def executar():
    global obj
    glCallList(obj)


def iluminacao_da_cena():
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[25, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade
    gluPerspective(distancia,1,0.1,500) # Especifica a projeção perspectiva
    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo
    gluLookAt(sin(esqdir) * 10, cimabaixo ,cos(esqdir) * 10, mouseX,mouseY,0, 0,1,0) # Especifica posição do observador e do alvo
    #iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    executar()                   
    glFlush()                    # Aplica o desenho

def teclado(tecla,x,y):
    global esqdir
    global cimabaixo
    if tecla == b'a':
        esqdir = esqdir - 0.1
    elif tecla == b'd':
        esqdir = esqdir + 0.1
    elif tecla == b'w':
        cimabaixo = cimabaixo + 0.1
    elif tecla == b's':
        cimabaixo = cimabaixo - 0.1
    glutPostRedisplay()   

def mouse(x,y):
    global mouseX, mouseY, mouseY_ant, mouseX_ant
    mouseX = (mouseX - mouseX_ant) * 0.005
    mouseY = (mouseY_ant - mouseY) * 0.005

    mouseY_ant,mouseX_ant = y,x

    glutPostRedisplay()

def scroll(button,state,x,y):
    global distancia
    
    if(button == 3):
        distancia += 2
    elif(button == 4):
        distancia -= 4

    glutPostRedisplay()
glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow("Arquibancada")
distancia = 20
desenho()
glutDisplayFunc(tela)
glutMotionFunc(mouse)
glutMouseFunc(scroll)
glutKeyboardFunc (teclado)
glutMainLoop()  # Inicia o laço de eventos da GLUT
