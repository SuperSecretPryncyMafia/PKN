from .__init__ import *
from custom_widgets import *
from counter_thread import CounterThread
from timer import Timer


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, controller, waiting_time: int):
        super(View, self).__init__(parent_window)
        self.controller = controller
        self.timer = Timer.only_seconds(waiting_time)
        self.time = self.timer.return_time()
        self.timer_thread = CounterThread(target=self.start_time, flag=0)

        self.snake = QLabel(self)
        self.__layout_h = QHBoxLayout()
        self.__layout_v = QVBoxLayout()
        self.__layout_grid = QGridLayout()
        self.__layout_grid.setSpacing(0)

        self.textures = {
            "rock" : QPixmap("Windows\GameScreen\Assets\\rock.png"),
            "paper" : QPixmap("Windows\GameScreen\Assets\paper.png"),
            "scissors": QPixmap("Windows\GameScreen\Assets\scissors.png")
        }

        self.widgets = {
            "time_info" : InformationLabel("Time left:", self),
            "down_counter": InformationLabel("{}".format(self.time), self),
            "choosen_weapon": Tile.empty_image(self),
            
            "buttons":{
                "rock_button": PushButton("Rock", self),
                "paper_button": PushButton("Paper", self),
                "scissors_button": PushButton("Scissors", self),
            }
        }

        self.__init__ui()

    def __init__ui(self):
        self.__layout_h.addWidget(Tile.empty_image(self), 1)

        self.__layout_h.addWidget(Tile.empty_image(self))
        self.__layout_v.addWidget(self.widgets["time_info"], 0, alignment=Qt.AlignTop)
        self.__layout_v.addWidget(self.widgets["down_counter"], 0, alignment=Qt.AlignTop)
        self.__layout_v.addWidget(self.widgets["choosen_weapon"], 2)
        self.__layout_h.addWidget(Tile.empty_image(self))

        self.__layout_h.addLayout(self.__layout_v)
        self.__layout_h.addWidget(Tile.empty_image(self), 1)

        self.__layout_v = QVBoxLayout()
        self.__layout_v.addLayout(self.__layout_h)
        self.__layout_h = QHBoxLayout()

        for widget in self.widgets["buttons"].values():
            widget.setMinimumHeight(100)
            widget.setMaximumHeight(100)
            self.__layout_h.addWidget(widget)

        self.__layout_v.addLayout(self.__layout_h)
        self.setLayout(self.__layout_v)

    def start_time(self):
        while self.timer.mins + self.timer.secs > 0:
            self.timer.decrease_one_second()
            self.timer.timer_update()
            self.widget_update()
        self.controller.to_results()

    def widget_update(self):
        self.widgets["down_counter"].setText(self.timer.return_time())

    def showEvent(self, event: QShowEvent):
        super(View, self).showEvent(event)
        self.timer_thread.start()

    def hideEvent(self, event: QHideEvent):
        super(View, self).hideEvent(event)