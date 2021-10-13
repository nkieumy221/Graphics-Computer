from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

listPoint = []
width = 800
height = 800
WIN_LEFT_BIT = 0x01;
WIN_RIGHT_BIT = 0x02;
WIN_BOTTOM_BIT = 0x04;
WIN_TOP_BIT = 0x08;

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def encode(p1=Point , win_min= Point , win_max= Point) :
    code = 0x00;
    if p1.x < win_min.x :
        code |= WIN_LEFT_BIT
    if p1.x > win_max.x :
        code |= WIN_RIGHT_BIT
    if p1.y < win_min.y :
        code |= WIN_BOTTOM_BIT
    if p1.y > win_max.y :
        code |= WIN_TOP_BIT
    return code

def line_clip(p1=Point ,p2=Point , win_min= Point , win_max= Point) :
    done = 0
    plot_line = 0
    m = 0
    if p1.x != p2.x :
        m = (p2.y - p1.y) / (p2.x - p1.x)
    while not done :
        code1 = encode(p1, win_min, win_max)
        code2 = encode(p2, win_min, win_max)
        if not (code1 | code2):
            done = 1
            plot_line = 1
        elif code1 & code2:
            done = 1
        else:
            if not code1:
                p1, p2 = p2, p1
                code1, code2 = code2, code1
            if code1 & WIN_LEFT_BIT :
                p1.y += (win_min.x - p1.x) * m
                p1.x = win_min.x
            elif code1 & WIN_RIGHT_BIT :
                p1.y += (win_max.x - p1.x) * m
                p1.x = win_max.x
            elif code1 & WIN_BOTTOM_BIT :
                if p1.x != p2.x :
                    p1.x += (win_min.y - p1.y) / m
                p1.y = win_min.y
            elif code1 & WIN_TOP_BIT :
                if p1.x != p2.x :
                    p1.x += (win_max.y - p1.y) / m
                p1.y = win_max.y
    if plot_line :
        glColor3f(1, 0, 0)
        glLineWidth(2)
        glBegin(GL_LINES)
        glVertex2i(round(p1.x), round(p1.y))
        glVertex2i(round(p2.x), round(p2.y))
        glEnd()
        glFlush()

def MouseEventHandler(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if len(listPoint) == 2:
            listPoint.clear()
        listPoint.append([(int)(x-width/2), (int)(height/2-y)])
        print(listPoint)
        glutPostRedisplay()

def draw_window(win_min=Point ,win_max=Point ):
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(round(win_min.x), round(win_min.y))
    glVertex2i(round(win_min.x), round(win_max.y))
    glVertex2i(round(win_max.x), round(win_max.y))
    glVertex2i(round(win_max.x), round(win_min.y))
    glEnd()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    win_min = Point(60, 60)
    win_max = Point(200, 200)
    draw_window(win_min, win_max)
    
    if len(listPoint) == 2:
        A = Point(listPoint[0][0],listPoint[0][1])
        B = Point(listPoint[1][0],listPoint[1][1])
        line_clip(A, B, win_min, win_max)
    

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
