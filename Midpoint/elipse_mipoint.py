from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
def initGL() :
	glClearColor(1.0, 1.0, 1.0, 1.0) #R=0,G=0,B=0, anpha=1
	glOrtho(-320,320,-240,240,-1,1)	

def draw4point(xc, yc, x, y) :
    glBegin(GL_POINTS)
    glVertex2i(x + xc, y + yc)
    glVertex2i(x + xc,-y + yc)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc - x, yc + y)
    glEnd()

def EllipsMidpoint(xc,yc,a, b ) :	
    x = 0
    y = b 
    x0 = a*a/math.sqrt(a*a + b*b) 
    P = b*b - a*a*b +a*a/4
    draw4point(xc,yc,x,y)
    while x <= x0:
        if P <0 :	
            P += (b*b)*(2*x + 3)
        else:
            P += (b*b)*(2*x+3) - 2*a*a*(y-1)
            y-=1
        x+=1
        draw4point(xc,yc,x,y)
    x=a
    y=0

    P = a*a - b*b*a +b*b/4
    draw4point(xc,yc,x,y)
    while x > x0:
        if P <0:
            P +=(a*a)*(2*y + 3)
        else:	
            P += (a*a)*(2*y+3) - 2*b*b*(x-1)           
            x-=1
        y+=1
        draw4point(xc,yc,x,y)

def mydisplay() :
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    EllipsMidpoint(0, 0, 300,200) #Tâm C(0,0) bán kính 200
    glViewport(0,0,640,480)
    glFlush()


def main():
    glutInit()
    mode=GLUT_SINGLE | GLUT_RGB
    glutInitDisplayMode(mode)

    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("DEMO THUAT TOAN VE DUONG ELLIPSE - MIDPOINT")
        
    initGL()
    glutDisplayFunc(mydisplay)    
    glutMainLoop()
main()