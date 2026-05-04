import os
import time
from ai.dalleGenerator import DalleGenerator
from args.defaultArgs import DefaultArgs
from downloader.downloader import Downloader
from env.defaultEnvManager import DefaultEnvManager
from prompt.userPrompt import UserPrompt

def main():    
    argsClass = DefaultArgs()
    args = argsClass.get_args()

    os.makedirs(args["out"], exist_ok=True)

    print(f"Generating {args['count']} thumbnails in {args['out']}...")
    if args["prompt"]:
        print(f"Prompt: {args['prompt']}")

    prompt = UserPrompt(args["prompt"])

    downloader = Downloader()
    dalleGenerator = DalleGenerator(DefaultEnvManager())

    for i in range(1, args["count"] + 1):
        try:
            print(f"[{i}/{args['count']}] Generating: {thumbnailResult['file_tag']}")

            thumbnailResult = dalleGenerator.generate(prompt)

            filename = f"thumb_{i:03d}_{thumbnailResult['file_tag']}.png"
            filepath = os.path.join(args["out"], filename)

            downloader.download_image(thumbnailResult["url"], filepath)

            print(f"[{i}/{args['count']}] Saved: {filename}")

            time.sleep(12)
        except Exception as e:
            print(f"[{i}/{args['count']}] Error: {e}")
            print("Waiting 20 seconds and trying again...")

            time.sleep(20)
    

if __name__ == "__main__":
    main()