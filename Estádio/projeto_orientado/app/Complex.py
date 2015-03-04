# -*- coding: utf-8 -*-
from gi.overrides.keysyms import musicalflat
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from pygame.mixer import music

class Ceu:

    def __init__(self):
        self.obj = GLuint()
        self.quad = gluNewQuadric()
        self.texturaID = GLuint()
        self._textureID = self.carrega_textura("../objs/ceu.jpg")
        self.rotate = 0
    def carrega_textura(self, caminho):

        im = Image.open(caminho, "r")
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
        self.textura1 = glGenTextures(1, self.texturaID)
        glBindTexture(GL_TEXTURE_2D, self.texturaID)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return self.texturaID

    def desenhar(self):

        self._textureID = self.carrega_textura("../objs/ceu.jpg")
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        #glBindTexture(GL_TEXTURE_2D, self._textureID)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glFrontFace(GL_CW)
        #glMaterial(GL_FRONT_AND_BACK)
        glRotatef(-45,1,1,1)
        glPushMatrix()
        glPushMatrix()
        gluQuadricTexture(self.quad, 1)
        glDisable(GL_CULL_FACE)
        glRotate(self.rotate,0,1,0)
        gluSphere(self.quad, 50, 50, 50)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        glPopMatrix()
        glPopMatrix()
        
        glutSwapBuffers()

    def executar(self):
        self.desenhar()
        #self.rotate += .15
        glutPostRedisplay()

class Placar:

    def __init__(self):
        self.textura1 = glGenTextures(1)
        self.obj = GLuint()

    def carrega_imagem(self):
        im = Image.open("../objs/placar.jpg", "r")
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)


        #glBindTexture(GL_TEXTURE_2D, textura1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


        glTexImage2D(
          GL_TEXTURE_2D, 0, 3, ix, iy, 0,
          GL_RGBA, GL_UNSIGNED_BYTE, image
          )

    def desenhar(self):
        self.obj = glGenLists(3)
        glNewList(self.obj,GL_COMPILE)
        glPushMatrix()

        glTranslatef(10, -.15, 5)
        glScale(.05,.05,.05)
        glRotate(35, 0, 1, 0)
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
        glScalef(25,14,1)
        glTranslate(0.25,1.7,0)
        glutSolidCube(1)
        glPopMatrix()

        # Textura placar
        self.carrega_imagem()

        glEnable(GL_TEXTURE_2D)
        glRotate(90, 0,1,0)
        glTranslate(-12.3,24,6)
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
        glPopMatrix()

        glEndList()

    def executar(self):
        glCallList(self.obj)

