from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = []
width = 800
height = 800
WIN_LEFT_BIT = 0x01
WIN_RIGHT_BIT = 0x02
WIN_BOTTOM_BIT = 0x04
WIN_TOP_BIT = 0x08

xmin=60
ymin=60
xmax=200
ymax=200

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def drawLine(p1=Point, p2=Point):
    glColor3f(1, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2i(round(p1.x), round(p1.y))
    glVertex2i(round(p2.x), round(p2.y))
    glEnd()
    glFlush()

def Ma(M=Point ):
    m=0
    if M.x< xmin :  
        m|= 1
    if M.x> xmax :  
        m|= 2
    if M.y< ymin :  
        m|= 4
    if M.y> ymax :  
        m|= 8
    return m

def BinaryClip(A = Point ,B = Point ):
    P = Point
    Q = Point
    M = Point
    print(A.x,A.y,B.x,B.y)
    if (Ma(A) | Ma(B))==0 :
        drawLine(A,B)
    if (Ma(A) & Ma(B)) != 0:
        return
    if (Ma(A) != 0) & (Ma(B) == 0):
        A, B = B, A
    if (Ma(A) == 0) & (Ma(B) != 0):
        P=A 
        Q=B
        while ((abs(P.x-Q.x)+abs(P.y-Q.y)) > 2) :
            M.x=(P.x+Q.x)/2  
            M.y=(P.y+Q.y)/2
            if Ma(M)==0 : 
                P=M
            else:      
                Q=M
        drawLine(A,P)
    if ((Ma(A) != 0) & (Ma(B) != 0)) & ((Ma(A) & Ma(B))==0) :
        P=A 
        Q=B
        M.x=(P.x+Q.x)/2 
        M.y=(P.y+Q.y)/2
        while (Ma(M)!=0) & ((abs(P.x-Q.x)+abs(P.y-Q.y)) > 2):
            if (Ma(P) & Ma(M))!=0 :
                P=M
            else:
                Q=M
            M.x=(P.x+Q.x)/2  
            M.y=(P.y+Q.y)/2
        if Ma(M)==0:
            BinaryClip(P,M)
            BinaryClip(M,Q)

def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def draw_window():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(xmin, ymin)
    glVertex2i(xmin, ymax)
    glVertex2i(xmax, ymax)
    glVertex2i(xmax, ymin)
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    draw_window()
    if len(listPoint) == 2:
        P1 = Point(listPoint[0][0],listPoint[0][1])
        P2 = Point(listPoint[1][0],listPoint[1][1])
        BinaryClip(P1, P2)

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Cohen Sutherland Drawing Algorithm")
    gluOrtho2D(-width/2, height/2, -height/2, width/2)
    glutDisplayFunc(display)
    glutMouseFunc(MouseEventHandler)
    glutMainLoop()
