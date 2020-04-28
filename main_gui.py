import pyxel
from calendar import Calendar as c
from player import Player as p
import resources


class MainUI:
    main_ui_active = False

    @classmethod
    def main_ui(cls):
        res_id = 0
        res_y = 46
        if MainUI.main_ui_active:

            #   MAIN UI HEADER
            pyxel.rectb(0, 0, 256, 13, 1)
            pyxel.text(4, 4, f"Week {c.week}, Year {c.year}", 1)
            pyxel.text(83, 4, f"{c.curr_season}", 1)
            pyxel.rect(214, 2, 40, 9, 1)
            pyxel.text(217, 4, "NEXT TURN", 0)

            # MAIN UI FOOTER
            pyxel.rectb(0, 213, 256, 43, 1)
            pyxel.rectb(64, 213, 64, 43, 1)
            pyxel.rectb(127, 213, 64, 43, 1)
            pyxel.text(22, 231, "BUILD", 1)
            pyxel.text(83, 231, "TASKS", 1)
            pyxel.text(151, 231, "TECH", 1)
            pyxel.text(208, 231, "WORSHIP", 1)

            # MAIN UI LEFT
            pyxel.rectb(0, 16, 79, 194, 1)
            pyxel.text(4, 20, p.name, 1)
            pyxel.text(4, 30, f"Population: {p.population}", 1)
            pyxel.text(4, 38, f"Prestige: {p.prestige}", 1)
            for resource in resources.res_list:
                if res_id <= len(resources.res_list):
                    if resources.res_list[res_id].stored > 0:
                        pyxel.text(4, res_y, f"{resources.res_list[res_id].name}: {resources.res_list[res_id].stored}", 1)
                        res_id += 1
                        res_y += 8

            # MAIN UI MAP
            pyxel.rectb(82, 16, 174, 134, 1)

            # MAIN UI DIALOGUE BOX
            pyxel.rectb(82, 152, 174, 58, 1)
