import base64

from google import genai
from google.genai import types

from ai.thumbnailGenerator import ThumbnailGenerator, ThumbnailResult
from env.envManager import EnvManager
from prompt.prompt import Prompt

_DEFAULT_GEMINI_MODEL = "gemini-2.5-flash-image"

class GeminiGenerator(ThumbnailGenerator):
    def __init__(self, envManager: EnvManager):
        self.api_key = envManager.get_gemini_api_key()
        self.model = _DEFAULT_GEMINI_MODEL

        self.client = genai.Client(api_key=self.api_key)

    def generate(self, prompt: Prompt) -> ThumbnailResult:
        prompt_text = prompt.generate_prompt()
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=[prompt_text],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="16:9",
                ),
            ),
        )

        parts = getattr(response, "parts", None)
        if not parts and getattr(response, "candidates", None):
            parts = response.candidates[0].content.parts

        if not parts:
            raise RuntimeError("Gemini returned no parts in response")

        for part in parts:
            inline_data = getattr(part, "inline_data", None)
            if inline_data and inline_data.data:
                mime_type = inline_data.mime_type or "image/png"
                raw = inline_data.data
                if isinstance(raw, bytes):
                    encoded = base64.b64encode(raw).decode("utf-8")
                else:
                    encoded = str(raw)
                image_url = f"data:{mime_type};base64,{encoded}"
                file_tag = "gemini"
                return {
                    "url": image_url,
                    "file_tag": file_tag,
                }

        raise RuntimeError("Gemini response has no image inline_data")