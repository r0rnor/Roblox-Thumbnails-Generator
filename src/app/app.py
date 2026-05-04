import os
import time
from typing import TypedDict

from ai.thumbnailGenerator import ThumbnailGenerator
from args.defaultArgs import ArgsDict
from downloader.downloader import Downloader
from prompt.userPrompt import UserPrompt

class AppArgsDict(TypedDict):
    downloader: Downloader
    generator: ThumbnailGenerator
    promptDecorator: UserPrompt
    startArgs: ArgsDict

class App():
    def __init__(self, args: AppArgsDict):
        self.promptDecorator = args["promptDecorator"]
        self.downloader = args["downloader"]
        self.generator = args["generator"]
        self.startArgs = args["startArgs"]
        
        os.makedirs(self.startArgs["out"], exist_ok=True)

    def run(self):
        count = self.startArgs["count"]
        out = self.startArgs["out"]

        print(f"Generating {count} thumbnails in {out}...")

        for i in range(1, count + 1):
            try:
                thumbnailResult = self.generator.generate(self.promptDecorator)
                print(f"[{i}/{count}] Generating: {thumbnailResult['file_tag']}")

                filename = f"thumb_{i:03d}_{thumbnailResult['file_tag']}.png"
                filepath = os.path.join(out, filename)

                self.downloader.download_image(thumbnailResult["url"], filepath)

                print(f"[{i}/{count}] Saved: {filename}")

                time.sleep(12)
            except Exception as e:
                print(f"[{i}/{count}] Error: {e}")
                print("Waiting 20 seconds and trying again...")

                time.sleep(20)