

from prompt.prompt import Prompt

class UserPrompt(Prompt):
    def __init__(self, prompt: str):
        self.prompt = prompt

    def generate_prompt(self) -> str:
        return self.prompt