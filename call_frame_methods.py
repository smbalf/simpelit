import splash
import main_gui
import new_game


def call_gameframes():
    splash.SplashScreen.title_screen()
    splash.SplashScreen.choose_state()
    main_gui.MainUI.main_ui()
    new_game.NewGame.new_game_info()

