from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math 

listPoint = []
width = 600
height = 600


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex3i(x, y, 0)
    glEnd()

def put4pixel(xc, yc, x, y) :
    draw_pixel( x+xc, y+yc)
    draw_pixel( x+xc,-y+yc)
    draw_pixel( xc-x, yc-y)
    draw_pixel( xc-x, yc+y)
    
def draw_elipse(xc, yc, a, b):
    a2=a*a 
    b2=b*b
    x=0  
    y=b  
    p=-2*b+1 + 2*b2/(a2)
    x0=a2/(math.sqrt(a2+b2)) 
    y0=b2/(math.sqrt(a2+b2))
    while (x<=x0):
        put4pixel(xc,yc, x, y)
        if p<0 : 
            p+=2*b2*(2*x+3)/a2
        else:
            p+=4*(1-y)+ 2*b2 * (2*x+3)/a2
            y-=1
        x+=1
        

    x=a;  y=0;  p=2*a2/b2 - 2*a+1
    while (y<=y0):
        put4pixel(xc,yc,x,y)
        if (p<0 ) : 
            p+=2*a2*(2*y+3)/b2
        else :
            p+=4*(1-x) + 2*a2*(2*y+3)/b2
            x-=1
        y+=1

def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 1:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 1:
        draw_elipse(listPoint[0][0], listPoint[0][1],
                  100, 200)
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Breshnam's Cricle Drawing Algorithm")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
