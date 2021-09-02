from .__init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow):
        super(View, self).__init__(parent_window)

        self.snake = QLabel(self)
        self.__layout_h = QHBoxLayout()
        self.__layout_v = QVBoxLayout()
        self.__layout_grid = QGridLayout()
        self.__layout_grid.setSpacing(0)

        self.textures = {
            0 : QPixmap("App\GameSnake\GameScreen\Assets\grass.png"),
            1 : QPixmap("App\GameSnake\GameScreen\Assets\\no_enter.png")
        }

        self.widgets = {
            "RockButton": PushButton("Rock", self),
            "PapperButton": PushButton("Papper", self),
            "ScissorsButton": PushButton("Scissors", self),
        }

        self.__init__ui()

    def __init__ui(self):
        for widget in self.widgets.items():
            self.__layout_v.addWidget(widget)
