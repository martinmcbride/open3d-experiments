from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

angle_x = 30
angle_y = -45
last_x = 0
last_y = 0
mouse_down = False
AXIS_LIMIT = 2.0

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
    glLineWidth(1)

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

def draw_paraboloid(size=2.0, step=0.1):

    # -------- surface --------
    glColor3f(0.6, 0.8, 1.0)

    x = -size
    while x < size:

        glBegin(GL_TRIANGLE_STRIP)

        y = -size
        while y <= size:

            z1 = x*x + y*y
            z2 = (x+step)*(x+step) + y*y

            glVertex3f(x, y, z1)
            glVertex3f(x+step, y, z2)

            y += step

        glEnd()
        x += step


    # -------- grid lines --------
    glColor3f(0.2, 0.2, 0.2)
    glLineWidth(1)

    # lines along x direction
    y = -size
    while y <= size:

        glBegin(GL_LINE_STRIP)

        x = -size
        while x <= size:
            z = x*x + y*y
            glVertex3f(x, y, z)
            x += step

        glEnd()
        y += step


    # lines along y direction
    x = -size
    while x <= size:

        glBegin(GL_LINE_STRIP)

        y = -size
        while y <= size:
            z = x*x + y*y
            glVertex3f(x, y, z)
            y += step

        glEnd()
        x += step

def draw_paraboloid_colored(size=2.0, step=0.1):

    x = -size
    while x < size:

        glBegin(GL_TRIANGLE_STRIP)

        y = -size
        while y <= size:

            z1 = x*x + y*y
            z2 = (x+step)*(x+step) + y*y

            # Choose color for vertex 1
            if z1 <= AXIS_LIMIT:
                glColor3f(0.6, 0.8, 1.0)  # inside: light blue
            else:
                glColor3f(1.0, 0.6, 0.6)  # outside: light red

            glVertex3f(x, y, min(z1, AXIS_LIMIT))

            # Choose color for vertex 2
            if z2 <= AXIS_LIMIT:
                glColor3f(0.6, 0.8, 1.0)  # inside
            else:
                glColor3f(1.0, 0.6, 0.6)  # outside

            glVertex3f(x+step, y, min(z2, AXIS_LIMIT))

            y += step

        glEnd()
        x += step

def draw_grid(size=10, step=1):
    glColor3f(0.7, 0.7, 0.7)
    glLineWidth(1)

    glBegin(GL_LINES)
    for i in range(-size, size + 1, step):
        glVertex3f(i, -size, 0)
        glVertex3f(i, size, 0)

        glVertex3f(-size, i, 0)
        glVertex3f(size, i, 0)
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

    draw_arrow(length,0,0,(1,0,0))
    draw_arrow(0,length,0,(0,1,0))
    draw_arrow(0,0,length,(0,0,1))


def draw_arrow(x,y,z,color):
    glPushMatrix()
    glColor3f(*color)
    glTranslatef(x,y,z)

    if x != 0:
        glRotatef(90,0,1,0)
    elif y != 0:
        glRotatef(-90,1,0,0)

    glutSolidCone(0.08,0.2,30,30)
    glPopMatrix()


def draw_labels(length=2.2):

    glColor3f(1,0,0)
    glRasterPos3f(length,0,0)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('X'))

    glColor3f(0,1,0)
    glRasterPos3f(0,length,0)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('Y'))

    glColor3f(0,0,1)
    glRasterPos3f(0,0,length)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('Z'))


def display():
    global angle_x, angle_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(5,5,5, 0,0,0, 0,0,1)

    glRotatef(angle_x,1,0,0)
    glRotatef(angle_y,0,0,1)

    draw_grid()
    draw_axes()
    draw_labels()

    draw_axis_numbers()
    draw_axis_ticks()

    glEnable(GL_CLIP_PLANE0)
    plane = [0.0, 0.0, -1.0, AXIS_LIMIT]
    glClipPlane(GL_CLIP_PLANE0, plane)
    draw_paraboloid_colored()

    glutSwapBuffers()


def mouse(button,state,x,y):
    global mouse_down,last_x,last_y

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            mouse_down=True
            last_x=x
            last_y=y
        else:
            mouse_down=False


def motion(x,y):
    global angle_x,angle_y,last_x,last_y

    if mouse_down:
        angle_x += (y-last_y)*0.5
        angle_y += (x-last_x)*0.5
        last_x=x
        last_y=y
        glutPostRedisplay()


def init():

    # Set background color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glEnable(GL_DEPTH_TEST)

    # Antialiasing
    glEnable(GL_MULTISAMPLE)

    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,1.0,0.1,100)

    glMatrixMode(GL_MODELVIEW)

def main():

    width = 900
    height = 900
    glutInit()

    # request multisampling buffer
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)

    glutInitWindowSize(900,900)
    glutCreateWindow(b"OpenGL 3D Axes Viewer (Antialiased)")

    init()


    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)


    glutMainLoop()


    data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    img = Image.frombytes("RGB", (width, height), data)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save("test.png")


main()