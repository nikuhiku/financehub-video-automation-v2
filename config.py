import os
from dotenv import load_dotenv
load_dotenv()

CONFIG = {
    "channel_name": "FinanceHub2100",
    "theme": "finance",
    "default_minutes": 5,
    "shorts": False,
    "subtitles": True,
    "music_volume": 0.03,
    "script_provider": "gemini",
    "tts_provider": "google_cloud",
    "image_provider": "pexels",
    "api_keys": {
        "gemini": os.getenv("GOOGLE_API_KEY"),
    },
    "output_dir": "videos",
    "temp_dir": "temp"
}
print("✅ Config loaded")