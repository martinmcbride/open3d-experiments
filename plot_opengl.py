from dataclasses import dataclass

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

@dataclass
class AxesOpenGL:
    origin: tuple = (0, 0, 0)
    size: tuple = (1, 1, 1)

    def draw(self):
        glLineWidth(4)

        glBegin(GL_LINES)

        # X axis
        glColor3f(1, 0, 0)
        glVertex3f(*self.origin)
        glVertex3f(self.size[0], 0, 0)

        # Y axis
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, self.size[1], 0)

        # Z axis
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, self.size[2])

        glEnd()


def draw_axes(length=2.0):

    glLineWidth(4)

    glBegin(GL_LINES)

    # X axis
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(length, 0, 0)

    # Y axis
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, length, 0)

    # Z axis
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, length)

    glEnd()

    # draw_arrow(length,0,0,(1,0,0))
    # draw_arrow(0,length,0,(0,1,0))
    # draw_arrow(0,0,length,(0,0,1))
