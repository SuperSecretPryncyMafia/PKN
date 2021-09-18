from __init__ import *

import sys
from threading import Thread

from StartScreen.start_screen import StartScreen
from GameScreen.game_screen import GameScreen
from Options.options import Options
from WaitingRoom.waiting_room import WaitingRoom
from Results.results import Results
from style_sheets import Theme


class PKNGame(QMainWindow):
    """
    The main window of the application.
    Inherits from QMainWindow and extends its functionality 
    as an overseer. This object coordinates the views, pop-ups and themes.
    After all preperations and initializations launches two parallel threads
    to simunainously show the main menu (start screen) and, if there is no registered name,
    launch the pop-up to make sure that user has choosen the name.
    """
    def __init__(self):
        super(PKNGame, self).__init__()
        self.screen_size = QDesktopWidget().screenGeometry()
        self.config = Options.Module.get_config()
        self.theme = self.config["theme"]

        if self.theme:
            Theme.LightTheme.widget(self)
        else:
            Theme.DarkTheme.widget(self)

        #  Placeholder for all views
        self.screens = {
            "start": StartScreen.Controller(self),
            "wait": WaitingRoom.Controller(self),
            "results": Results.Controller(self),
            "game": GameScreen.Controller(self),
            "options": Options.Controller(self)
        }

        self.current_screen = None
        
        self.__hide_all()
        self.__start_screen()
        Thread(target = self.show())
        Thread(target = self.login_popup())

    @staticmethod
    def login_popup_static(config: dict, parent_window: QMainWindow):
        """
        Takes care of pop-up in the Option view after reseting the options to default
        which also resets the username.

        parameters:
        config - configuration dictionary objecct taken from the json during initialization of the main window.
        parent_window - The main window of the entire application.

        returns:
        None
        """
        if config["username"] == "":
            while config["username"] == "":
                text = QInputDialog.getText(parent_window, "Login", "Choose your username:")[0]
                config["username"] = text

    def login_popup(self):
        """
        Takes care of pop-up at the start of the application.
        This dialog is not letting unnamed user to play.
        """
        if self.config["username"] == "":
            text = QInputDialog.getText(self, "Login", "Choose your username:")[0]
            self.config["username"] = text
            while self.config["username"] == "":
                text = QInputDialog.getText(self, "Login", "Choose your username:\nYou need to enter something!")[0]
                self.config["username"] = text
            Options.Module.overwrite_config(self.config)

    def __hide_all(self):
        for screen in self.screens.values():
            screen.view.hide()

    def __start_screen(self):
        """
        Launches the first screen
        """
        self.current_screen = self.screens["start"].view
        self.setCentralWidget(self.current_screen)
        self.current_screen.show()
    
    def change_to(self, from_screen: str, to_screen: str) -> None:
        """
        Manages the change of views
        :param from_screen: str
        :param to_screen: str
        :return: None
        """
        self.login_popup_static(self.config, self)
        self.current_screen.hide()
        # Reinitialization of screen to handle the Buffer Stack Overflow qt error ( -1073740791 (0xC0000409) )
        self.screens[from_screen].__init__(self)
        self.current_screen = self.screens[to_screen].view
        self.setCentralWidget(self.current_screen)
        self.current_screen.show()

    def exit(self):
        self.close()


if __name__ == "__main__":
    snake = QApplication(sys.argv)
    PKNGame()
    sys.exit(snake.exec_())

