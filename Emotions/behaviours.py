# Emotions/behaviours.py
from typing import Optional

from Emotions.state import EmotionState
from Emotions.faces import EMOTION_FACES
from Hardware.audio import AudioManager
from Hardware.display import RobotDisplay
from Hardware.ears import EarsManager


class EmotionController:
    def __init__(
        self,
        audio: AudioManager,
        display: RobotDisplay,
        ears: Optional[EarsManager] = None,
    ):
        self.audio = audio
        self.display = display
        self.ears = ears

        self.state = EmotionState(on_change=self._on_emotion_change)

        self._apply_emotion(self.state.current)

    def _on_emotion_change(self, new_emotion: str):
        self._apply_emotion(new_emotion)

    def _apply_emotion(self, emotion: str):
        loop = (emotion == "sleeping")
        self.audio.play_for_emotion(emotion, loop=loop)

        face_fn = EMOTION_FACES.get(emotion)
        if face_fn:
            face_grid = face_fn()
            self.display.show_face(face_grid, emotion=emotion)
        else:
            print(f"No face defined for emotion '{emotion}'")

        if self.ears:
            self.ears.do_for_emotion(emotion)

    def set_emotion(self, emotion: str):
        self.state.set_emotion(emotion)

    def shutdown(self):
        self.audio.stop()
        self.display.clear("black")
        if self.ears:
            self.ears.shutdown()
