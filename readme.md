# Alarm clock based on ESP32

This is an alarm clock based on ESP32. Its main features are:

- Four digits seven segments display
- Three push buttons for alarm time selection
- LM386 audio power amplifier with a 1W speaker
- LDR used to power off the display in the dark
- PIR detector to see time in the dark and turn off the alarm 
- "Dimmable" LED using PWM ouput


ESP32 is programmed using micropython.It connects via wifi to an NTP server and synchronize automatically. It also calculates summer/winter time. 

PCB was designed with kiCAD. 

3D printed alarm clock body was designed with FreeCAD. 

Inspired by this project: https://github.com/thedalles77/Raspberry-Pi-Pico-LED-Alarm-Clock

Audio player idea from here: https://circuitdigest.com/microcontroller-projects/esp32-based-audio-player

Tetris tune acknowledgements: https://assets.codeclubau.org/assets/tetris-theme.pdf

