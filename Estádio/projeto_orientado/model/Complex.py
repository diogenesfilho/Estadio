__author__ = 'pedro'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image, ImageFilter

class Placar:

    def __init__(self):
        self.textura1 = glGenTextures(1)

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
        glPushMatrix()
        glTranslatef(8, 0.6, 8)
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
        glScalef(25,15,1)
        glTranslate(0.25,1.7,0)
        glutSolidCube(1)
        glPopMatrix()

        # Textura placar
        self.carrega_imagem()

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
        glPopMatrix()

class Campo:

    def __init__(self):
        self.textura1 = glGenTextures(1)

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
        glScalef(1, 1, 3)
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

        #Isolando para que nao aja problemas quando rotacionar e transladar.
        glPushMatrix()
        glColor3f(1, 1, 1)
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
        alturaRede = 3
        glScalef(1, 1, alturaRede)
        glColor3f(0.2, 0.2, 0.2)
        glutSolidCylinder(0.08, 5, 100, 50)
        distanciaEntreTraves = -15
        glTranslate( 0.0, distanciaEntreTraves, 0.0)
        glutSolidCylinder(0.05, 5, 30, 30)
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
        glutSolidCylinder(0.01, 0.3, 30, 30)
        glPopMatrix()

        glPushMatrix()
        glColor3f(1, 1, 0)
        glScalef(0.01, 0.1, 0.2)
        glTranslate(-110, -7, 8.6)
        glutSolidCube(1)
        glPopMatrix()

    def desenhar(self):
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

class Bola:

    def __init__(self):
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

        if tecla == b'a':
            self.esqdir += - 20
            self.axisX -= .1

        if tecla == b's':
            self.cimabaixo += - 20
            self.axisZ += .1

        if tecla == b'w':
            self.cimabaixo += + 20
            self.axisZ -= .1

        if tecla == b'd':
            self.esqdir += + 20
            self.axisX += .1

        glutPostRedisplay()