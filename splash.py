import pyxel
import main_gui
import new_game


class SplashScreen:
    splash_active = True
    arrow_x = 88
    arrow_y = 80

    @classmethod
    def title_screen(cls):
        if SplashScreen.splash_active:
            pyxel.rect(0, 0, 256, 12, 1)
            pyxel.text(98, 4, "THE SIMULATION", 0)
            pyxel.text(98, 80, "START NEW GAME", 1)
            pyxel.text(98, 100, "LOAD GAME", 1)
            pyxel.text(98, 120, "QUIT GAME", 1)
            pyxel.rect(0, 244, 256, 12, 1)
            pyxel.text(83, 248, "(C) Avarga Studios 2020", 0)

            pyxel.text(SplashScreen.arrow_x, SplashScreen.arrow_y, ">", 1)

    @classmethod
    def choose_state(cls):
        if SplashScreen.splash_active:
            if pyxel.btnr(pyxel.KEY_DOWN) and SplashScreen.arrow_y < 120:
                SplashScreen.arrow_y += 20
            elif pyxel.btnr(pyxel.KEY_DOWN) and SplashScreen.arrow_y > 120:
                SplashScreen.arrow_y = 80

            if pyxel.btnr(pyxel.KEY_UP) and SplashScreen.arrow_y > 80:
                SplashScreen.arrow_y -= 20
            elif pyxel.btnr(pyxel.KEY_UP) and SplashScreen.arrow_y < 80:
                SplashScreen.arrow_y = 80

            if SplashScreen.arrow_y == 80 and pyxel.btnr(pyxel.KEY_ENTER) or pyxel.btnr(pyxel.KEY_KP_ENTER):
                SplashScreen.splash_active = False
                new_game.NewGame.new_game_started = True

            elif SplashScreen.arrow_y == 100 and pyxel.btnr(pyxel.KEY_ENTER) or pyxel.btnr(pyxel.KEY_KP_ENTER):
                SplashScreen.splash_active = False
                main_gui.MainUI.main_ui_active = True

            elif SplashScreen.arrow_y == 120 and pyxel.btnr(pyxel.KEY_ENTER) or pyxel.btnr(pyxel.KEY_KP_ENTER):
                pyxel.quit()
