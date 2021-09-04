from .__init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow):
        super(View, self).__init__(parent_window)

        self.widgets = {
            "waiting_label": TitleLabel("Waiting...", self),
            "down_counter":QLabel("I'm counting, just veeeery slow: 64"),
            "information_label": PushButton("-- some information --", self),
            "players_table": None,
            "players_counter": QLabel("one :3", self),
            "exit_button": PushButton("exit", self),
        }

        self.__layout_v = QVBoxLayout()
        self.__layout_h = QHBoxLayout()

        self.__init__ui()
    
    def __init_ui(self):
        pass