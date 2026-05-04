from abc import ABC, abstractmethod

class AbstractArgs(ABC):
    @abstractmethod
    def get_args(self) -> { "prompt": str, "count": int, "out": str }:
        pass