from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
sys.setrecursionlimit(15000)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)

def setpixel(x, y, colour):
    glColor3f(colour[0], colour[1], colour[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def boundary(x, y, border, fill):
    colour = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (colour != border).any() and (colour != fill).any():
        setpixel(x, y, fill)
        boundary(x+1, y, border, fill)
        boundary(x-1, y, border, fill)
        boundary(x, y+1, border, fill)
        boundary(x, y-1, border, fill)

def flood(x, y, bg, fill):
    colour = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (colour == bg).all() and (colour != fill).any():
        setpixel(x, y, fill)
        flood(x+1, y, bg, fill)
        flood(x-1, y, bg, fill)
        flood(x, y+1, bg, fill)
        flood(x, y-1, bg, fill)

def mouse(btn, state, x, y):
    y = 500 - y
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fill = [1,0,0]
        border = [1,1,1]
        boundary(x, y, border, fill)
    elif btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        fill = [0,0,1]
        bg = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
        flood(x, y, bg, fill)

def square():
    glLineWidth(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(10,10)
    glVertex2i(60,10)
    glVertex2i(60,60)
    glVertex2i(10,60)
    glEnd() 
    glBegin(GL_LINE_LOOP)
    glVertex2i(10,80)
    glVertex2i(60,80)
    glVertex2i(60,130)
    glVertex2i(10,130)
    glEnd()
    glFlush()

def main():
    print("Click left mouse button for flood filling-blue colour.")
    print("Click right mouse button for boundary filling-red colour.")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Seed Filling Algorithms")
    init()
    glutDisplayFunc(square)
    glutMouseFunc(mouse)
    glutMainLoop()

main()