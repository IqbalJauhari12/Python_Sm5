import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)
    
def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 280)
    glVertex2i(7, 160)
    glVertex2i(150, 160)
    glEnd()
    
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(80, 135)
    glVertex2i(7, 10)
    glVertex2i(150, 10)
    glEnd()
    glFlush()    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Iqbal")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()
main()
