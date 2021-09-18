from __init__ import QMainWindow
from .view import View
from .model import Model


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        self.module = Model()
        self.round = 1
        self.results = self.module.players_results()
        self.view = View(self.parent_window, self.round, self.results)
        self.event_handler()

    def next_round(self):
        self.round += 1
        self.view = View(self.parent_window, self.round)

    def to_start(self):
        self.parent_window.change_to("results", "start")

    def event_handler(self):
        self.view.widgets["return_button"].clicked.connect(self.to_start)