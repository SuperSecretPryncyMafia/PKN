from .view import View, QMainWindow
from .model import Model


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        self.waiting_time = Model.get_waiting_time_secs()
        self.view = View(self.parent_window, self.waiting_time, self)

        self.event_handler()

    def to_start(self):
        self.view = View(self.parent_window, self.waiting_time, self)
        self.parent_window.change_to("wait", "start")

    def to_game(self):
        self.parent_window.change_to("wait", "game")

    def event_handler(self):
        self.view.widgets["exit_button"].clicked.connect(self.to_start)
        if self.view.flag == 1:
            self.to_game()
