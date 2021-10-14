from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def initGL():
	glClearColor(1.1, 1.0, 1.0, 1.0) 
	glOrtho(-2,2,-2,2,-1,1)	

vertices =[1.5, 1.5,0, 1.5,0, 0,1.5, 0]
def draw():
    glBegin(GL_POLYGON)
    glVertex2f(vertices[0], vertices[1])
    glVertex2f(vertices[2], vertices[3])
    glVertex2f(vertices[4], vertices[5])
    glVertex2f(vertices[6], vertices[7])
    glEnd()
    glFlush()

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, .5, .25)
	draw()

def rotate(heso):
    M_1_PI = 1 /math.pi
    vertices[0]= vertices[0] * math.cos(heso*(M_1_PI/180)) - vertices[1] * math.sin(heso*(M_1_PI/180))
    vertices[2]= vertices[2] * math.cos(heso*(M_1_PI/180)) - vertices[3] * math.sin(heso*(M_1_PI/180))
    vertices[4]= vertices[4] * math.cos(heso*(M_1_PI/180)) - vertices[5] * math.sin(heso*(M_1_PI/180))
    vertices[6]= vertices[6] * math.cos(heso*(M_1_PI/180)) - vertices[7] * math.sin(heso*(M_1_PI/180))

    vertices[1]= vertices[0] * math.sin(heso*(M_1_PI/180))+ vertices[1] * math.cos(heso*(M_1_PI/180))
    vertices[3]= vertices[2] * math.sin(heso*(M_1_PI/180))+ vertices[3] * math.cos(heso*(M_1_PI/180))
    vertices[5]= vertices[4] * math.sin(heso*(M_1_PI/180))+ vertices[5] * math.cos(heso*(M_1_PI/180))
    vertices[7]= vertices[6] * math.sin(heso*(M_1_PI/180))+ vertices[7] * math.cos(heso*(M_1_PI/180))
    draw()
 
#Tinh tien theo truc Y:
def changeY(heso_tinh_tien):
	vertices[0] += heso_tinh_tien
	vertices[2] += heso_tinh_tien
	vertices[4] += heso_tinh_tien
	vertices[6] += heso_tinh_tien
	draw()
 
#Tinh tien theo truc X:
def changeX(heso_tinh_tien):
	vertices[1] += heso_tinh_tien
	vertices[3] += heso_tinh_tien
	vertices[5] += heso_tinh_tien
	vertices[7] += heso_tinh_tien
	draw()
 
#Thay doi ti le:
def scale(heso_ti_le):
	for i in range(8):
	    vertices[i] *= heso_ti_le	

def keyPressed(key,x,y):
    #Nhan phim T hoac t tang kich thuoc
    if key == b't': 
        scale(1.2)
    #Nhan phim N hoac n giam kich thuoc
    if key == b'n': 
        scale(0.8)
    #Nhan phim L hoac l xoay trái
    if key == b'l': 
        rotate(-5)
    #Nhan phim R hoac r xoay phai
    if key == b'r': 
        rotate(5)

def keypressSpecial(key,x,y):
    if key == GLUT_KEY_UP :
        changeX(0.1)    #Phim mui ten di len
    if key == GLUT_KEY_DOWN :
        changeX(-0.1) #Phim mui ten di xuong
    if key == GLUT_KEY_RIGHT :
        changeY(0.1) #Phim mui ten sang phai
    if key == GLUT_KEY_LEFT :
        changeY(-0.1) #Phim mui ten sang trai

if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(640, 640)    
    glutInitWindowPosition(100, 50) 
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
    glutCreateWindow("Transform 2D") 
    initGL()
    glutDisplayFunc(Display)
    glutIdleFunc(Display)
    glutSpecialFunc(keypressSpecial)
    glutKeyboardFunc(keyPressed)  
    glutMainLoop() 
