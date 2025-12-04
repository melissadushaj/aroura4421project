# Hardware/ears.py
from time import sleep
from gpiozero import AngularServo

LEFT_EAR_PIN = 12
RIGHT_EAR_PIN = 13

class EarsManager:
    def __init__(self, left_pin: int = LEFT_EAR_PIN, right_pin: int = RIGHT_EAR_PIN):
        self.left = AngularServo(
            left_pin,
            min_angle=0,
            max_angle=180,
            min_pulse_width=0.0005,
            max_pulse_width=0.0025,
        )

        self.right = AngularServo(
            right_pin,
            min_angle=0,
            max_angle=180,
            min_pulse_width=0.0005,
            max_pulse_width=0.0025,
        )
        self.neutral()

    def neutral(self):
        self.left.angle = 90
        self.right.angle = 90

    def perk_up(self):
        self.left.angle = 30
        self.right.angle = 30

    def droop(self):
        self.left.angle = 150
        self.right.angle = 150

    def big_wiggle(self, times: int = 3, delay: float = 0.25):

        for _ in range(times):
            self.left.angle = 30
            self.right.angle = 30
            sleep(delay)
            self.left.angle = 150
            self.right.angle = 150
            sleep(delay)
        self.neutral()

    def surprise_pop(self):

        self.perk_up()
        sleep(0.3)

        for _ in range(3):
            self.left.angle = 20
            self.right.angle = 40
            sleep(0.12)
            self.left.angle = 40
            self.right.angle = 20
            sleep(0.12)

        self.perk_up()
        sleep(0.3)
        self.neutral()

    def empathetic_nod(self):

        self.neutral()
        sleep(0.3)

        for angle in range(90, 151, 10):  
            self.left.angle = angle
            self.right.angle = angle
            sleep(0.08)

        sleep(0.4)

        for angle in range(150, 89, -10): 
            self.left.angle = angle
            self.right.angle = angle
            sleep(0.08)

        self.neutral()

    def confused_tilt(self):

        for _ in range(3):
            self.left.angle = 40
            self.right.angle = 140
            sleep(0.25)
            self.left.angle = 140
            self.right.angle = 40
            sleep(0.25)

        self.neutral()

    def sad_droop_shiver(self):

        self.droop()
        sleep(0.5)

        for _ in range(4):
            self.left.angle = 155
            self.right.angle = 145
            sleep(0.15)
            self.left.angle = 145
            self.right.angle = 155
            sleep(0.15)

        self.droop()
        sleep(0.4)
        self.neutral()

    def sleepy_settle(self):
        
        for angle in range(90, 151, 10):
            self.left.angle = angle
            self.right.angle = angle
            sleep(0.1)

        self.left.angle = 150
        self.right.angle = 150

    def do_for_emotion(self, emotion: str):

        print(f"Emotion -> {emotion}")
        if emotion == "happy":
            self.big_wiggle()
        elif emotion == "surprised":
            self.surprise_pop()
        elif emotion == "empathetic":
            self.empathetic_nod()
        elif emotion == "confused":
            self.confused_tilt()
        elif emotion == "sad":
            self.sad_droop_shiver()
        elif emotion == "sleeping":
            self.sleepy_settle()
        else:
            self.neutral()
    
    def shutdown(self):
        
        self.left.angle = None
        self.right.angle = None
