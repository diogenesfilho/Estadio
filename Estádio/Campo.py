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
from PIL import Image, ImageFilter

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global textura1


esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45

def carrega_textura():
    global textura1

    im = Image.open("campo.jpg", "r")
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

def rede():

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
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.05, 5, 30, 10)

    glTranslate( 0.0, 5.0, 0.0)
    glutSolidCylinder(0.05, 5, 30, 10)
    glPopMatrix()

    glPopMatrix()

    #Estrura interna vertical.
    glPushMatrix()
    glScalef(0.0, 10, 0.5)
    glTranslate( 0.0, -0.25, -0.7)
    for s in range(11):        
        glTranslate( 0.0, 0.0, 0.95)
        glutWireCube(0.5)
    glPopMatrix()

    #Estrura interna horizontal.
    glRotatef(90,.1,.0,.0)
    glPushMatrix()
    glScalef(0.0, 10, 0.5)
    glTranslate( 0.0, 0.25, -0.6)
    for s in range(10):        
        glTranslate( 0.0, 0.0, 0.95)
        glutWireCube(0.5)
    glPopMatrix()

def trave():

    glScalef(0.3,0.3,0.3)
    glPushMatrix()

    rede()

    glPushMatrix(0,0,-5)
    glScalef(1.5,1,1)
    glTranslate( 0.0, 5.0, 0.0)
    glRotatef(90,0,1,0)
    rede()
    glPopMatrix()

    glPushMatrix()
    glScalef(1.5,1,1)
    glTranslate( 0.0, 5.0, 0.0)
    glRotatef(90,0,0,1) 
    rede()

    glTranslate( -5.0, 5.0, 0.0)
    rede()

    glPopMatrix()


    glPopMatrix()



def Campo():
    global textura1
    carrega_textura()

    glEnable(GL_TEXTURE_2D)
    glBegin(GL_POLYGON)# objeto

    glVertex3f( 8.0, -1, 3.0  )  #  ponto de vertice
    glTexCoord2f(1.0,0.0)
    glVertex3f( 8.0, -1, -14.0  )  #  ponto de vertice
    glTexCoord2f(1.0,1.0)
    glVertex3f( -2.0, -1, -14.0  )  #  ponto de vertice
    glTexCoord2f(0.0,1.0)
    glVertex3f( -2.0, -1, 3.0  )  #  ponto de vertice
    glTexCoord2f(0.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def desenho():

  
    glPushMatrix()
    Campo()
    glPopMatrix()



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
glutCreateWindow("Campo")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT



