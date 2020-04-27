import splash
import main_gui


def call_gameframes():
    splash.SplashScreen.title_screen()
    splash.SplashScreen.choose_state()
    main_gui.MainUI.main_ui()
