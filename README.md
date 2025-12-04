# 4421project

This project is a Raspberry Pi–powered social robot designed for use in hospital environments.
Its goal is to provide comfort, emotional expression, and simple interactions through:

- A pixel-based LCD face display
- Animated robot “emotions”
- Audio feedback and sound effects
- Servo-driven ears 
- A modular, maintainable software architecture

The robot displays different emotional states (e.g., happy, surprised, neutral, empathy) and responds with matching sounds and movements.

# Goals
- Create a friendly robot that can express emotions visually and audibly.
- Build modular hardware control for:
- LCD matrix (pixel faces)
- Speakers (sound effects & music)
- Servo motors (“ears” or gestures)
- Provide a simple interface for running “modes” such as:
  1. Emotion mode
  2. Demo mode
  3. Interaction mode (future)
Allow easy expansion for future improvements or hospital use cases.

# Hardware
1. Raspberry Pi 5
2. MG90S Micro Servo (ears)
3. LED Display Module
- Width: 32 pixels (adjust in display.py)
- Height: 16 pixels
- RGB matrix or LCD depending on model
- Brightness configurable
4. USB-powered speakers
4. 5V external power for servo (old iPhone charger)

# Setup Instructions
1. Install python packages
  sudo apt update
  sudo apt install python3-pip
  pip3 install pygame gpiozero pillow numpy
  pip3 install spidev

2. Enable Interfaces
   Use raspi-config:
    - Enable SPI for LED matrix
    - Enable I2C if needed
    - Enable audio
