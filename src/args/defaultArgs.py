

import argparse
from typing import List, Optional, TypedDict
from args.abstractArgs import AbstractArgs

class ArgsDict(TypedDict):
    prompt: str
    count: int
    out: str

class DefaultArgs(AbstractArgs):
    def __init__(self, args_list: Optional[List[str]] = None):
        parser = argparse.ArgumentParser(description="Roblox Thumbnails Generator")

        parser.add_argument("--prompt", type=str, required=False, default="", help="The prompt to generate the thumbnail")
        parser.add_argument("--count", type=int, required=False, default=1, help="The number of thumbnails to generate")
        parser.add_argument("--out", type=str, required=False, default="output", help="The output directory")

        args = parser.parse_args(args_list)

        self.prompt = args.prompt
        self.count = args.count
        self.out = args.out

    def get_args(self) -> ArgsDict:
        return { "prompt": self.prompt, "count": self.count, "out": self.out }