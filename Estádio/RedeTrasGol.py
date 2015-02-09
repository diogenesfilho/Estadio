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

global esqdir
global cimabaixo
global aux1
global aux2
global angulo


esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45

def rede():

    glPushMatrix()
    glScalef(1,3,3)

    #Estrura externa.
    glPushMatrix() 
    #Isolando para que nao aja problemas quando rotacionar e transladar.
    glPushMatrix()             
    glColor3f(.1, .1, .1)
    glutSolidCylinder(0.05, 5, 30, 10)

    glTranslate( 0.0, -5.0, 0.0)
    glutSolidCylinder(0.05, 5, 30, 10)
    glPopMatrix()


    glPushMatrix()
    glScalef(1,1,0.3)

    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.05, 5, 30, 10)

    glTranslate( 0.0, 16.7, 0.0)
    glutSolidCylinder(0.05, 5, 30, 10)
    glPopMatrix()

    glPopMatrix()

    #Estrura interna vertical.
    glPushMatrix()
    glScalef(0.0, 10, 0.6)
    glTranslate( 0.0, -0.25, -0.5)
    for s in range(8):        
        glTranslate( 0.0, 0.0, 1.0)
        glutWireCube(0.5)
    glPopMatrix()

    #Estrura interna horizontal.
    glRotatef(90,.1,.0,.0)
    glPushMatrix()
    glScalef(0.0, 10, 1)
    glTranslate( 0.0, 0.25, -0.5)
    for s in range(5):        
        glTranslate( 0.0, 0.0, 1.0)
        glutWireCube(0.5)

    glPopMatrix()

    glPopMatrix()

def estrutura():

    #Estrura externa.
    glPushMatrix()
    alturaRede = 3 
    glScalef(1,1,alturaRede)  
    glColor3f(.1, .1, .1)
    glutSolidCylinder(0.08, 5, 100, 50)
    distanciaEntreTraves = -15
    glTranslate( 0.0, distanciaEntreTraves, 0.0)
    glutSolidCylinder(0.05, 5, 30,30)
    glPopMatrix()
    rede()

def redeAtrasDoGol():

    glScalef(0.2,0.2,0.2)

    glPushMatrix()
    glRotatef(90,1,0,0)
    alturaTrave,larguraTrave = 2,2
    glScalef(1,larguraTrave,alturaTrave)
    estrutura()

    glTranslate(0,15,0)
    estrutura()
    glPopMatrix()


def desenho():

    redeAtrasDoGol()

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

    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():

    global angulo
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(angulo,1,0.1,500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
   
    glEnable(GL_DEPTH_TEST)

    desenho()                    
    glFlush() 


def Teclado (tecla, x, y):
    global aux1
    global aux2
    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
    
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )
    
    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )
        
    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )
    tela()
    glutPostRedisplay()

def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()   

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == 3):
        if (state == GLUT_DOWN): 
            if (angulo >= 10):
                angulo -= 2
        
    if (button == 4):
        if (state == GLUT_DOWN):
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow("Rede Atrás do Gol")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()



