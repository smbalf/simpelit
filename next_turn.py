import pyxel
import calendar


def next_turn():
    if pyxel.btnr(pyxel.KEY_N) or \
            (pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 210 < pyxel.mouse_x < 252 and 0 < pyxel.mouse_y < 8):
        calendar.Calendar.next_week()
