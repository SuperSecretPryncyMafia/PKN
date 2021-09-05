from .view import View, QMainWindow


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        
        self.view = View(self.parent_window)
        self.event_handler()

    def to_play(self):
        self.parent_window.change_to("start", "wait")

    def to_options(self):
        self.parent_window.change_to("start", "options")

    def event_handler(self):
        self.view.widgets["play_button"].clicked.connect(self.to_play)
        self.view.widgets["options_button"].clicked.connect(self.to_options)
        self.view.widgets["exit_button"].clicked.connect(self.parent_window.exit)




