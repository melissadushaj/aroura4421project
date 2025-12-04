# demo.py
import time
from pathlib import Path

from Config.settings import EMOTIONS, SOUNDS_DIR
from Hardware.audio import AudioManager
from Hardware.display import RobotDisplay
from Hardware.ears import EarsManager
from Emotions.behaviours import EmotionController

def run_demo():
    print("Starting demo!")

    audio = AudioManager()
    display = RobotDisplay()
    ears = EarsManager()
    controller = None  

    try:
        display.clear("black")
        display.show_text_center(
            "Hello Prof. Jenkin\n"
            "& EECS 4421!\n"
            "This is Aroura,\n"
            "our final project.\n"
            "Here's our demo!",
            fg="white",
            bg="black",
        )
        time.sleep(4)

        controller = EmotionController(audio=audio, display=display, ears=ears)

        print("Showing emotions...")
        for emotion in EMOTIONS:
            print(f"  -> {emotion}")
            controller.set_emotion(emotion)
            time.sleep(4)

        print("Notidication test...")
        audio.play_for_emotion("surprised", loop=False)
        display.show_notification("New message from your nurse!")
        time.sleep(5)
        audio.stop()

        display.clear("black")
        display.show_text_center(
            "Translating ...",
            fg="white",
            bg="black",
        )
        time.sleep(2)

        print("Translator demo")
        audio.play_for_emotion("empathetic", loop=False)
        display.show_notification("Mesazh i ri nga infermierja juaj!")
        time.sleep(5)
        audio.stop()

        music_path = SOUNDS_DIR / "nokia.mp3"
        total_demo_seconds = 9

        print(f"Playing music files: {music_path.name}")
        audio.play_music_file(str(music_path), loop=False)

        start = time.time()
        while time.time() - start < total_demo_seconds and audio.is_playing():
            elapsed = int(time.time() - start)
            display.show_music_screen(
                title=music_path.stem.replace("_", " "),
                elapsed_s=elapsed,
                total_s=total_demo_seconds,
            )
            time.sleep(0.5)

        audio.stop()

        print("Going to sleep...")
        controller.set_emotion("sleeping")
        time.sleep(2)

    except KeyboardInterrupt:
        print("\nInterrupted by user")

    finally:
        print("Shutting down")
        if controller is not None:
            controller.shutdown()

if __name__ == "__main__":
    run_demo()
