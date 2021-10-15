from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Clears the window and draws the tetrahedron.  The tetrahedron is  easily
# specified with a triangle strip, though the specification really isn't very
# easy to read.
def display() :
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a white grid "floor" for the tetrahedron to sit on.
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    i = -2.5 
    while i<2.5 :
        glVertex3f(i, 0, 2.5) 
        glVertex3f(i, 0, -2.5)
        
        glVertex3f(2.5, 0, i) 
        glVertex3f(-2.5, 0, i)
        i += 0.25
        
    glEnd()
    # Draw the tetrahedron.  It is a four sided figure, so when defining it
    # with a triangle strip we have to repeat the last two vertices.
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1, 1, 1) 
    glVertex3f(0, 2, 0)
    
    glColor3f(1, 0, 0) 
    glVertex3f(-1, 0, 1)
    
    glColor3f(0, 1, 0) 
    glVertex3f(1, 0, 1)
    
    glColor3f(0, 0, 1) 
    glVertex3f(0, 0, -1.4)
    
    glColor3f(1, 1, 1) 
    glVertex3f(0, 2, 0)
    
    glColor3f(1, 0, 0) 
    glVertex3f(-1, 0, 1)
    glEnd()
    glFlush()


def init() :
    # Set the current clear color to sky blue and the current drawing color to
    # white.
    glClearColor(0.1, 0.39, 0.88, 1.0)
    glColor3f(1.0, 1.0, 1.0)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  
    glFrustum(-2, 2, -1.5, 1.5, 1, 40)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  
    glTranslatef(0, 0, -3)
    glRotatef(50, 1, 0, 0)
    glRotatef(70, 0, 1, 0)


# Initializes GLUT, the display mode, and main window registers callbacks
# does application initialization enters the main event loop.
def main() :
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow("A Simple Tetrahedron")
    glutDisplayFunc(display)
    init()
    glutMainLoop()
    
main()