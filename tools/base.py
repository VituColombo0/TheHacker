from abc import ABC, abstractmethod

class BaseTool(ABC):
    def __init__(self, target: str):
        self.target = target

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def run(self):
        pass
