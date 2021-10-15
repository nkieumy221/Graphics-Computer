from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0) #R=0,G=0,B=0, anpha=1
    glOrtho(-320,320,-240,240,-1,1)	
    
def draw8point(xc, yc, x, y):
    glBegin(GL_POINTS)
    glVertex2i(xc + x, yc + y)
    glVertex2i(xc + y, yc + x)
    glVertex2i(xc + y, yc - x)
    glVertex2i(xc + x, yc - y)
    glVertex2i(xc - x, yc - y)
    glVertex2i(xc - y, yc - x)
    glVertex2i(xc - y, yc + x)
    glVertex2i(xc - x, yc + y)
    glEnd()

def CircleMidpoint(xc,yc,R ): 
    y = R 
    x = 0
    P = 5/4 - R
    draw8point(xc,yc,x,y)
    while x < y :
        if P <0 :	
            # Chon diem P
            P += 2*x + 3 
        else :     
            # Chon diem S
            P += 2*(x - y) + 5
            y-=1
        x+=1
        draw8point(xc,yc,x,y)
		
def mydisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    CircleMidpoint(0, 0, 200) #Tâm C(0,0) bán kính 200
    glViewport(0,0,640,480)
    glFlush()



def main():
    glutInit()
    mode=GLUT_SINGLE | GLUT_RGB
    glutInitDisplayMode(mode)

    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("DEMO THUAT TOAN VE DUONG TRON - MIDPOINT")
    initGL()
    glutDisplayFunc(mydisplay)    
    glutMainLoop()
main()