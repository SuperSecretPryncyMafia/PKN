from .view import View, QMainWindow


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window

        self.view = View(self.parent_window)

        self.event_handler()

    def scissors_choosen(self):
        print("scissors :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["scissors"]
        self.view.widgets["choosen_weapon"].update()

    def event_handler(self):
        # self.view.widgets["Buttons"]["rock_button"].clicked.connect(self.save_and_leave)
        # self.view.widgets["Buttons"]["papper_button"].clicked.connect(self.to_start)
        self.view.widgets["buttons"]["scissors_button"].clicked.connect(self.scissors_choosen)
