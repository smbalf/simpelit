import splash
import main_gui
import new_game


def call_gameframes():
    splash.SplashScreen.title_screen()
    splash.SplashScreen.choose_state()
    new_game.NewGame.new_game_info()
    main_gui.MainUI.main_ui()
    main_gui.MainUI.default_gameframe()
    main_gui.MainUI.open_frames()
    main_gui.MainUI.construction_ui()
    main_gui.MainUI.tasks_ui()
    main_gui.MainUI.tech_ui()
    main_gui.MainUI.worship_ui()
