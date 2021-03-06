from __init__ import QMainWindow
from .view import View
from .model import Model


class Controller:
    def __init__(self, parent_window: QMainWindow, round: int):
        super().__init__()
        self.parent_window = parent_window
        self.round = round
        self.view = View(self.parent_window, self.round)
        self.module = Model()