from abc import ABC, abstractmethod

class EnvManager(ABC):
    @abstractmethod
    def get_dalle_api_key(self) -> str:
        pass

