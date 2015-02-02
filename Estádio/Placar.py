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
from PIL import Image, ImageFilter

global esqdir
global cimabaixo
global aux1
global aux2
global angulo


esqdir = 3.1
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 160

def carrega_imagem():
    global textura1

    im = Image.open("placar.jpg", "r")
    try:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
    except SystemError:
        ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
    
    textura1 = glGenTextures(1)
    #glBindTexture(GL_TEXTURE_2D, textura1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    
    glTexImage2D(
      GL_TEXTURE_2D, 0, 3, ix, iy, 0,
      GL_RGBA, GL_UNSIGNED_BYTE, image
      )

def desenho():

    #Coluna Esq
    glPushMatrix()
    glColor3f(1,1,1)
    glScalef(2,70,1.5)
    glTranslate(-0.7,0,0)
    glutSolidCube(0.5)
    glPopMatrix()

    #Coluna Dir
    glPushMatrix()
    glColor3f(1,1,1)
    glScalef(2,70,1.5)
    glTranslate(6.9,0,0)
    glutSolidCube(0.5)
    glPopMatrix()

    #Bloco Princ
    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glScalef(25,15,1)
    glTranslate(0.25,1.7,0)
    glutSolidCube(1)
    glPopMatrix()

    # Textura placar
    carrega_imagem()

    glEnable(GL_TEXTURE_2D)
    glRotate(90, 0,1,0)
    glTranslate(-12.3,25,6)
    glScale(13,7,12)
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glTexCoord2f(1.0, 0.0) 
    glVertex3f( 1.0, -1.0, -1.0)

    glTexCoord2f(1.0, 1.0) 
    glVertex3f( 1.0,  1.0, -1.0)

    glTexCoord2f(0.0, 1.0) 
    glVertex3f( 1.0,  1.0,  1.0)

    glTexCoord2f(0.0, 0.0) 
    glVertex3f( 1.0, -1.0,  1.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0.0, 0.0, 0.0, 0.0)

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

    global angulo
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0.0, 0.0,0.0, 0.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva
    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    #iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho

# Função callback chamada para gerenciar eventos de teclas normais 
def Teclado (tecla, x, y):
    global aux1
    global aux2
    
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 2
    
    if tecla == b's': # S
        aux1 = aux1 + 2
        
    if tecla == b'w': # W
        aux2 = aux2 + 2

    if tecla == b'z': # Z
        aux2 = aux2 - 2
    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    
    if tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
        print esqdir
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    
    tela()
    glutPostRedisplay()   

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == 3):
        if (state == GLUT_DOWN): 
            angulo -= 2
        
    if (button == 4):
        if (state == GLUT_DOWN):   # Zoom-out
            angulo += 2

    tela()
    glutPostRedisplay()

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(1024,800)
glutCreateWindow("Placar")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT



