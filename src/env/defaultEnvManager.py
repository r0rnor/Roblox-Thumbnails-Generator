

import os
from dotenv import load_dotenv

from env.envManager import EnvManager

class DefaultEnvManager(EnvManager):
    def __init__(self):
        load_dotenv()

    def get_dalle_api_key(self) -> str:
        return os.getenv("DALLE_API_KEY")