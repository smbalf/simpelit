import pyxel
from calendar import Calendar as c
from player import Player as p
import resources
import buildings


class MainUI:
    main_ui_active = False
    default_frame = False
    construction = False
    tasks = False
    tech = False
    worship = False

    @classmethod
    def close_frames(cls):
        MainUI.default_frame = False
        MainUI.construction = False
        MainUI.tasks = False
        MainUI.tech = False
        MainUI.worship = False

    @classmethod
    def open_frames(cls):
        if not MainUI.main_ui_active:
            return

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 9 < pyxel.mouse_x < 55 and pyxel.mouse_y > 216:
            MainUI.return_default()
            pyxel.rect(10, 232, 46, 11, 0)
            pyxel.text(15, 235, "RESOURCES", 1)

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 70 < pyxel.mouse_x < 100 and pyxel.mouse_y > 216:
            MainUI.close_frames()
            pyxel.rect(72, 232, 29, 11, 0)
            pyxel.text(77, 235, "BUILD", 1)
            MainUI.construction = True

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 116 < pyxel.mouse_x < 144 and pyxel.mouse_y > 216:
            MainUI.close_frames()
            pyxel.rect(119, 232, 29, 11, 0)
            pyxel.text(124, 235, "TASKS", 1)
            MainUI.tasks = True

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 164 < pyxel.mouse_x < 188 and pyxel.mouse_y > 216:
            MainUI.close_frames()
            pyxel.rect(167, 232, 26, 11, 0)
            pyxel.text(172, 235, "TECH", 1)
            MainUI.tech = True

        if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 208 < pyxel.mouse_x < 245 and pyxel.mouse_y > 216:
            MainUI.close_frames()
            pyxel.rect(210, 232, 36, 11, 0)
            pyxel.text(215, 235, "WORSHIP", 1)
            MainUI.worship = True

    @classmethod
    def return_default(cls):
        MainUI.close_frames()
        MainUI.default_frame = True

    @classmethod
    def main_ui(cls):
        if not MainUI.main_ui_active:
            return

        #   MAIN UI HEADER
        pyxel.rectb(0, 0, 256, 13, 1)
        pyxel.text(4, 4, f"Week {c.week}, Year {c.year}", 1)
        pyxel.text(113, 4, f"{c.curr_season}", 1)
        pyxel.rect(192, 2, 8, 9, 1)
        pyxel.text(195, 4, "P", 0)
        pyxel.rect(203, 2, 8, 9, 1)
        pyxel.tri(205, 4, 207, 6, 205, 8, 0)
        pyxel.rect(214, 2, 40, 9, 1)
        pyxel.text(217, 4, "NEXT TURN", 0)

        #   MAIN UI LEFT
        pyxel.rectb(0, 16, 79, 200, 1)
        pyxel.rect(1, 17, 77, 9, 7)
        pyxel.text(4, 19, p.name, 1)
        pyxel.text(4, 30, f"Pop: {int(p.population)}({p.employed})/{p.population_max}", 1)
        pyxel.text(4, 39, f"Prestige: {p.prestige}", 1)

        # MAIN UI MAP
        pyxel.rectb(82, 16, 174, 133, 1)

        # MAIN UI DIALOGUE BOX
        pyxel.rectb(82, 152, 174, 64, 1)

        # MAIN UI FOOTER
        pyxel.rect(0, 219, 256, 37, 1)
        pyxel.rectb(1, 220, 254, 35, 0)

        pyxel.rectb(10, 232, 46, 11, 0)
        pyxel.text(15, 235, "RESOURCES", 0)
        pyxel.rectb(72, 232, 29, 11, 0)
        pyxel.text(77, 235, "BUILD", 0)
        pyxel.rectb(119, 232, 29, 11, 0)
        pyxel.text(124, 235, "TASKS", 0)
        pyxel.rectb(167, 232, 26, 11, 0)
        pyxel.text(172, 235, "TECH", 0)
        pyxel.rectb(210, 232, 36, 11, 0)
        pyxel.text(215, 235, "WORSHIP", 0)

    @classmethod
    def default_gameframe(cls):
        resource_text_y = 60
        if not MainUI.main_ui_active:
            return

        if MainUI.default_frame:
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "RESOURCES", 1)
            for resource in resources.res_list:
                if resource.stored > 0:
                    pyxel.text(4, resource_text_y, f"{resource.name[0:6]}: {int(resource.stored)}", 1)
                    resource_text_y += 8

    @classmethod
    def construction_ui(cls):
        building_text_y = 60
        if not MainUI.main_ui_active:
            return
        if MainUI.construction:
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "BUILDINGS", 1)

            for building in buildings.build_list:
                pyxel.text(4, building_text_y, f"{building.name[0:6]}: {building.built} - [B]", 1)
                building_text_y += 8

            if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 56 < pyxel.mouse_y < 60:
                buildings.construct(buildings.hut)
            elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 64 < pyxel.mouse_y < 68:
                buildings.construct(buildings.clay_house)
            elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and 72 < pyxel.mouse_y < 76:
                buildings.construct(buildings.grain_field)

    @classmethod
    def tasks_ui(cls):
        # tasks_text_y = 60
        if not MainUI.main_ui_active:
            return
        if MainUI.tasks:
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "TASKS", 1)

    @classmethod
    def tech_ui(cls):
        # tasks_text_y = 60
        if not MainUI.main_ui_active:
            return
        if MainUI.tech:
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "TECH", 1)

    @classmethod
    def worship_ui(cls):
        # tasks_text_y = 60
        if not MainUI.main_ui_active:
            return
        if MainUI.worship:
            pyxel.rect(1, 48, 77, 9, 7)
            pyxel.text(4, 50, "WORSHIP", 1)
