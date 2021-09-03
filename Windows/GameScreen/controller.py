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

    def rock_choosen(self):
        print("rock :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["rock"]
        self.view.widgets["choosen_weapon"].update()

    def paper_choosen(self):
        print("paper :)")
        self.view.widgets["choosen_weapon"].image = self.view.textures["paper"]
        self.view.widgets["choosen_weapon"].update()

    def event_handler(self):
        self.view.widgets["Buttons"]["rock_button"].clicked.connect(self.rock_choosen)
        self.view.widgets["Buttons"]["paper_button"].clicked.connect(self.paper_choosen)
        self.view.widgets["buttons"]["scissors_button"].clicked.connect(self.scissors_choosen)
