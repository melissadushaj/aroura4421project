from time import sleep
from gpiozero import AngularServo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

SERVO_PIN = 18  

factory = PiGPIOFactory()
Device.pin_factory = factory

servo = AngularServo(
    SERVO_PIN,
    min_angle=0,
    max_angle=180,
    min_pulse_width=0.0005,
    max_pulse_width=0.0025,
)

def main():
    print("Sweeping servo...")
    try:
        for angle in [0, 45, 90, 135, 180, 90]:
            print(f"Moving to {angle}°")
            servo.angle = angle
            sleep(0.7)

        print("Holding at 90°")
        servo.angle = 90
        sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        print("Releasing servo (no signal)")
        servo.angle = None

if __name__ == "__main__":
    main()
