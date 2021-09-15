from __init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, round: int):
        super(View, self).__init__(parent_window)
        self.round = round

        self.widgets = {
            "results_title": TitleLabel("Results", self),
        }

        self.players = []

        self.layout_v = QVBoxLayout()
        self.layout_h = QHBoxLayout()

        self.__init_ui()

    def __init_ui(self):
        self.layout_h.addSpacing(20)
        self.layout_h.addWidget(self.widgets["results_title"], alignment=Qt.AlignCenter | Qt.AlignTop)
        self.layout_h.addSpacing(20)
 