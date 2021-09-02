from __init__ import *
"""
(
    QMainWindow,
    QWidget,
    QApplication,
    QMessageBox,
)
"""

import sys

from StartScreen.start_screen import StartScreen
from GameScreen.game_screen import GameScreen
from Options.options import Options
from style_sheets import Theme


class PKNGame(QMainWindow):
    
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
            "game": GameScreen.Controller(self),
            "options": Options.Controller(self)
        }

        self.current_screen = None

        self.__hide_all()
        self.__start_screen()
        self.show()

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
        self.current_screen.hide()
        # Reinitialization of screen to handle the Buffer Stack Overflow qt error ( -1073740791 (0xC0000409) )
        self.screens[from_screen].__init__(self)
        self.current_screen = self.screens[to_screen].view
        self.setCentralWidget(self.current_screen)
        self.current_screen.show()


if __name__ == "__main__":
    snake = QApplication(sys.argv)
    PKNGame()
    sys.exit(snake.exec_())

