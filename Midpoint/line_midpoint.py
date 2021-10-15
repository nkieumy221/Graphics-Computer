from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

listPoint = []
width = 600
height = 600

def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex3i(x, y, 0)
    glEnd()

def LineMidPoint(x1,y1,x2,y2) :	
    Dx = x2-x1 
    Dy = y2-y1
    p = 2*Dy-Dx
    x = x1	
    y = y1
    draw_pixel(x, y)
    while x < x2:  
        if p <0:	 
            p+= 2*Dy
        else:
            p+=2*(Dy-Dx)
            y+=1
        x+=1
        draw_pixel(x, y)
  	
def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def mydisplay() :
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 2:
        LineMidPoint(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()

def main() :
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("DEMO THUAT TOAN VE DOAN THANG - BRESENHAM")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(mydisplay)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
 
main()
