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
            "rock" : QPixmap("Windows\GameScreen\Assets\\rock.png"),
            "paper" : QPixmap("Windows\GameScreen\Assets\paper.png"),
            "scissors": QPixmap("Windows\GameScreen\Assets\scissors.png")
        }

        self.widgets = {
            "choosen_weapon": Tile.empty_image(self),
            
            "buttons":{
                "rock_button": PushButton("Rock", self),
                "paper_button": PushButton("Paper", self),
                "scissors_button": PushButton("Scissors", self),
            }
        }

        self.__init__ui()

    def __init__ui(self):
        self.__layout_h.addWidget(Tile.empty_image(self), 1)

        self.__layout_h.addWidget(Tile.empty_image(self))
        self.__layout_v.addWidget(self.widgets["choosen_weapon"], 2)
        self.__layout_h.addWidget(Tile.empty_image(self))

        self.__layout_h.addLayout(self.__layout_v)
        self.__layout_h.addWidget(Tile.empty_image(self), 1)

        self.__layout_v = QVBoxLayout()
        self.__layout_v.addLayout(self.__layout_h)
        self.__layout_h = QHBoxLayout()

        for widget in self.widgets["buttons"].values():
            widget.setMinimumHeight(100)
            widget.setMaximumHeight(100)
            self.__layout_h.addWidget(widget)

        self.__layout_v.addLayout(self.__layout_h)
        self.setLayout(self.__layout_v)
