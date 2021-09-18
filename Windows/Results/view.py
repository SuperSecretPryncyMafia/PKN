from __init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, round: int, results: list):
        super(View, self).__init__(parent_window)
        self.round = round
        self.results = results

        self.widgets = {
            "results_title": TitleLabel("Results", self),
            "return_button": PushButton("Return to title", self)
        }

        self.players = []

        self.layout_v = QVBoxLayout()
        self.layout_h = QHBoxLayout()

        self.__init_ui()

    def __init_ui(self):
        self.layout_v.addWidget(self.widgets["results_title"], 1, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.layout_v.addSpacing(100)
        self.layout_v.addWidget(self.widgets["return_button"], 1)
        self.setLayout(self.layout_v)
        
 