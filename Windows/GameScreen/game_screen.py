from .view import View
from .controller import Controller
from .model import Model
from abc import ABC


class GameScreen(ABC):
    View = View
    Controller = Controller
    Model = Model