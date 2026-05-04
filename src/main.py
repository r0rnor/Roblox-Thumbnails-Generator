from ai.geminiGenerator import GeminiGenerator
from args.defaultArgs import DefaultArgs
from downloader.filesDownloader import FilesDownloader
from env.defaultEnvManager import DefaultEnvManager
from prompt.userPrompt import UserPrompt

from app.app import App

def main():    
    argsClass = DefaultArgs()
    args = argsClass.get_args()

    customPrompt = args["prompt"]

    envManager = DefaultEnvManager()

    downloader = FilesDownloader()
    generator = GeminiGenerator(envManager)
    promptDecorator = UserPrompt(customPrompt)
    
    app = App({
        "downloader": downloader,
        "generator": generator,
        "startArgs": args,
        "promptDecorator": promptDecorator,
    })

    app.run()

if __name__ == "__main__":
    main()