class Campo:

    def __init__(self):
        self.textura1 = glGenTextures(1)
        self.obj = GLuint()

    def carrega_textura(self):
        im = Image.open("../objs/campo.jpg", "r")
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    def trave(self):
        glTranslate(4,0,0)
        glScalef(0.4, 1, 3)
        glPushMatrix()

        self.rede()

        glPushMatrix(0, 0, -5)
        glScalef(1.5, 1, 1)
        glTranslate(0.0, 5.0, 0.0)
        glRotatef(90, 0, 1, 0)
        self.rede()
        glPopMatrix()

        glPushMatrix()
        glScalef(1.5, 1, 1)
        glTranslate(0.0, 5.0, 0.0)
        glRotatef(90, 0, 0, 1)
        self.rede()

        glTranslate(-5.0, 5.0, 0.0)
        self.rede()

        glPopMatrix()

        glPopMatrix()

    def rede(self):

        glPushMatrix()
        glColor3f(1, 1, 1)
        #Isolando para que nao aja problemas quando rotacionar e transladar.
        glPushMatrix()

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
        glTranslate(0.0, -0.25, -0.7)
        for s in range(11):
            glTranslate( 0.0, 0.0, 0.95)
            glutWireCube(0.5)
        glPopMatrix()

        #Estrura interna horizontal.
        glRotatef(90, .1, .0, .0)
        glPushMatrix()
        glScalef(0.0, 10, 0.5)
        glTranslate(0.0, 0.25, -0.6)
        for s in range(10):
            glTranslate(0.0, 0.0, 0.95)
            glutWireCube(0.5)
        glPopMatrix()

    def redeTrasGol(self):

        glPushMatrix()
        glScalef(1, 1, 3)
        glColor3f(0.2, 0.2, 0.2)
        glutSolidCylinder(0.02, 5, 100, 50)
        distanciaEntreTraves = -15
        glTranslate( 0.0, distanciaEntreTraves, 0.0)
        glutSolidCylinder(0.015, 5, 30, 30)
        glPopMatrix()

        #Estrura interna horizontal.
        glPushMatrix()
        glScalef(0.0, 30, 0.67)
        glTranslate(0.0, -0.25, -0.55)
        for s in range(23):
            glTranslate(0.0, 0.0, 1.0)
            glutWireCube(0.5)
        glPopMatrix()

        #Estrura interna .vertical
        glRotatef(90, .1, .0, .0)
        glPushMatrix()
        glScalef(0.0, 30, 0.64)
        glTranslate( 0.0, 0.255, -0.5)
        for s in range(23):
            glTranslate(0.0, 0.0, 1.0)
            glutWireCube(0.5)

        glPopMatrix()

    def Campo(self):
        self.carrega_textura()
        glEnable(GL_TEXTURE_2D)
        glBegin(GL_POLYGON)# objeto
        glColor3f(1, 1, 1)
        glVertex3f(8.0, -1, 3.0)  #  ponto de vertice
        glTexCoord2f(1.0, 0.0)
        glVertex3f(8.0, -1, -14.0)  #  ponto de vertice
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-2.0, -1, -14.0)  #  ponto de vertice
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-2.0, -1, 3.0)  #  ponto de vertice
        glTexCoord2f(0.0, 0.0)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def bandeirinha(self):


        glPushMatrix()
        glColor3f(0.8, 0.8, 0.8)
        glRotatef(90, 1.0, 0.0, 0.0)
        glTranslate(-1.1, 1.8, 0.7)
        glutSolidCylinder(0.004, 0.3, 30, 30)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1, 1, 0)
        glScalef(0.01, 0.1, 0.2)
        glTranslate(-110, -7, 8.6)
        glutSolidCube(1)
        glPopMatrix()

    def desenhar(self):
        self.obj = glGenLists(4)
        glNewList(self.obj,GL_COMPILE)

        glPushMatrix()

        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 0, 0, 1)
        glTranslate(2.7, -1.6, -0.2)
        alturaTrave, larguraTrave = 0.08, 0.2
        glScalef(1, larguraTrave, alturaTrave)
        self.redeTrasGol()
        glPopMatrix()

        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glRotatef(90, 0, 0, 1)
        glTranslate(-13.7, -1.6, -0.2)
        alturaTrave, larguraTrave = 0.08, 0.2
        glScalef(1, larguraTrave, alturaTrave)
        self.redeTrasGol()
        glPopMatrix()

        glPushMatrix()
        glScalef(0.1, 0.1, 0.1)
        glRotate(90, 0.0, 1.0, 0.0)
        glTranslate(-25, -5, 23)
        self.trave()
        glPopMatrix()

        glPushMatrix()
        glScalef(0.1, 0.1, 0.1)
        glRotate(-90, 0.0, 1.0, 0.0)
        glTranslate(-135, -5, -38)
        self.trave()
        glPopMatrix()

        glPushMatrix()
        self.Campo()
        glPopMatrix()

        glPushMatrix()
        self.bandeirinha()
        glPopMatrix()

        glPushMatrix()
        glTranslate(8.2, 0, 0)
        self.bandeirinha()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0, 0, -14.7)
        self.bandeirinha()
        glPopMatrix()

        glPushMatrix()
        glTranslate(8.2, 0, -14.7)
        self.bandeirinha()
        glPopMatrix()

        glPopMatrix()

        glEndList()

    def executar(self):
        glCallList(self.obj)

