from .__init__ import *
from custom_widgets import *
from timer import Timer
from threading import Thread


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, waiting_time: int):
        super(View, self).__init__(parent_window)
        self.timer = Timer.only_seconds(waiting_time)
        self.time = self.timer.return_time()

        self.widgets = {
            "waiting_label": TitleLabel("Waiting...", self),
            "down_counter": QLabel("{}".format(self.time)),
            "information_label": PushButton("-- some information --", self),
            "players_table": None,
            "players_counter": QLabel("one :3", self),
            "exit_button": PushButton("exit", self),
        }

        self.__layout_v = QVBoxLayout()
        self.__layout_h = QHBoxLayout()

        self.__init_ui()
        
    def __init_ui(self):
        if self.isVisible():
            Thread(target=self.start_time).start()
        self.__layout_v.addWidget(self.widgets["waiting_label"], 2, Qt.AlignCenter)
        self.__layout_v.addWidget(self.widgets["down_counter"], 1, Qt.AlignCenter)
        self.__layout_v.addWidget(self.widgets["information_label"], 1, Qt.AlignCenter)
        self.__layout_v.addWidget(self.widgets["players_counter"], 2, Qt.AlignCenter)
        self.__layout_v.addWidget(self.widgets["exit_button"], 2, Qt.AlignCenter)

        self.setLayout(self.__layout_v)

    def start_time(self):
        while self.timer.mins + self.timer.secs > 0:
            self.timer.decrease_one_second()
            self.timer.timer_update()
            self.widget_update()

    def widget_update(self):
        self.widgets["down_counter"].setText(self.timer.return_time())
