

from ai.thumbnailGenerator import ThumbnailGenerator, ThumbnailResult
from prompt.prompt import Prompt
from env.envManager import EnvManager

class DalleGenerator(ThumbnailGenerator):
    def __init__(self, envManager: EnvManager):
        self.envManager = envManager

    def generate(self, prompt: Prompt) -> ThumbnailResult:
        apiKey = self.envManager.get_dalle_api_key()

        promptText = prompt.generate_prompt()

        return {
            "url": apiKey,
            "file_tag": "thumbnail.png"
        }