class ArqAlta:
    def __init__(self):
        self.obj = GLuint()

    def degrau(self):
        glPushMatrix()
        glScalef(2, 80, 1.0)
        glutSolidCube(0.5)
        glPopMatrix()

    def degrau2(self):
        glPushMatrix()
        glScalef(2, 700, 1.0)
        glutSolidCube(0.5)
        glPopMatrix()

    def haste(self):
        # Coluna
        glPushMatrix()
        glColor3f(0.1,0.1,0.1)
        glRotate(90, 1.0, 0.0, 0.0)
        glTranslate(-6.4,3.6,-7.5)
        glutSolidCylinder(0.05, 6.0, 40, 10)
        glPopMatrix()

    def janela(self):

        glPushMatrix()
        glColor3f(0,0,0)
        glTranslate(-6.9,6.3,2.85)
        glScalef(1,1,1.4)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.8,0.8,0.8)
        glTranslate(-6.8,6.3,2.85)
        glScalef(1,1,1.4)
        glutSolidCube(0.9)
        glPopMatrix()

    def muroDireito(self):
        # MURO
        glPushMatrix()
        glColor3f(1,1,1)
        glScalef(0.1,1,2.5)
        glTranslate(-100,5.3,-3.3)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-10,6,-9.6)
        glutSolidCylinder(0.02, 2.6, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glRotate(90, 1.0, 0.0, 0.0)
        glTranslate(-10,-8.3,-6)
        glutSolidCylinder(0.04, 0.5, 40, 10)
        glPopMatrix()

    def muroEsquerdo(self):

        glPushMatrix()
        glColor3f(1,1,1)
        glScalef(0.1,1,2.5)
        glTranslate(-100,5.3,3.3)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-10,6,7)
        glutSolidCylinder(0.02, 2.6, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glRotate(90, 1.0, 0.0, 0.0)
        glTranslate(-10,8.3,-6)
        glutSolidCylinder(0.04, 0.5, 40, 10)
        glPopMatrix()


    def corrimao(self):
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
        glTranslate(-0.6,3.2,17)
        glutSolidCylinder(0.02, 3.0, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.3,0.3,0.3)
        glRotate(90, 1.0, 0.0, 0.0)
        glTranslate(-0.6,18,-3.5)
        glutSolidCylinder(0.02, 0.5, 40, 10)
        glPopMatrix()

    def coluna(self):
        glPushMatrix()
        glColor3f(1,1,1)
        glRotatef(90, 1,0,0)
        glScalef(0.3,0.3,10)
        glTranslate(-28.5,-120,0.1)
        glutSolidCube(1)
        glPopMatrix()

    def refletor(self):

        #Base Vertical.
        glRotatef(90, 1.0, 0.0 , 0.0)
        glColor3f(0.5,0.5,0.5)
        glutSolidCylinder(0.07, 15.0, 40, 10)
        glRotatef(5, 1.0, 0.0 , 0.0)
        #Base Luzes.
        glTranslate( -0.75, 0.0, -1.02)

        glColor3f(0.8, 0.8, 0.8) # cor RGB
        #Luzes do meio.
        contador = 0
        glTranslate( -0.1, 0.1, 0.5)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1

        #Luzes de cima.
        contador = 0
        glTranslate( -1.5, 0.0, 0.3)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)#Nao altera. Definir espaco entre as lampadas.
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1

        #Luzes de baixo.
        contador = 0
        glTranslate( -1.5, 0.0, -0.6)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)#Nao altera.Definir espaco entre as lampadas.
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1


        glTranslate( -0.65, -0.1, 0.3)
        glPushMatrix()
        glColor3f(1, 1, 1) # cor RGB
        glScalef(3.5, 0.2, 2.0)
        glutWireCube(0.52)
        glPopMatrix()

        #Fios que seguram as lampadas.
        glPushMatrix()
        glRotatef(90, 0.0, 1.0 , 0.0)
        glTranslate( -0.3, 0.0, -0.92)
        for s in range(3):
            glutSolidCylinder(0.008, 1.83, 10, 1)
            glTranslate( 0.3, 0, 0)
        glPopMatrix()

    def executar(self):
        glCallList(self.obj)

    def desenhar(self):
        self.obj = glGenLists(1)
        glNewList(self.obj, GL_COMPILE)
        glPushMatrix()
        glScalef(.2,.2,.2)
        glTranslate(-15,-4,-25)
        # Parte Baixa

        glPushMatrix()
        glScalef(1,1,2)
        glRotatef(90, 1.0, 0.0, 0.0)
        contador = 0
        while contador <= 4:
            if contador%2==0:
                glColor3f(0.1,0.1,0.1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(1,1,1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            contador+=1
        glPopMatrix()

        # Divisão

        glPushMatrix()
        glRotatef(90, 1.0, 0.0, 0.0)
        glColor3f(1,1,1)
        glScalef(0.1,80,7)
        glScalef(1,2,1)
        glTranslate(-6,0,-0.2)
        glutSolidCube(0.5)
        glPopMatrix()

        # Piso parte alta

        glPushMatrix()
        glColor3f(0.5,0.5,0.5)
        glScalef(2.5,1,1)
        glScalef(1,1,2)
        glTranslate(-0.75,2,0)
        glRotatef(90, 1.0, 0.0, 0.0)
        self.degrau()
        glPopMatrix()


        # Parte Alta Esquerda

        glPushMatrix()
        glTranslate(-9.5,4.6,23.2)
        glRotatef(90, 1.0, 0.0, 0.0)
        glScalef(1,2.7,1)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 12:
            if contador%2==0:
                glColor3f(1,1,1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            contador+=1
        glPopMatrix()

        # Parte Alta Direita

        glPushMatrix()
        glTranslate(-9.5,4.6,-23.2)
        glRotatef(90, 1.0, 0.0, 0.0)
        glScalef(1,2.7,1)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 12:
            if contador%2==0:
                glColor3f(1,1,1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            contador+=1
        glPopMatrix()

        # Parte Alta Meio

        glPushMatrix()
        glTranslate(-6,3.2,0)
        glRotatef(90, 1.0, 0.0, 0.0)
        glScalef(1,1.17,1)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 5:
            if contador%2==0:
                glColor3f(0.1,0.1,0.1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(1,1,1)
                self.degrau()
                glTranslate(0.5,0,0.2)
            contador+=1
        glPopMatrix()


        # Cabines de imprensa

            # BLOCO
        glPushMatrix()
        glColor3f(0.9,0.9,0.9)
        glTranslate(-8.0,5,-0.15)
        glScalef(1,1.5,2.6)
        glutSolidCube(3)
        glPopMatrix()

            # JANELAS
        glPushMatrix()
        contador = 0
        while contador <= 4:
            self.janela()
            glTranslate(0,0,-1.5)
            contador+=1
        glPopMatrix()

            # HASTES
        glPushMatrix()
        contador = 0
        while contador <= 5:
            self.haste()
            glTranslate(0,0,-1.5)
            contador+=1
        glPopMatrix()

            # TETO
        glPushMatrix()
        glColor3f(0.1,0.1,0.1)
        glTranslate(-4.2,7.4,0)
        glScalef(1.5,0.05,2.7)
        glutSolidCube(3)
        glPopMatrix()

            # BALCÃO
        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-6,4,3.7)
        glScalef(1,1.2,0.1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-6,4,-3.7)
        glScalef(1,1.2,0.1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-5.5,4,-2.1)
        glScalef(0.1,1.2,3.1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-5.5,4,2.1)
        glScalef(0.1,1.2,3.1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0,0,0)
        glTranslate(-5.7,4.6,2.1)
        glScalef(0.3,0.1,3.1)
        glutSolidCube(1)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0,0,0)
        glTranslate(-5.7,4.6,-2.1)
        glScalef(0.3,0.1,3.1)
        glutSolidCube(1)
        glPopMatrix()


        # CORRIMÕES
        glPushMatrix()
        glTranslate(0,0,20)
        contador = 0
        while contador <= 51:
            self.corrimao()
            glTranslate(0,0,-1.5)
            contador+=1
        glPopMatrix()

        # MURO DIR
        glPushMatrix()
        contador = 0
        while contador <= 20:
            self.muroDireito()
            glTranslate(0,0,-1.5)
            contador+=1
        glPopMatrix()

            # perto cabine
        glPushMatrix()
        glTranslate(3.5,-1.5,2.8)
        self.muroDireito()
        glColor3f(1,0,0)
        glPopMatrix()


        # MURO ESQ
        glPushMatrix()
        contador = 0
        while contador <= 20:
            self.muroEsquerdo()
            glTranslate(0,0,1.5)
            contador+=1
        glPopMatrix()

        glPushMatrix()
        glTranslate(3.5,-1.5,-2.8)
        self.muroEsquerdo()
        glColor3f(1,0,0)
        glPopMatrix()


        # COLUNA SUSTENTAÇÃO
        glPushMatrix()
        contador = 0
        while contador <= 8:
            self.coluna()
            glTranslate(0,0,9)
            contador+=1
        glPopMatrix()


        # REFLETOR DIREITO
        glPushMatrix()
        glTranslate(-11,20,-20)
        glRotatef(90, 0,1,0)
        glScalef(2,2,2)
        self.refletor()
        glPopMatrix()

        # REFLETOR ESQUERDO
        glPushMatrix()
        glTranslate(-11,20,20)
        glRotatef(90, 0,1,0)
        glScalef(2,2,2)
        self.refletor()
        glPopMatrix()

        glPopMatrix()
        glEndList()

#------------------------------------------------------------------------------

class Terreno:
    def __init__(self):
        self.textura1 = glGenTextures(1)
        self.obj = GLuint()

    def carrega_imagem(self):
        im = Image.open("../objs/terreno.jpg", "r")
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)


        #glBindTexture(GL_TEXTURE_2D, textura1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


        glTexImage2D(
          GL_TEXTURE_2D, 0, 3, ix, iy, 0,
          GL_RGBA, GL_UNSIGNED_BYTE, image
          )

    def desenhar(self):
        self.obj = glGenLists(97)
        glNewList(self.obj, GL_COMPILE)

        self.carrega_imagem()
        glEnable(GL_TEXTURE_2D)
        glPushMatrix()
        glTranslatef(0,-1.1,0)
        glBegin(GL_QUADS)
        glColor3f(1,1,1)

        glVertex3f(-100.0, 0.0, -100.0)
        glTexCoord2f(0.0, 150)
        glVertex3f(-100.0, 0.0,  100.0)
        glTexCoord2f(150, 150)
        glVertex3f(100.0, 0.0,  100.0)
        glTexCoord2f(150, 0.0)
        glVertex3f(100.0, 0.0, -100.0)
        glTexCoord2f(0.0, 0.0)
        glEnd()
        glPopMatrix()

        glDisable(GL_TEXTURE_2D)

        glEndList()

    def executar(self):
        glCallList(self.obj)

class Bola:

    def __init__(self):
        music.load("../objs/torcidaASA.mp3")
        self.obj = GLuint()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        self.quad = gluNewQuadric()
        self.textura1 = ''
        self.axisX = 3.5
        self.axisZ = -5
        self.esqdir = 0
        self.cimabaixo = 0
        self.texturaID = GLuint()
        self._textureID = self.carrega_textura("../objs/soccer_ball.jpeg")

    def carrega_textura(self, caminho):

        im = Image.open(caminho, "r")
        try:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBA", 0, -1)
        except SystemError:
            ix, iy, image = im.size[0], im.size[1], im.tostring("raw", "RGBX", 0, -1)
        self.textura1 = glGenTextures(1, self.texturaID)
        glBindTexture(GL_TEXTURE_2D, self.texturaID)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return self.texturaID

    def desenhar(self):

        self._textureID = self.carrega_textura("../objs/soccer_ball.jpeg")
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self._textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glPushMatrix()
        glTranslatef(self.axisX, -.95, self.axisZ)
        glScale(.02, .02, .02)
        glPushMatrix()
        glRotatef(90, 1.0, 0.0, 0.0)
        glRotatef(self.esqdir, 0, 0, 1)
        glRotatef(self.cimabaixo, 0, 1, 0)
        gluQuadricTexture(self.quad, 1)
        gluSphere(self.quad, 2, 20, 20)
        glPopMatrix()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)

        glutSwapBuffers()

    def teclado(self, tecla, x, y):
        if tecla == b'a' and self.axisX >= -1:
            self.esqdir += - 20
            self.axisX -= .1

        if tecla == b's'and self.axisZ <= 1.7:
            self.cimabaixo += - 20
            self.axisZ += .1

        if tecla == b'w' and self.axisZ >= -12.8:
            self.cimabaixo += + 20
            self.axisZ -= .1

        if tecla == b'd' and self.axisX <= 6.9:
            self.esqdir += + 20
            self.axisX += .1

        # TRAVE - X 2.4 a 3.7
        if self.axisZ < -12.8 and 2.4 <= self.axisX <= 3.7:
            music.play(0)

        # 1.8 / 3.7 a 2.4
        if self.axisZ > 1.7 and 2.4 <= self.axisX <= 3.7:
            music.play(0)

        print self.axisX
        print self.axisZ

        glutPostRedisplay()

class ArqGrade:

    def __init__(self):
        self.obj = GLuint()

    def grade(self, qtd):
        glRotate(-90,1,0,0)
        glPushMatrix()
        glColor(0,0,0)
        for i in range(qtd):
            glutSolidCylinder(0.08, (i+1), 10, 10)
            glTranslate(1,0,0)
        glPopMatrix()
        glRotate(90,1,0,0)

    def bancos(self, qtd):
        glPushMatrix()
        glScale(.5,.4,2)
        glColor(1,1,1)
        for i in range(qtd):
            glutSolidCube(0.5)
            glTranslate(0.5,0,0)
        glPopMatrix()

    def refletor(self):

        #Base Vertical.
        glRotatef(90, 1.0, 0.0 , 0.0)
        glColor3f(0.5,0.5,0.5)
        glutSolidCylinder(0.07, 10.0, 40, 10)
        glRotatef(5, 1.0, 0.0 , 0.0)
        #Base Luzes.
        glTranslate( -0.75, 0.0, -1.02)

        glColor3f(0.8, 0.8, 0.8) # cor RGB
        #Luzes do meio.
        contador = 0
        glTranslate( -0.1, 0.1, 0.5)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1

        #Luzes de cima.
        contador = 0
        glTranslate( -1.5, 0.0, 0.3)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)#Nao altera. Definir espaco entre as lampadas.
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1

        #Luzes de baixo.
        contador = 0
        glTranslate( -1.5, 0.0, -0.6)
        while(contador < 6):
            glTranslate( 0.25, 0.0, 0.0)#Nao altera.Definir espaco entre as lampadas.
            glutWireCube(0.18,100)
            glutSolidCube(0.15)
            contador += 1


        glTranslate( -0.65, -0.1, 0.3)
        glPushMatrix()
        glColor3f(1, 1, 1) # cor RGB
        glScalef(3.5, 0.2, 2.0)
        glutWireCube(0.52)
        glPopMatrix()

        #Fios que seguram as lampadas.
        glPushMatrix()
        glRotatef(90, 0.0, 1.0 , 0.0)
        glTranslate( -0.3, 0.0, -0.92)
        for s in range(3):
            glutSolidCylinder(0.008, 1.83, 10, 1)
            glTranslate( 0.3, 0, 0)
        glPopMatrix()

    def corrimao(self):
        # CORRIMÃO

        glPushMatrix()
        glColor3f(0.3,0.3,0.3)
        glTranslate(-0.6,3.5,17)
        glutSolidCylinder(0.01, 3.4, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.8,0.8,0.8)
        glTranslate(-0.6,3.4,17)
        glutSolidCylinder(0.01, 3.4, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.8,0.8,0.8)
        glTranslate(-0.6,3.3,17)
        glutSolidCylinder(0.01, 3.4, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.3,0.3,0.3)
        glRotate(90, 1.0, 0.0, 0.0)
        glTranslate(-0.6,18,-3.5)
        glutSolidCylinder(0.01, 0.5, 40, 10)
        glPopMatrix()

    def corrimaoCima(self):
        # CORRIMÃO

        glPushMatrix()
        glColor3f(0.3,0.3,0.3)
        glTranslate(-0.6,3.5,17)
        glutSolidCylinder(0.02, 3.4, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.8,0.8,0.8)
        glTranslate(-0.6,3.4,17)
        glutSolidCylinder(0.02, 3.4, 40, 10)
        glPopMatrix()

        glPushMatrix()
        glColor3f(0.8,0.8,0.8)
        glTranslate(-0.6,3.3,17)
        glutSolidCylinder(0.02, 3.4, 40, 10)
        glPopMatrix()


    def desenhar(self):
        self.obj = glGenLists(11)
        glNewList(self.obj, GL_COMPILE)
        glPushMatrix()
        glScale(.2,.2,.2)
        glTranslate(45,-5,-70)

        # PISO PASSAGEM
        glPushMatrix()
        glTranslate(0,1,82)
        glRotate(90,0,1,0)

        for i in range(1):
            glScale(1,1,2)

            self.bancos(327)

        glPopMatrix()

        glPushMatrix()
        glTranslate(2,-15,-85)
        glScale(5,5,5)
        for i in range(14):
            self.corrimao()
            glTranslate(0,0,1)
        glPopMatrix()

        # CORRIMAO DE CIMA

        glPushMatrix()
        glTranslate(12.4,-7,-85)
        glScale(5,5,5)
        for i in range(14):
            self.corrimaoCima()
            glTranslate(0,0,1)
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.4,1,82)
        glRotate(90,0,1,0)
        for i in range(9):
            if i % 2 == 0:
                glColor3f(0.2,0.2,0.2)
            else:
                glColor3f(0.8,0.8,0.8)
            self.bancos(328)
            glTranslate(0,1,1)
        glPopMatrix()

        # CORRIMAO LADO ESQ

        glPushMatrix()
        glTranslate(-43.2,-53.5,-2.2)
        glScale(4,4,4)
        glRotate(90, 0,1,0)
        glRotate(-41, 1,0,0)
        for i in range(1):
            self.corrimaoCima()
            glTranslate(0,0,1)
        glPopMatrix()

        # CORRIMAO LADO DIR

        glPushMatrix()
        glTranslate(-43.2,-53.5,79.7)
        glScale(4,4,4)
        glRotate(90, 0,1,0)
        glRotate(-41, 1,0,0)
        for i in range(1):
            self.corrimaoCima()
            glTranslate(0,0,1)
        glPopMatrix()



        for i in range(42):
            glPushMatrix()
            self.grade(10)
            glRotate(-180,0,1,0)
            glRotate(-90,0,0,1)
            glTranslate(-9,-9,0)
            self.grade(10)
            glPopMatrix()
            glTranslate(0,0,2)
        glPopMatrix()

        # REFLETOR DIREITO
        glPushMatrix()
        glTranslate(12.5,3,-10)
        glRotatef(-90, 0,1,0)
        glScalef(0.5,0.5,0.5)
        self.refletor()
        glPopMatrix()

        # REFLETOR ESQUERDO
        glPushMatrix()
        glTranslate(12.5,3,0)
        glRotatef(-90, 0,1,0)
        glScalef(0.5,0.5,0.5)
        self.refletor()
        glPopMatrix()

        glEndList()


    def executar(self):
        glCallList(self.obj)

