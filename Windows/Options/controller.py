from __init__ import QMainWindow
from .view import View
from .module import Module


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        self.config = Module.get_config()

        self.view = View(self.parent_window, self.config)

        self.event_handler()

    def to_start(self):
        self.parent_window.change_to("options", "start")

    def save_and_leave(self):
        self.save_changes()
        self.to_start()

    def save_changes(self):
        Module.overwrite_config(self.config)

    def set_default(self):
        self.config = Module.get_default()

    def event_handler(self):
        self.view.widgets["exit_buttons"]["save_button"].clicked.connect(self.save_and_leave)
        self.view.widgets["exit_buttons"]["return_button"].clicked.connect(self.to_start)
        self.view.widgets["exit_buttons"]["default_button"].clicked.connect(self.set_default)
