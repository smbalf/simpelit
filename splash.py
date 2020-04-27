import pyxel
import main_gui

class SplashScreen:
    splash_active = True
    arrow_x = 88
    arrow_y = 80

    @classmethod
    def title_screen(cls):
        if SplashScreen.splash_active:
            pyxel.rect(0, 0, 256, 12, 6)
            pyxel.text(98, 4, "THE SIMULATION", 0)
            pyxel.text(98, 80, "START NEW GAME", 6)
            pyxel.text(98, 100, "QUIT GAME", 6)
            pyxel.rect(0, 244, 256, 12, 6)
            pyxel.text(83, 248, "(C) Avarga Studios 2020", 0)

            pyxel.text(SplashScreen.arrow_x, SplashScreen.arrow_y, ">", 6)

    @classmethod
    def choose_state(cls):
        if SplashScreen.splash_active:
            if pyxel.btnr(pyxel.KEY_DOWN) and SplashScreen.arrow_y < 100:
                SplashScreen.arrow_y += 20
            elif pyxel.btnr(pyxel.KEY_DOWN) and SplashScreen.arrow_y > 100:
                SplashScreen.arrow_y = 80

            if pyxel.btnr(pyxel.KEY_UP) and SplashScreen.arrow_y > 80:
                SplashScreen.arrow_y -= 20
            elif pyxel.btnr(pyxel.KEY_UP) and SplashScreen.arrow_y < 80:
                SplashScreen.arrow_y = 80

            if pyxel.btnr(pyxel.KEY_ENTER) or pyxel.btnr(pyxel.KEY_KP_ENTER) and SplashScreen.arrow_x == 80:
                SplashScreen.splash_active = False
                main_gui.MainUI.main_ui_active = True

            elif pyxel.btnr(pyxel.KEY_ENTER) or pyxel.btnr(pyxel.KEY_KP_ENTER) and SplashScreen.arrow_x == 100:
                pyxel.quit()
