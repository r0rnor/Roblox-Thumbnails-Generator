

import os
from dotenv import load_dotenv

from env.envManager import EnvManager
from args.defaultArgs import ArgsDict

class DefaultEnvManager(EnvManager):
    def __init__(self, args: ArgsDict):
        load_dotenv()
        self.args = args

    def get_dalle_api_key(self) -> str:
        result = self.args["api_key"] or os.getenv("DALLE_API_KEY")
        
        if not result:
            raise ValueError("DALLE_API_KEY is not set")

        return result

    def get_fal_flux_api_key(self) -> str:
        result = self.args["api_key"] or os.getenv("FAL_KEY")

        if not result:
            raise ValueError("FAL_KEY is not set")

        return result

    def get_fal_model(self) -> str:
        result = os.getenv("FAL_MODEL")

        if not result:
            raise ValueError("FAL_MODEL is not set")

        return result

    def get_gemini_api_key(self) -> str:
        result = self.args["api_key"] or os.getenv("GEMINI_API_KEY")

        if not result:
            raise ValueError("GEMINI_API_KEY is not set")

        return result