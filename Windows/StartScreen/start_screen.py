from .controller import Controller, View
from abc import ABC


class StartScreen(ABC):
    Controller = Controller
    View = View
