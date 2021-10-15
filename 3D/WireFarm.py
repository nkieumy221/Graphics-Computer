from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Clears the window and draws the torus.
def display() :
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw a white torus of outer radius 3, inner radius 0.5 with 15 stacks
    # and 30 slices.
    glColor3f(1.0, 1.0, 1.0)
    glutWireTorus(0.5, 3, 15, 30)

    # Draw a red x-axis, a green y-axis, and a blue z-axis.  Each of the
    # axes are ten units long.
    glBegin(GL_LINES)
    glColor3f(1, 0, 0) 
    glVertex3f(0, 0, 0) 
    glVertex3f(10, 0, 0)
    
    glColor3f(0, 1, 0) 
    glVertex3f(0, 0, 0) 
    glVertex3f(0, 10, 0)
    
    glColor3f(0, 0, 1) 
    glVertex3f(0, 0, 0) 
    glVertex3f(0, 0, 10)
    
    glEnd()
    glFlush()

# Sets up global attributes like clear color and drawing color, and sets up
# the desired projection and modelview matrices.
def init() :

  # Set the current clear color to black and the current drawing color to
  # white.
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)


    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 4.0/3.0, 1, 40)

    # Position camera at (4, 6, 5) looking at (0, 0, 0) with the vector
    # <0, 1, 0> pointing upward.
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(4, 6, 5, 0, 0, 0, 0, 1, 0)


def main() :
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow("A Simple Torus")
    glutDisplayFunc(display)
    init()
    glutMainLoop()
    
main()