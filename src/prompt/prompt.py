from abc import ABC, abstractmethod

class Prompt(ABC):
    @abstractmethod
    def generate_prompt(self) -> str:
        pass
    
    