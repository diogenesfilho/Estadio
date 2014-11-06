# -*- coding: utf-8 -*- 

# Aula sobre composição de objetos e uso do teclado.


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


def parede():
    glBegin(GL_POLYGON)# objeto
    glVertex3f( 0.0, 0.0, 1.0  )  #  ponto de vertice
    glVertex3f( 0.0, 4.0, 1.0  )  #  ponto de vertice
    glVertex3f( 5.0, 4.0, 1.0  )  #  ponto de vertice
    glVertex3f( 5.0, 0.0, 1.0  )  #  ponto de vertice
    glEnd()

def paredeMaior():
    glBegin(GL_POLYGON)# objeto
    glVertex3f( 0.0, 0.0, 1.0  )  #  ponto de vertice
    glVertex3f( 0.0, 4.0, 1.0  )  #  ponto de vertice
    glVertex3f( 6.0, 4.0, 1.0  )  #  ponto de vertice
    glVertex3f( 6.0, 0.0, 1.0  )  #  ponto de vertice
    glEnd()

def chao():
    glBegin(GL_POLYGON)# objeto
    glVertex3f( 0.0, 0.0, 1.0  )  #  ponto de vertice
    glVertex3f( 0.0, 5.0, 1.0  )  #  ponto de vertice
    glVertex3f( 6.0, 5.0, 1.0  )  #  ponto de vertice
    glVertex3f( 6.0, 0.0, 1.0  )  #  ponto de vertice
    glEnd()


def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix() 
    

def desenho():
    global aux1
    global aux2

    #eixos()
    #Cor parede.
    glColor3f(.9, .9, .9) # cor RGB

    parede()

    glTranslate( 0.0, 0.0, -6.0)  #Transtaçao do objeto
    parede()

    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glTranslate( -7.0, 0.0, -1.0)
    paredeMaior()

    glColor3f(.3, .6, .1)
    glRotatef(90, 1.0, 0.0 , 0.0)
    glTranslate( 0.0, 1.0, -1.0)
    chao()

    #Colocando a mesa no lugar.
    glRotatef(90, -1.0, 0.0 , 0.0)
    glTranslate( 3.0, -0.6, 3.0)

    #Base Mesa
    glColor3f(.2, .4, .2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glutSolidCube(0.8)
    #glTranslate( 0.0, 0.0, -0.71)  #Transtaçao do objeto
    glPopMatrix()

    #Tampa Mesa.
    glColor3f(.9,.7,.1)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate( 0.0, 0.0, -0.5)
    glutSolidCylinder(0.9, 0.1, 30, 30)
    glPopMatrix()

    #Chaleira.
    glColor3f(.9,.5,.1)
    glTranslate( 0.0, 0.6, 0.0)
    glutSolidTeapot(0.2)

    #Copo
    glColor3f(.5,.6,.9)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate( 0.6, 0.1, -0.08)
    glutSolidCylinder(0.05, 0.19, 30, 30)
    glPopMatrix()


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
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva
    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho

# Função callback chamada para gerenciar eventos de teclas normais 
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

# Função callback chamada para gerenciar eventos de teclas especiais
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
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()

#global esqdir
#global cimabaixo

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow("Dinner Room")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT



