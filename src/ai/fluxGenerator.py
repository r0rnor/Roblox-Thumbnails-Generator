import time
from ai.thumbnailGenerator import ThumbnailGenerator, ThumbnailResult
import fal_client

from env.envManager import EnvManager
from prompt.prompt import Prompt

_DEFAULT_FAL_MODEL = "fal-ai/flux/schnell"

class FalFluxGenerator(ThumbnailGenerator):
    def __init__(self, envManager: EnvManager):
        self.api_key = envManager.get_fal_flux_api_key()
        self.model = envManager.get_fal_model() or _DEFAULT_FAL_MODEL

    def generate(self, prompt: Prompt) -> ThumbnailResult:
        text_prompt = prompt.generate_prompt()
                
        result = fal_client.subscribe(
            self.model,
            arguments={
                "prompt": text_prompt,
                "image_size": "landscape_16_9",
                "num_inference_steps": 4,
            },
        )
        
        image_url = result['images'][0]['url']
        
        words = text_prompt.split()[:3]
        safe_name = "_".join(words).lower()
        safe_name = "".join(c for c in safe_name if c.isalnum() or c == "_")
        
        timestamp = int(time.time())
        file_tag = f"flux_{safe_name}_{timestamp}"
        
        return {
            "url": image_url,
            "file_tag": file_tag
        }