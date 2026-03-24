import math
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

def draw_axis_numbers(length=2.0, step=0.5):

    glColor3f(0.0, 0.0, 0.0)  # black text for white background

    # X axis numbers
    x = step
    while x <= length:
        glRasterPos3f(x, 0, 0)
        label = f"{x:.1f}"
        for c in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))
        x += step

    # Y axis numbers
    y = step
    while y <= length:
        glRasterPos3f(0, y, 0)
        label = f"{y:.1f}"
        for c in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))
        y += step

    # Z axis numbers
    z = step
    while z <= length:
        glRasterPos3f(0, 0, z)
        label = f"{z:.1f}"
        for c in label:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))
        z += step

def draw_axis_ticks(length=2.0, step=0.5, tick=0.05):

    glColor3f(0,0,0)
    glLineWidth(4)

    glBegin(GL_LINES)

    t = step
    while t <= length:

        # X ticks
        glVertex3f(t, -tick, 0)
        glVertex3f(t, tick, 0)

        # Y ticks
        glVertex3f(-tick, t, 0)
        glVertex3f(tick, t, 0)

        # Z ticks
        glVertex3f(0, -tick, t)
        glVertex3f(0, tick, t)

        t += step

    glEnd()


@dataclass
class Axes:
    start: tuple = (0, 0, 0) # (x, y, z) origin in user space
    extent: tuple = (1, 1, 1) # (x, y, z) extent of axes in user space
    size: tuple = (1, 1, 1) # (x, y, z) size of axes in device space
    divs: tuple = (0.2, 0.2, 0.2) # (x, y, z) divisions in use space
    text_offset: tuple = ((0.03, 0.06, 0), (0.12, 0.03, 0), (0, 0, 0))
    colors: tuple = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    div_colors: tuple = ((1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5, 1))
    line_width: float = 4

    def of_start(self, start):
        self.start = start
        return self

    def of_extent(self, extent):
        self.extent = extent
        return self

    def of_divs(self, divs):
        self.divs = divs
        return self

    def of_size(self, size):
        self.size = size
        return self

    def transform_from_graph(self, point):
        return [(point[i] - self.start[i]) * self.size[i] / self.extent[i] for i in range(3)]

    def _get_divs(self, start, extent, div):
        divs = []
        n = math.ceil(start/div)*div
        while n <= start + extent:
            divs.append(n)
            n += div
        return divs

    def _draw_backplanes(self):

        glColor3f(0, 0, 0)
        glLineWidth(4)

        glBegin(GL_LINES)


        glEnd()

    def _draw_axis_ticks(self):

        tick = 0.03
        glColor3f(0, 0, 0)
        glLineWidth(4)

        glBegin(GL_LINES)

        glColor3f(*self.colors[0])
        markers = self._get_divs(self.start[0], self.extent[0], self.divs[0])
        for m in markers:
            pos = self.transform_from_graph((m, self.start[1]+self.extent[1], 0))
            glVertex3f(pos[0], pos[1], 0)
            glVertex3f(pos[0], pos[1]+tick, 0)

        glColor3f(*self.colors[1])
        markers = self._get_divs(self.start[1], self.extent[1], self.divs[1])
        for m in markers:
            pos = self.transform_from_graph((self.extent[0], m, 0))
            glVertex3f(pos[0], pos[1], 0)
            glVertex3f(pos[0]+tick, pos[1], 0)

        glColor3f(*self.colors[2])
        markers = self._get_divs(self.start[2], self.extent[2], self.divs[2])
        for m in markers:
            pos = self.transform_from_graph((0, self.extent[1], m))
            glVertex3f(0, pos[1], pos[2])
            glVertex3f(0, pos[1]+tick, pos[2])

        glEnd()

    def _draw_axis_labels(self):

        glColor3f(*self.colors[0])
        markers = self._get_divs(self.start[0], self.extent[0], self.divs[0])
        for m in markers[1:-1]:
            pos = self.transform_from_graph((m, self.extent[1], 0))
            glRasterPos3f(pos[0] + self.text_offset[0][0], self.start[1]+pos[1] + self.text_offset[1][0], 0)
            label = f"{m:.1f}"
            for c in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))

        glColor3f(*self.colors[1])
        markers = self._get_divs(self.start[1], self.extent[1], self.divs[1])
        for m in markers[1:-1]:
            pos = self.transform_from_graph((self.extent[0], m, 0))
            glRasterPos3f(pos[0] + self.text_offset[1][0], pos[1] + self.text_offset[1][1], 0)
            label = f"{m:.1f}"
            for c in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))

        glColor3f(*self.colors[2])
        markers = self._get_divs(self.start[2], self.extent[2], self.divs[2])
        for m in markers[1:-1]:
            pos = self.transform_from_graph((0, self.extent[1], m))
            print(pos, 0, pos[1] + self.text_offset[1][0],  pos[2] + self.text_offset[1][1])
            glRasterPos3f(0, pos[1] + self.text_offset[1][1],  pos[2] + self.text_offset[1][2])
            label = f"{m:.1f}"
            for c in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(c))


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

        self._draw_axis_ticks()
        self._draw_backplanes()
        self._draw_axis_labels()

        # _draw_arrow(self.size[0],0,0,self.colors[0])
        # _draw_arrow(0,self.size[1],0,self.colors[1])
        # _draw_arrow(0,0,self.size[2],self.colors[2])

        return self
