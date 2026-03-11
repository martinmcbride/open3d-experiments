from drawing_opengl import make_opengl_3dimage
from plot_opengl import Axes


def draw(width, height):
    Axes().draw()

make_opengl_3dimage("cube.png", draw, 600, 500)
