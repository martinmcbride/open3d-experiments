from dataclasses import dataclass

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def _draw_arrow(x,y,z,color):
    glPushMatrix()
    glColor3f(*color)
    glTranslatef(x,y,z)

    if x != 0:
        glRotatef(90,0,1,0)
    elif y != 0:
        glRotatef(-90,1,0,0)

    glutSolidCone(0.08,0.2,30,30)
    glPopMatrix()

@dataclass
class Axes:
    start: tuple = (0, 0, 0) # (x, y, z) origin
    extent: tuple = (1, 1, 1) # (x, y, z) extent of axes
    size: tuple = (1, 1, 1) # (x, y, z) size of axes in 3D coordinates
    colors: tuple = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    line_width: float = 4

    def of_size(self, size):
        self.size = size
        return self

    def draw(self):
        glLineWidth(self.line_width)

        glBegin(GL_LINES)

        # X axis
        glColor3f(*self.colors[0])
        glVertex3f(0, 0, 0)
        glVertex3f(self.size[0], 0, 0)
        glVertex3f(0, self.size[1], 0)
        glVertex3f(self.size[0], self.size[1], 0)
        glVertex3f(0, 0, self.size[2])
        glVertex3f(self.size[0], 0, self.size[2])

        # Y axis
        glColor3f(*self.colors[1])
        glVertex3f(0, 0, 0)
        glVertex3f(0, self.size[1], 0)
        glVertex3f(self.size[0], 0, 0)
        glVertex3f(self.size[0], self.size[1], 0)
        glVertex3f(0, 0, self.size[2])
        glVertex3f(0, self.size[1], self.size[2])

        # Z axis
        glColor3f(*self.colors[2])
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, self.size[2])
        glVertex3f(self.size[0], 0, 0)
        glVertex3f(self.size[0], 0, self.size[2])
        glVertex3f(0, self.size[1], 0)
        glVertex3f(0, self.size[1], self.size[2])

        glEnd()

        # _draw_arrow(self.size[0],0,0,self.colors[0])
        # _draw_arrow(0,self.size[1],0,self.colors[1])
        # _draw_arrow(0,0,self.size[2],self.colors[2])

        return self
