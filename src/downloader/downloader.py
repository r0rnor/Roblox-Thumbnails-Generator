from abc import ABC, abstractmethod

class Downloader(ABC):
    @abstractmethod
    def download_image(self, url: str, filepath: str) -> None:
        pass
    
