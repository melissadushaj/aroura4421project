# Hardware/audio.py
import os
import pygame
from Config.settings import SOUNDS_DIR, AUDIO_VOLUME, EMOTION_SOUNDS

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(AUDIO_VOLUME)

        self.emotion_sounds = {}
        for emotion, filename in EMOTION_SOUNDS.items():
            path = SOUNDS_DIR / filename
            if path.exists():
                self.emotion_sounds[emotion] = str(path)
            else:
                print(f"WARNING: sound file not found for {emotion}: {path}")

    def _play_file(self, filepath: str, loop: bool = False):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return

        pygame.mixer.music.stop()

        try:
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play(-1 if loop else 0)
        except Exception as e:
            print(f"Error playing file {filepath}: {e}")

    def play_for_emotion(self, emotion: str, loop: bool = False):
        filepath = self.emotion_sounds.get(emotion)
        if not filepath:
            print(f"No sound written for this emotion '{emotion}'")
            return

        self._play_file(filepath, loop)
        print(f"Playing emotion sound effect '{emotion}'")

    def play_music_file(self, filepath: str, loop: bool = False):
        self._play_file(filepath, loop)
        print(f"Playing music: {filepath}")

    def is_playing(self) -> bool:
        return pygame.mixer.music.get_busy()

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped all sounds")
