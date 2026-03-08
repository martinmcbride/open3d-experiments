from drawing_opengl import make_opengl_3dimage
from plot_opengl import draw_axes, AxesOpenGL


def draw(width, height):
    axes = AxesOpenGL()
    axes.draw()

make_opengl_3dimage("cube.png", draw, 600, 500)
