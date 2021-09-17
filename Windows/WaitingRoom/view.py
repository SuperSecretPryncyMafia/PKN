from .__init__ import *
from custom_widgets import *
from timer import Timer
from counter_thread import CounterThread


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, waiting_time: int, controller):
        super(View, self).__init__(parent_window)
        self.parent_window = parent_window
        self.controller = controller
        self.timer = Timer.only_seconds(waiting_time)
        self.time = self.timer.return_time()
        self.flag = [0]
        self.timer_thread = CounterThread(target=self.start_time, flag=self.flag)

        self.widgets = {
            "waiting_label": TitleLabel("Waiting...", self),
            "down_counter": InformationLabel("{}".format(self.time), self),
            "information_label": PushButton("-- some information --", self),
            "players_counter": InformationLabel("one :3", self),
            "exit_button": PushButton("exit", self),
        }

        self.__layout_v = QVBoxLayout()

        self.__init_ui()
        
    def __init_ui(self):
        self.widgets["waiting_label"].setAlignment(Qt.AlignCenter)
        for w in self.widgets.values():
            w.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            w.setMaximumWidth(self.parent_window.screen_size.width())
            self.__layout_v.addWidget(w, 1)

        self.setLayout(self.__layout_v)

    def start_time(self):
        while self.timer.mins + self.timer.secs > 0:
            self.timer.decrease_one_second()
            self.timer.timer_update()
            if self.flag[0] == 1:
                return
            self.widget_update()
        self.controller.to_game()

    def widget_update(self):
        self.widgets["down_counter"].setText(self.timer.return_time())

    def showEvent(self, event: QShowEvent):
        super(View, self).showEvent(event)
        self.timer_thread.start()

    def hideEvent(self, event: QHideEvent):
        self.flag[0] = 1
        super(View, self).hideEvent(event)
        
        
