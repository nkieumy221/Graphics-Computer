from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = []
width = 600
height = 600


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex3i(x, y, 0)
    glEnd()

def put8pixel(xc, yc, x, y) :
    draw_pixel( x+xc, y+yc)
    draw_pixel( y+xc, x+yc)
    draw_pixel( y+xc,-x+yc)
    draw_pixel( x+xc,-y+yc)
    draw_pixel(-x+xc,-y+yc)
    draw_pixel(-y+xc,-x+yc)
    draw_pixel(-y+xc, x+yc)
    draw_pixel(-x+xc, y+yc)
    
def draw_cricle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2*r
    while x <=y:
        put8pixel(xc,yc,x,y)
        if p < 0:  
            p+=4*x+6
        else:  
            p+=4*(x-y)+10
            y-=1
        x+=1

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
        draw_cricle(listPoint[0][0], listPoint[0][1],
                  100)
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
