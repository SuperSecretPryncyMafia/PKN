from __init__ import *
from style_sheets import Theme


class BaseView(QWidget):
    """
    Holds all common options of all views

    :param: parent_window
    """
    def __init__(self, parent_window: QMainWindow):
        super(BaseView, self).__init__(parent_window, Qt.Widget)
        self.setMinimumSize(640, 400)
        self.parent_window = parent_window
        self.theme = self.parent_window.theme

        if self.theme == 0:
            Theme.DarkTheme.widget(self)
        else:
            Theme.LightTheme.widget(self)

        self.widget = {}


class Tile(QLabel):
    def __init__(self, parent: QWidget, image: QPixmap):
        super(Tile, self).__init__(parent)
        self.parent = parent
        self.image = image
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        if self.parent.theme == 0:
            Theme.DarkTheme.button(self)
        else:
            Theme.LightTheme.button(self)

    def resizeEvent(self, event: QResizeEvent):
        self.setMinimumWidth(self.height())

    @classmethod
    def empty_image(cls, parent_window: QMainWindow):
        return cls(parent_window, None)

    def update(self):
        if self.image:
            self.image.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(self.image)
            self.setScaledContents(True)
        else:
            self.setText('')


class PushButton(QPushButton):
    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.parent = parent
        self.setMaximumWidth(parent.parent_window.screen_size.width() / 3)
        self.setMaximumHeight(parent.parent_window.screen_size.height() / 5)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        if self.parent.theme == 0:
            Theme.DarkTheme.button(self)
        else:
            Theme.LightTheme.button(self)


class TitleLabel(QLabel):
    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.parent = parent
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.font = QFont()
        self.font.setPointSize(20)
        self.setFont(self.font)

        if self.parent.theme == 0:
            Theme.DarkTheme.title_label(self)
        else:
            Theme.LightTheme.title_label(self)

    def resizeEvent(self, eve: QResizeEvent) -> None:
        self.update_size()
        super().resizeEvent(eve)

    def update_size(self):
        self.font = QFont()
        self.font.setPointSize(int(self.height()/5))
        self.setText = self.text
        self.update()
        self.setFont(self.font)
        

class SidePanel(QGroupBox):
    def __init__(self, text: str, parent: QWidget):
        super().__init__(text, parent)
        self.parent = parent
        self.text = text
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        if self.parent.theme == 0:
            Theme.DarkTheme.title_label(self)
        else:
            Theme.LightTheme.title_label(self)
