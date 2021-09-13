from .controller import Controller
from .view import View
from .module import Module
from abc import ABC


class Options(ABC):
    Controller = Controller
    View = View
    Module = Module
    