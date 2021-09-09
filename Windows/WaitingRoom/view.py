from .__init__ import *
from custom_widgets import *
from timer import Timer
from threading import Thread


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, waiting_time: int, controller):
        super(View, self).__init__(parent_window)
        self.controller = controller
        self.timer = Timer.only_seconds(waiting_time)
        self.time = self.timer.return_time()
        self.timer_process = Thread(target=self.start_time)
        self.flag = 0
        self.signal = pyqtSignal()

        self.widgets = {
            "waiting_label": TitleLabel("Waiting...", self),
            "down_counter": QLabel("{}".format(self.time), self),
            "information_label": PushButton("-- some information --", self),
            "players_table": None,
            "players_counter": QLabel("one :3", self),
            "exit_button": PushButton("exit", self),
        }

        self.__layout_v = QVBoxLayout()

        self.__init_ui()
        
    def __init_ui(self):
        self.__layout_v.addWidget(self.widgets["waiting_label"], 2)
        self.__layout_v.addWidget(self.widgets["down_counter"], 1)
        self.__layout_v.addWidget(self.widgets["information_label"], 1)
        self.__layout_v.addWidget(self.widgets["players_counter"], 2)
        self.__layout_v.addWidget(self.widgets["exit_button"], 2)

        self.setLayout(self.__layout_v)

    def start_time(self):
        while self.timer.mins + self.timer.secs > 0:
            self.timer.decrease_one_second()
            self.timer.timer_update()
            if self.flag == 1:
                break
            self.widget_update()
        self.controller.to_game()

    def widget_update(self):
        self.widgets["down_counter"].setText(self.timer.return_time())

    def showEvent(self, event: QShowEvent):
        print("Waiting room is visible!")
        super(View, self).showEvent(event)
        self.timer_process.start()

    def hideEvent(self, event: QHideEvent):
        print("Waiting room is now invisible!")
        self.flag = 1
        super(View, self).hideEvent(event)
        
        
