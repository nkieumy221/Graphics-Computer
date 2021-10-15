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

def draw_line(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    x = x1
    y = y1
    
    if (dx < 0): 
        dx = -dx
    if (dy < 0): 
        dy = -dy
    incx = 1
    if (x2 < x1): 
        incx = -1
    incy = 1
    if (y2 < y1):
        incy = -1   

    if (dx > dy):
        draw_pixel(x, y)
        e = 2 * dy-dx
        inc1 = 2*(dy-dx)
        inc2 = 2*dy
        print(dx)
        for i in range(dx) :
            if (e >= 0):
                y += incy
                e += inc1
            else:
                e += inc2
            x += incx
            draw_pixel(x, y)

    else :
        draw_pixel(x, y)
        e = 2*dx-dy
        inc1 = 2*(dx-dy)
        inc2 = 2*dx
        print(dy)
        for i in range(dy) :
            if (e >= 0) :
                x += incx
                e += inc1
            else :
                e += inc2
            y += incy
            draw_pixel(x, y)


def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    if len(listPoint) == 2:
        draw_line(listPoint[0][0], listPoint[0][1],
                  listPoint[1][0], listPoint[1][1])
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Breshnam's Line Drawing Algorithm")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
