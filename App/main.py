import time
from Hardware.audio import AudioManager
from Hardware.display import DisplayManager
from Hardware.ears import EarsManager
from Emotions.behaviours import EmotionController
from Config.settings import EMOTIONS


def main():
    print("[App] Starting robot app")

    audio = AudioManager()
    display = DisplayManager()
    ears = EarsManager()  # not used yet, but initialized
    controller = EmotionController(audio=audio, display=display)

    try:
        while True:
            for emotion in EMOTIONS:
                print(f"\n[App] Setting emotion: {emotion}")
                controller.set_emotion(emotion)
                time.sleep(4)  # show each emotion for 4 seconds

    except KeyboardInterrupt:
        print("\n[App] Shutting down...")
    finally:
        audio.stop()
        display.clear()


if __name__ == "__main__":
    main()