class ArqFrente:

    def __init__(self):
        self.obj = GLuint()

    def cobertura(self):
        glPushMatrix()

        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(14.0, 0.0, 0.0)
        glVertex3f(14.0, 1.0, 0.0)
        glVertex3f(13.0, 1.0, 0.0)
        glVertex3f(13.0, 2.0, 0.0)
        glVertex3f(12.0, 2.0, 0.0)
        glVertex3f(12.0, 3.0, 0.0)
        glVertex3f(11.0, 3.0, 0.0)
        glVertex3f(11.0, 4.0, 0.0)
        glVertex3f(10.0, 4.0, 0.0)
        glVertex3f(10.0, 5.0, 0.0)
        glVertex3f(9.0, 5.0, 0.0)
        glVertex3f(9.0, 6.0, 0.0)
        glVertex3f(8.0, 6.0, 0.0)
        glVertex3f(8.0, 7.0, 0.0)
        glVertex3f(7.0, 7.0, 0.0)
        glVertex3f(7.0, 8.0, 0.0)
        glVertex3f(6.0, 8.0, 0.0)
        glVertex3f(6.0, 9.0, 0.0)
        glVertex3f(5.0, 9.0, 0.0)
        glVertex3f(5.0, 10.0, 0.0)
        glVertex3f(4.0, 10.0, 0.0)
        glVertex3f(4.0, 11.0, 0.0)
        glVertex3f(3.0, 11.0, 0.0)
        glVertex3f(3.0, 12.0, 0.0)
        glVertex3f(2.0, 12.0, 0.0)
        glVertex3f(2.0, 13.0, 0.0)
        glVertex3f(1.0, 13.0, 0.0)
        glVertex3f(1.0, 14.0, 0.0)
        glVertex3f(0.0, 14.0, 0.0)

        glEnd()

        glPopMatrix()

    def degrau(self,tamanho):
        glPushMatrix()
        glScalef(2, tamanho, 1.0)
        glutSolidCube(0.5)
        glPopMatrix()

    def escadinha(self):
        contador = 0
        glPushMatrix()
        glTranslate(-10,0,-6.95)
        while contador < 13:
            glPushMatrix()
            glScalef(0.5,0.05,0.5)
            self.degrau(100)
            glPopMatrix()
            glTranslate(0.8,0,0.5)
            contador+=1
        glPopMatrix()



    def arquibancada(self):
        #Apenas para testar com zoom, porem poderia se tornar definitivo.
        glScalef(0.2,0.2,0.2)


        # Parte Alta Esquerda
        glPushMatrix()
        glScalef(0.9,1.1,1.1)
        glTranslate(0,0,0)
        glRotatef(90, 1.0, 0.0, 0.0)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 14:
            if contador%2==0:
                glColor3f(1,1,1)
                self.degrau(300)
                glTranslate(0.8,0,0.5)
            else:
                glColor3f(0.0,0.0,0.0)
                self.degrau(300)
                glTranslate(0.8,0,0.5)
            contador+=1

        #Escadinha aux.    
        glPushMatrix()
        glColor3f(1,1,0)
        glTranslate(-0.5,50,0.1)
        self.escadinha()
        glTranslate(0,-100,0)
        self.escadinha()
        glPopMatrix()

        #Costa.
        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-12.5,-0.5,-4)
        glScalef(0.5, 1.02, 15)
        self.degrau(300)
        glPopMatrix()

        glPopMatrix()

        #Cobertura lateral.
        glPushMatrix()
        glTranslate(-0.6,-8.05,24.4) # nao altera, sobe e desce, frente e tras.
        glScalef(0.75, 0.6,0.9)
        self.cobertura()
        glTranslate(0.0,0.0,-54.6)
        self.cobertura()
        glPopMatrix()

    def arquibancada2(self):

        #Apenas para testar com zoom, porem poderia se tornar definitivo.
        glScalef(0.2,0.2,0.2)


        # Parte Alta Esquerda
        glPushMatrix()
        glScalef(0.9,1.1,1.1)
        glTranslate(0,0,0)
        glRotatef(90, 1.0, 0.0, 0.0)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 8:
            if contador%2==0:
                glColor3f(1,1,1)
                self.degrau(125)
                glTranslate(0.8,0,0.5)
            else:
                glColor3f(0.0,0.0,0.0)
                self.degrau(125)
                glTranslate(0.8,0,0.5)
            contador+=1
        glPopMatrix()

        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-0,-2,-2)
        glScalef(1, 0.06, 32)
        self.degrau(150)
        glPopMatrix()

    def desenho(self):
        glPushMatrix()
        self.arquibancada()
        glPopMatrix()

        glPushMatrix()
        glTranslate(0,0,13)
        self.arquibancada()
        glPopMatrix()
        glTranslate(0,0,7)
        self.arquibancada2()


    def desenhar(self):
        self.obj = glGenLists(1)
        glNewList(self.obj, GL_COMPILE)
        glPushMatrix()
        glTranslate(6,.1,-16.3)
        glScalef(0.45,.7,.5)
        glRotatef(-90,0,1,0)


        self.desenho()

        glPopMatrix()
        glEndList()

    def executar(self):
        glCallList(self.obj)


