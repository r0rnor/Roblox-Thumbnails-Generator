

import argparse
from typing import List, Optional, TypedDict
from args.abstractArgs import AbstractArgs

class ArgsDict(TypedDict):
    prompt: str
    count: int
    out: str
    api_key: str | None

class DefaultArgs(AbstractArgs):
    def __init__(self, args_list: Optional[List[str]] = None):
        parser = argparse.ArgumentParser(description="Roblox Thumbnails Generator")

        parser.add_argument("--prompt", type=str, required=False, default="Roblox", help="The prompt to generate the thumbnail")
        parser.add_argument("--count", type=int, required=False, default=1, help="The number of thumbnails to generate")
        parser.add_argument("--out", type=str, required=False, default="output", help="The output directory")
        parser.add_argument("--api-key", type=str, required=False, help="The API key to use")

        args = parser.parse_args(args_list)

        self.prompt = args.prompt
        self.count = args.count
        self.out = args.out
        self.api_key = args.api_key

    def get_args(self) -> ArgsDict:
        return { "prompt": self.prompt, "count": self.count, "out": self.out, "api_key": self.api_key }