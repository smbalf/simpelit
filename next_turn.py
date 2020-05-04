import pyxel
from calendar import Calendar as cal
import player
import resources
import main_gui
import buildings


class Turns:
    auto_play = False

    @classmethod
    def auto_status(cls):
        if not main_gui.MainUI.main_ui_active:
            return

        if pyxel.btnr(pyxel.KEY_S):
            Turns.auto_play = True
            Turns.auto_turns()

        if pyxel.btnr(pyxel.KEY_P):
            Turns.auto_play = False

    @classmethod
    def auto_turns(cls):
        if not main_gui.MainUI.main_ui_active:
            return
        if Turns.auto_play:
            Turns.next_turn()
        else:
            return

    @classmethod
    def next_turn(cls):
        if not main_gui.MainUI.main_ui_active:
            return

        if pyxel.btnr(pyxel.KEY_N) or \
                (pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 210 < pyxel.mouse_x < 252 and 0 < pyxel.mouse_y < 8):
            cal.next_week()
            player.Player.growth_factor()
            player.Player.pop_change()
            consumption()
            production()
            construction()

        elif Turns.auto_play:
            if pyxel.frame_count % 45 == 0:
                cal.next_week()
                player.Player.growth_factor()
                player.Player.pop_change()
                consumption()
                production()
                construction()


def consumption():
    if resources.grain.stored > 0:
        resources.grain.stored -= player.Player.population * 0.1
    elif resources.grain.stored == 0:
        player.Player.population -= 1


def production():
    if not cal.spring:
        resources.grain.stored += (buildings.grain_field.built * 0.1)
    else:
        resources.grain.stored += buildings.grain_field.built


def construction():
    for queued_building in buildings.build_queue:
        built = queued_building.queued_num + queued_building.buildtime
        if cal.turn == built:
            queued_building.built += 1
            player.Player.employed += queued_building.workers
            player.Player.experience += queued_building.build_exp

            text_updates.append(f"{cal.week}.{cal.year} - A {queued_building.name} was built.")

            if queued_building.buildtype == "Dwelling":
                if queued_building.name == "Hut":
                    player.Player.population_max += 3
                if queued_building.name == "House":
                    player.Player.population_max += 5


text_updates = []


def textbox():
    text_y = 154
    for text in text_updates:
        pyxel.text(84, text_y, text, 1)
        text_y += 8

        if text_y >= 203:
            text_y = 154
            text_updates.clear()
