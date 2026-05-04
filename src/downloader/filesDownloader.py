
import base64

from downloader.downloader import Downloader
import requests

class FilesDownloader(Downloader):
    def download_image(self, url: str, filepath: str) -> bool:
        if url.startswith("data:"):
            header, encoded = url.split(",", 1)
            if ";base64" not in header:
                raise ValueError("Only base64 data URLs are supported")
            with open(filepath, "wb") as file:
                file.write(base64.b64decode(encoded))
            return True

        response = requests.get(url)

        if response.status_code == 200:
            with open(filepath, 'wb') as file:
                file.write(response.content)
            return True
        
        return False