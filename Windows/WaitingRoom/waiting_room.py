from abc import ABC
from .view import View
from .model import Model
from .controller import Controller


class WaitingRoom(ABC):
    Model = Model
    View = View
    Controller = Controller