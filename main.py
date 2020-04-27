import pyxel
import call_frame_methods

WIDTH = 256
HEIGHT = 256
CAPTION = "The Simulation"
BLACK = 0x191919  # 0
WHITE = 0xf9f9f9  # 1
RED = 0xff3232  # 2
BLUE = 0x3232ff  # 3
GREEN = 0x329932  # 4
PURPLE = 0x8c198c  # 5
YELLOW = 0xffff4c  # 6
GREY = 0x666666  # 7
BROWN = 0x73510d  # 8


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption=CAPTION,
                   palette=[BLACK, WHITE, RED, BLUE, GREEN, PURPLE, YELLOW, GREY, BROWN])

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(1, 1, "(" + str(pyxel.mouse_x) + ", " + str(pyxel.mouse_y) + ")", 1)
        pyxel.text(pyxel.mouse_x, pyxel.mouse_y, ".", 1)

        call_frame_methods.call_gameframes()


App()
