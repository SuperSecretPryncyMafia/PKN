from __init__ import *
from custom_widgets import *


class View(BaseView):
    def __init__(self, parent_window: QMainWindow, config: dict):
        super(View, self).__init__(parent_window)
        self.config = config

        self.widgets = {
            "options_title": TitleLabel("Options", self),
            "option_labels": {
                "label1" : QLabel(self, text="label1"),
                "option1": QSpinBox(parent=self),
                "label2" : QLabel(self, text="label2"),
                "option2": QLabel(self, text=str(self.config["options"]["option2"])),
                "label3" : QLabel(self, text="label3"),
                "option3": QComboBox(parent=self),
                "label4" : QLabel(self, text="label4"),
                "option4": QLineEdit(self.config["options"]["option4"][0], self)
            },
            
            "exit_buttons": {
                "save_button": PushButton(" Save and leave ", self),
                "return_button": PushButton("Leave without saving", self),
                "default_button": PushButton(" Reset Nickname ", self),
            },
        }

        self.layout_v = QVBoxLayout()
        self.layout_h = QHBoxLayout()

        self.__init_ui()

    def __init_ui(self):
        self.layout_v.addSpacing(30)

        self.layout_h.addWidget(self.widgets["options_title"], alignment=Qt.AlignCenter | Qt.AlignTop)

        self.layout_v.addLayout(self.layout_h, 2)
        self.layout_v.addSpacing(20)

        for w in self.widgets["option_labels"].values():
            w.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
            w.adjustSize()
            self.layout_v.addWidget(w, 1)
        
        self.layout_v.addSpacing(30)
        
        self.layout_h = QHBoxLayout()
        for w in self.widgets["exit_buttons"].values():
            w.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            w.setMinimumHeight(50)
            self.layout_h.addWidget(w)

        self.layout_v.addLayout(self.layout_h, 2)
        self.setLayout(self.layout_v)
