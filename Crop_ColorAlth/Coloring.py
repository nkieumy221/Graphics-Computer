from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

color = [3]
def delay(ms):
    ms + time.sleep(3)

def init():
    glClearColor(1.0,1.0,1.0,0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0,640,0,480)

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex3i(x, y, 0)
    glEnd()

def bound_it(x, y,fillColor,bc):  
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()
    if((color[0]!=bc[0] | color[1]!=bc[1] | color[2]!=bc[2])&(
        color[0]!=fillColor[0] | color[1]!=fillColor[1] | color[2]!=fillColor[2])):
        glColor3f(fillColor[0],fillColor[1],fillColor[2])
        glBegin(GL_POINTS)
        glVertex2i(x,y)
        glEnd()
        glFlush()
        bound_it(x+1,y,fillColor,bc)
        bound_it(x-2,y,fillColor,bc)
        bound_it(x,y+2,fillColor,bc)
        bound_it(x,y-2,fillColor,bc)
    
def mouse(btn, state, x, y):
    y = 480-y
    bCol =[3]
    if btn == GLUT_LEFT_BUTTON :
        if state==GLUT_DOWN:
            bCol.append([[1,0,0]])
            color.append([[0,0,1]])
            bound_it(x,y,color,bCol)
        
def world():
    glLineWidth(3)
    glPointSize(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(150,100)
    glVertex2i(300,300)
    glVertex2i(450,100)
    glEnd()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(200,200)
    glutCreateWindow("Many Amaze Very GL WOW")
    glutDisplayFunc(world)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()
