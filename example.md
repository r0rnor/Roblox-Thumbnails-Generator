```py
import os
import time
import random
import requests
import argparse

API_KEY = "ТВОЙ_КЛЮЧ_ОТ_OPENAI"
API_URL = "https://api.openai.com/v1/images/generations"

colors = ["neon green", "lava red", "icy blue", "toxic yellow"]
emotions = ["shocked", "angry", "extremely happy", "scared"]
backgrounds = ["obby course", "tycoon base", "simulator spawn area", "lava pit"]

def generate_prompt(custom_prompt):
    color = random.choice(colors)
    emotion = random.choice(emotions)
    background = random.choice(backgrounds)
    
    if custom_prompt:
        prompt = (
            f"{custom_prompt}, {background} background, {emotion} character, "
            f"{color} lighting, 3D low poly game thumbnail, high contrast"
        )
    else:
        prompt = (
            f"3D low poly game thumbnail, {background} background, "
            f"{emotion} character, {color} lighting and atmosphere, "
            f"bright colors, high contrast, trending gaming style"
        )
    
    file_tag = f"{emotion}_{color}".replace(" ", "_")
    return prompt, file_tag

def request_image(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status() 
    return response.json()['data'][0]['url']

def download_image(url, filepath):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Генератор обложек для A/B тестов")
    
    parser.add_argument("--prompt", type=str, default="", 
                        help="Свой базовый промпт (например: 'zombie survival')")
    parser.add_argument("--count", type=int, default=100, 
                        help="Количество картинок для генерации (по умолчанию: 100)")
    parser.add_argument("--out", type=str, default="roblox_thumbnails", 
                        help="Название папки для сохранения (по умолчанию: roblox_thumbnails)")
    
    args = parser.parse_args()
    
    os.makedirs(args.out, exist_ok=True)
    
    print(f"Начинаем генерацию {args.count} картинок в папку '{args.out}'...")
    if args.prompt:
        print(f"Базовая тема: {args.prompt}")
    
    for i in range(1, args.count + 1):
        try:
            prompt, file_tag = generate_prompt(args.prompt)
            print(f"[{i}/{args.count}] Генерируем: {file_tag}...")
            
            image_url = request_image(prompt)
            
            filename = f"thumb_{i:03d}_{file_tag}.png"
            filepath = os.path.join(args.out, filename)
            
            download_image(image_url, filepath)
            print(f"[{i}/{args.count}] Сохранено: {filename}")
            
            time.sleep(12) 
            
        except Exception as e:
            print(f"[{i}/{args.count}] Ошибка: {e}")
            print("Ждем 20 секунд и пробуем следующую...")
            time.sleep(20)

if __name__ == "__main__":
    main()

```