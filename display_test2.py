# display_test2.py
from time import sleep

from Hardware.display import RobotDisplay

def main():
    disp = RobotDisplay()

    print("Clear to red...")
    disp.clear("red")
    sleep(2)

    print("Show test pattern...")
    disp.show_test_pattern()
    sleep(3)

    print("Show centered text...")
    disp.show_text_center("Hello robot!", fg="white", bg="purple")
    sleep(3)

    print("Clear to black...")
    disp.clear("black")
    sleep(1)

    print("Done.")

if __name__ == "__main__":
    main()
