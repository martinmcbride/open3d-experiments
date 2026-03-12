from drawing_opengl import make_opengl_3dimage
from plot_opengl import Axes


def draw(width, height):
    Axes().of_size((1, 1.1, 0.8)).draw()

make_opengl_3dimage("cube.png", draw, 600, 500)
