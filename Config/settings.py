# settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE_DIR / "Sounds"

AUDIO_VOLUME = 0.7  

FACE_COLS = 16   
FACE_ROWS = 16   

BRIGHTNESS = 60 

EMOTIONS = [
    "happy",
    "surprised",
    "empathetic",
    "confused",
    "sad",
    "sleeping",
]

EMOTION_SOUNDS = {
    "happy": "happy_robotic.mp3",
    "surprised": "sparkle_se.mp3",
    "empathetic": "empathetic.mp3",
    "confused": "confused.mp3",
    "sad": "sad_face_squish.mp3",
    "sleeping": "calming_music.mp3",
}

EMOTIONS = list(EMOTION_SOUNDS.keys())
