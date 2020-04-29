import pyxel
from calendar import Calendar as c
from player import Player as p
import resources


class MainUI:
    main_ui_active = False

    @classmethod
    def main_ui(cls):
        resource_text_y = 60
        if MainUI.main_ui_active:

            #   MAIN UI HEADER
            pyxel.rectb(0, 0, 256, 13, 1)
            pyxel.text(4, 4, f"Week {c.week}, Year {c.year}", 1)
            pyxel.text(113, 4, f"{c.curr_season}", 1)
            pyxel.rect(214, 2, 40, 9, 1)
            pyxel.text(217, 4, "NEXT TURN", 0)

            # MAIN UI FOOTER
            pyxel.rectb(0, 219, 256, 37, 1)
            pyxel.rectb(64, 219, 64, 37, 1)
            pyxel.rectb(127, 219, 64, 437, 1)
            pyxel.text(22, 237, "BUILD", 1)
            pyxel.text(83, 237, "TASKS", 1)
            pyxel.text(151, 237, "TECH", 1)
            pyxel.text(208, 237, "WORSHIP", 1)

            # MAIN UI LEFT
            pyxel.rectb(0, 16, 79, 200, 1)
            pyxel.rect(1, 17, 77, 9, 7)
            pyxel.text(4, 19, p.name, 1)
            pyxel.text(4, 30, f"Population: {p.population}", 1)
            pyxel.text(4, 39, f"Prestige: {p.prestige}", 1)
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "RESOURCES", 1)
            for resource in resources.res_list:
                if resource.stored > 0:
                    pyxel.text(4, resource_text_y, f"{resource.name}: {resource.stored}", 1)
                    resource_text_y += 8

            # MAIN UI MAP
            pyxel.rectb(82, 16, 174, 134, 1)

            # MAIN UI DIALOGUE BOX
            pyxel.rectb(82, 152, 174, 64, 1)
            pyxel.text(84, 154, f"{c.week}.{c.year} - Scrollable textbox goes here.", 1)

