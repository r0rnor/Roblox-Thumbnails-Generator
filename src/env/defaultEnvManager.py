

import os
from dotenv import load_dotenv

from env.envManager import EnvManager

class DefaultEnvManager(EnvManager):
    def __init__(self):
        load_dotenv()

    def get_dalle_api_key(self) -> str:
        result = os.getenv("DALLE_API_KEY")
        
        if not result:
            raise ValueError("DALLE_API_KEY is not set")

        return result

    def get_fal_flux_api_key(self) -> str:
        result = os.getenv("FAL_KEY")

        if not result:
            raise ValueError("FAL_KEY is not set")

        return result

    def get_fal_model(self) -> str:
        result = os.getenv("FAL_MODEL")

        if not result:
            raise ValueError("FAL_MODEL is not set")

        return result