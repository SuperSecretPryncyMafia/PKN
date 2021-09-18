from .view import View, QMainWindow
from .model import Model


class Controller:
    def __init__(self, parent_window: QMainWindow):
        super().__init__()
        self.parent_window = parent_window
        self.model = Model()
        self.view = View(self.parent_window, self, self.model.get_waiting_time_secs())

        self.event_handler()

    def scissors_choosen(self):
        print("scissors :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["scissors"]
        self.view.widgets["choosen_weapon"].update()

    def rock_choosen(self):
        print("rock :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["rock"]
        self.view.widgets["choosen_weapon"].update()

    def paper_choosen(self):
        print("paper :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["paper"]
        self.view.widgets["choosen_weapon"].update()

    def to_results(self):
        self.parent_window.change_to("game", "results")

    def event_handler(self):
        self.view.widgets["buttons"]["rock_button"].clicked.connect(self.rock_choosen)
        self.view.widgets["buttons"]["paper_button"].clicked.connect(self.paper_choosen)
        self.view.widgets["buttons"]["scissors_button"].clicked.connect(self.scissors_choosen)
