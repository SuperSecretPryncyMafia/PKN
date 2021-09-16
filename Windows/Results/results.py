from .controller import Controller
from .view import View
from .model import Model
from abc import ABC


class Results(ABC):
    Controller = Controller
    View = View
    Model = Model
    