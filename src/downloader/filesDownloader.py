

from downloader.downloader import Downloader
import requests

class FilesDownloader(Downloader):
    def download_image(self, url: str, filepath: str) -> bool:
        response = requests.get(url)

        if response.status_code == 200:
            with open(filepath, 'wb') as file:
                file.write(response.content)
            return True
        
        return False