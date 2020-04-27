import pyxel


class MainUI:
    main_ui_active = False

    @classmethod
    def main_ui(cls):
        if MainUI.main_ui_active:
            pyxel.text(100, 100, "MAIN ACTIVE", 6)
