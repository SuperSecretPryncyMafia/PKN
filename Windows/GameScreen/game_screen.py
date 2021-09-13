from .view import View
from .controller import Controller
from .module import Module
from abc import ABC


class GameScreen(ABC):
    View = View
    Controller = Controller
    Module = Module