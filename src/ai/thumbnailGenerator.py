from abc import ABC, abstractmethod
from typing import TypedDict
from prompt.prompt import Prompt

class ThumbnailResult(TypedDict):
    url: str
    file_tag: str

class ThumbnailGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: Prompt) -> ThumbnailResult:
        pass

    

