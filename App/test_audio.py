import time
from Hardware.audio import AudioManager

def main():
    print("Initializing AudioManager")
    audio = AudioManager()

    test_emotion = "happy"

    print(f"Playing emotion sound: {test_emotion}")
    audio.play_for_emotion(test_emotion, loop=False)

    time.sleep(5)

    print("Stopping audio")
    audio.stop()

if __name__ == "__main__":
    main()
