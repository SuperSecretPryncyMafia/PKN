from view import View, QMainWindow


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        
        self.view = View(self.parent_window)
        self.event_handler()

    def event_handler(self):
        self.view.widgets["exit_button"].clicked.connect(exit)