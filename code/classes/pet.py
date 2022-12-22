from abc import ABC, abstractmethod
from event_type import eventType
class Pet(ABC):
    def __init__(self, name) -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name

    @abstractmethod
    def eat(self):
        ...

    @abstractmethod
    def play(self):
        ...

    def update(self, EventType):
        if EventType is eventType.FEEDING:
            self.eat()
        if EventType is eventType.PLAYING:
            self.play()

