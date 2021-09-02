from __init__ import *


class DarkTheme:
    @staticmethod
    def button(obj: QPushButton):
        obj.setStyleSheet("""
        QPushButton{
            color: #E0E0E0;
            border: none;
            outline: none;
            background-color: #424242;
            selection-background-color: #424242;
        }
        """)

    @staticmethod
    def widget(obj):
        obj.setStyleSheet("""
        QWidget{
            background-color: #616161;
        }
        """)

    @staticmethod
    def group_box(obj):
        obj.setStyleSheet("""
        QGroupBox{
            color: #606060;
            border: none;
            outline: none;
            background-color: #A2A2A2;
            selection-background-color: #A2A2A2;
        }
        """)

    @staticmethod
    def title_label(obj):
        obj.setStyleSheet("""
        QLabel{
            color: #212121;
            font: medium Ubuntu;
            font-size: 30px;
        
        }
        """)

    @staticmethod
    def tile_style(obj):
        obj.setStyleSheet("""
        QLabel{
            color: #E0E0E0;
            border: none;
            outline: none;
            background-color: #424242;
            selection-background-color: #424242;
        }
        """)


class LightTheme:
    @staticmethod
    def button(obj: QPushButton):
        obj.setStyleSheet("""
        QPushButton{
            color: #202020;
            border: none;
            outline: none;
            background-color: #C2C2C2;
            selection-background-color: #C2C2C2;
        }
        """)
    
    @staticmethod
    def button_unavaliable(obj: QPushButton):
        obj.setStyleSheet("""
        QPushButton{
            color: #202020;
            border: none;
            outline: none;
            background-color: #A2A2A2;
            selection-background-color: #A2A2A2;
        }
        """)

    @staticmethod
    def group_box(obj):
        obj.setStyleSheet("""
        QGroupBox{
            color: #202020;
            border: none;
            outline: none;
            background-color: #C2C2C2;
            selection-background-color: #C2C2C2;
        }
        """)

    @staticmethod
    def widget(obj):
        obj.setStyleSheet("""
        QWidget{
        }
        """)

    @staticmethod
    def title_label(obj):
        obj.setStyleSheet("""
        QLabel{
            color: #202020;
            font: medium Ubuntu;
            font-size: 30px;
        
        }
        """)

    @staticmethod
    def tile_style(obj):
        obj.setStyleSheet("""
        QLabel{
            color: #202020;
            border: none;
            outline: none;
            background-color: #A2A2A2;
            selection-background-color: #A2A2A2;
        }
        """)


class Theme:
    DarkTheme = DarkTheme()
    LightTheme = LightTheme()



