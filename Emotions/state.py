from dataclasses import dataclass, field
from typing import Callable, Optional
from Config.settings import EMOTIONS

@dataclass
class EmotionState:

    current: str = field(default="happy")  # default emotion

    on_change: Optional[Callable[[str], None]] = None

    def set_emotion(self, new_emotion: str):
        if new_emotion not in EMOTIONS:
            print(f"[EmotionState] Unknown emotion '{new_emotion}'")
            return

        if new_emotion == self.current:
            return

        print(f"[EmotionState] Emotion changed: {self.current} -> {new_emotion}")
        self.current = new_emotion

        if self.on_change:
            self.on_change(new_emotion)
