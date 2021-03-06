import pyxel
import player
import player_keylogging
import main_gui


class NewGame:

    new_game_started = False

    @classmethod
    def new_game_info(cls):
        if NewGame.new_game_started:
            player_keylogging.PlayerKeys.typing = True
            pyxel.rect(50, 60, 160, 75, 1)
            pyxel.text(60, 65, "WELCOME TO THE SIMULATION", 0)
            pyxel.text(60, 80, "WHAT IS THE NAME OF YOUR PEOPLE?", 0)
            pyxel.text(60, 95, player_keylogging.PlayerKeys.text, 0)
            pyxel.text(60, 125, "CLICK BELOW TO BEGIN YOUR JOURNEY...", 0)
            pyxel.rectb(50, 200, 160, 18, 1)
            pyxel.text(95, 206, "ENTER THE WORLD...", 1)

            if 1 < len(player_keylogging.PlayerKeys.text) <= 17:
                if pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_x > 50 and pyxel.mouse_y > 195:
                    player.Player.name = player_keylogging.PlayerKeys.text.upper()
                    player_keylogging.PlayerKeys.typing = False
                    NewGame.new_game_started = False
                    main_gui.MainUI.main_ui_active = True
                    main_gui.MainUI.default_frame = True