class ArqTras:

    def __init__(self):
        self.obj = GLuint()

    def cobertura(self):
        glPushMatrix()

        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(14.0, 0.0, 0.0)
        glVertex3f(14.0, 1.0, 0.0)
        glVertex3f(13.0, 1.0, 0.0)
        glVertex3f(13.0, 2.0, 0.0)
        glVertex3f(12.0, 2.0, 0.0)
        glVertex3f(12.0, 3.0, 0.0)
        glVertex3f(11.0, 3.0, 0.0)
        glVertex3f(11.0, 4.0, 0.0)
        glVertex3f(10.0, 4.0, 0.0)
        glVertex3f(10.0, 5.0, 0.0)
        glVertex3f(9.0, 5.0, 0.0)
        glVertex3f(9.0, 6.0, 0.0)
        glVertex3f(8.0, 6.0, 0.0)
        glVertex3f(8.0, 7.0, 0.0)
        glVertex3f(7.0, 7.0, 0.0)
        glVertex3f(7.0, 8.0, 0.0)
        glVertex3f(6.0, 8.0, 0.0)
        glVertex3f(6.0, 9.0, 0.0)
        glVertex3f(5.0, 9.0, 0.0)
        glVertex3f(5.0, 10.0, 0.0)
        glVertex3f(4.0, 10.0, 0.0)
        glVertex3f(4.0, 11.0, 0.0)
        glVertex3f(3.0, 11.0, 0.0)
        glVertex3f(3.0, 12.0, 0.0)
        glVertex3f(2.0, 12.0, 0.0)
        glVertex3f(2.0, 13.0, 0.0)
        glVertex3f(1.0, 13.0, 0.0)
        glVertex3f(1.0, 14.0, 0.0)
        glVertex3f(0.0, 14.0, 0.0)

        glEnd()

        glPopMatrix()

    def degrau(self):
        glPushMatrix()
        glScalef(2, 300, 1.0)
        glutSolidCube(0.5)
        glPopMatrix()

    def escadinha(self):
        contador = 0
        glPushMatrix()
        glTranslate(-10,0,-6.95)
        while contador < 13:
            glPushMatrix()
            glScalef(0.5,0.05,0.5)
            self.degrau()
            glPopMatrix()
            glTranslate(0.8,0,0.5)
            contador+=1
        glPopMatrix()



    def arquibancada(self):
        #Apenas para testar com zoom.
        glScalef(0.3,0.3,0.3)


        # Parte Alta Esquerda
        glPushMatrix()
        glScalef(0.9,1.1,1.1)
        glTranslate(0,0,0)
        glRotatef(90, 1.0, 0.0, 0.0)
        contador = 0
        glScalef(1, 0.3, 1)
        while contador <= 14:
            if contador%2==0:
                glColor3f(1,1,1)
                self.degrau()
                glTranslate(0.8,0,0.5)
            else:
                glColor3f(0.0,0.0,0.0)
                self.degrau()
                glTranslate(0.8,0,0.5)
            contador+=1

        #Escadinha aux.    
        glPushMatrix()
        glColor3f(1,1,0)
        glTranslate(-0.5,50,0.1)

        glPushMatrix()
        glScalef(1,.3,1)
        self.escadinha()
        glPopMatrix()

        glTranslate(0,-50,0)

        glPushMatrix()
        glScalef(1,.3,1)
        self.escadinha()
        glPopMatrix()

        glTranslate(0,-50,0)

        glPushMatrix()
        glScalef(1,.3,1)
        self.escadinha()
        glPopMatrix()

        glPopMatrix()

        #Costa.
        glPushMatrix()
        glColor3f(1,1,1)
        glTranslate(-12.5,-0.5,-4)
        glScalef(0.5, 1.02, 15)
        self.degrau()
        glPopMatrix()

        glPopMatrix()

        #Cobertura lateral.
        glPushMatrix()
        glTranslate(-0.5,-8.1,24.8) # nao altera, sobe e desce, frente e tras.
        glScalef(0.8, 0.6,1)
        self.cobertura()
        glTranslate(0.0,0.0,-49.6)
        self.cobertura()
        glPopMatrix()

    def desenhar(self):
        self.obj = glGenLists(9)
        glNewList(self.obj, GL_COMPILE)
        
        glPushMatrix()
        glTranslate(3,.2,5.5)
        glScalef(0.65,.5,.5)
        glRotatef(90,0,1,0)

        self.arquibancada()
        
        glPopMatrix()
        glEndList()

    def executar(self):
        glCallList(self.obj)


