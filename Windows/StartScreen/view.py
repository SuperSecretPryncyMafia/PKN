from .__init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow):
        super(View, self).__init__(parent_window)

        self.widgets = {
            "title_label": TitleLabel("Rock-Paper-Scissors", self),
            "theme_button": PushButton("switch theme", self),

            "play_button": PushButton("play", self),
            "options_button": PushButton("options", self),
            "exit_button": PushButton("exit", self),
        }

        self.__layout_v = QVBoxLayout()
        self.__layout_h = QHBoxLayout()

        self.__init__ui()

    def __init__ui(self):
        self.__layout_h.addLayout(self.__layout_v)

        # Center part of the view
        self.__layout_v = QVBoxLayout()
        self.__layout_v.addWidget(self.widgets["title_label"], 3, alignment=Qt.AlignCenter)
        self.__layout_v.addWidget(self.widgets["play_button"], 1)
        self.__layout_v.addWidget(self.widgets["options_button"], 1)
        self.__layout_v.addWidget(self.widgets["exit_button"], 1)
        self.__layout_h.addLayout(self.__layout_v)

        # Right-hand side of the view
        self.__layout_v = QVBoxLayout()
        self.__layout_h.addLayout(self.__layout_v)

        self.setLayout(self.__layout_h)



