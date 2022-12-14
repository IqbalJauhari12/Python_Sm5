import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-300, 300.0, -300, 300.0)

def drawDiamond():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 280)
    glVertex2i(80, 160)
    glVertex2i(150, 160)
    glEnd()
    
    glColor3f(0.37,0.62,0.7)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 280)
    glVertex2i(80, 160)
    glVertex2i(10, 160)
    glEnd()
 
    glColor3f(0.37,0.62,0.7)
    glBegin(GL_TRIANGLES)
    glVertex2i(150, 160)
    glVertex2i(80, 160)
    glVertex2i(80, 20)
    glEnd()
    
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 160)
    glVertex2i(10, 160)
    glVertex2i(80, 20)
    glEnd()
    glFlush()
    
initRotAngle = 0.0
def animRotate ():
    global initRotAngle
    glPushMatrix()
    glRotate(initRotAngle,0,0,-1)
    drawDiamond()
    initRotAngle = initRotAngle + 1
    glPopMatrix()
    glFlush()

def Timer():
    glutPostRedisplay()
    glutTimerFunc(10,Timer,5)
    glFlush()
    
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    animRotate()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Iqbal")
    glutDisplayFunc(render)
    glutTimerFunc(10, Timer, 5)
    init()
    glutMainLoop()
main()