#----------------------------------------------------------------
class Grade:
    def __init__(self):
        self.obj = GLuint()

    def estrutura(self):

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

    def grade(self):

        glPushMatrix()

        glPushMatrix()
        self.estrutura()

        glTranslate( 0.0, 5.0, 0.0)
        glRotatef(125,.0,.1,.0)
        glScalef(1.0, 1.0, 0.4)
        self.estrutura()
        glPopMatrix()

        glTranslate( 0.0, -5.0, 2.5)
        glScalef(1,3,10.5)
        glColor(0,0,0)
        glutSolidCube(0.5)

        glPopMatrix()

    def curva(self):
        glPushMatrix()

        self.grade()
        glTranslate(0,0,5.1)

        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(15,0,1,0)
        self.grade()
        glPopMatrix()

        glTranslate(1.3,0,2.4)
        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(30,0,1,0)
        self.grade()
        glPopMatrix()

        glTranslate(2.6,0,2.1)
        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(45,0,1,0)
        self.grade()
        glPopMatrix()

        glTranslate(3.5,0,1.6)
        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(60,0,1,0)
        self.grade()
        glPopMatrix()

        glTranslate(4.3,0,1.2)
        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(75,0,1,0)
        self.grade()
        glPopMatrix()

        glTranslate(4.7,0,.5)
        glPushMatrix()
        glScalef(1,1,0.5)
        glRotatef(90,0,1,0)
        self.grade()
        glPopMatrix()

        glPopMatrix()

    def seguimento(self, qtd):
        for i in range(qtd):
            glTranslate(0,0,5)
            glPushMatrix()
            glPushMatrix()
            glColor(0,0,0)
            self.estrutura()

            glTranslate( 0.0, 5.0, 0.0)
            glRotatef(125,.0,.1,.0)
            glScalef(1.0, 1.0, 0.4)
            self.estrutura()
            glPopMatrix()

            glTranslate( 0.0, -5.0, 2.5)
            glScalef(1,3,10.5)
            glColor(0,0,0)
            glutSolidCube(0.5)
            glPopMatrix()

    def desenhar(self):
        self.obj = glGenLists(2)
        glNewList(self.obj,GL_COMPILE)
        glPushMatrix()
        glColor(0,0,0)
        glScale(.2,.1,.175)
        glTranslate(-11,-7.45,-77)
        glScalef(.5,.5,.5)
        glPushMatrix()
        qtd = 0
        for i in range(4):
            if i%2 == 0:
                qtd = 36
            else:
                qtd = 15
            self.seguimento(qtd)
            self.curva()
            glTranslate(16,0,13)
            glRotatef(90,0,1,0)
        glPopMatrix()
        glPopMatrix()
        glEndList()

    def executar(self):
        glCallList(self.obj)