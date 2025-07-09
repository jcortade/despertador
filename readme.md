# Alarm clock based on ESP32

This is an alarm clock based on ESP32 programmed in micropython. Its main features are:

- Four digits seven segments display. Oldie but goldie.
- Three push buttons for alarm time selection.
- LM386 audio power amplifier with a 1W speaker.
- LDR used to power off the display in the dark.
- PIR detector to see time in the dark and turn off the alarm.
- "Dimmable" LED using PWM ouput.
- It connects via wifi to an NTP server and synchronize automatically. It also even calculates summer/winter time!




PCB was designed with kiCAD. 

![PCB editor screenshot](https://github.com/jcortade/despertador/blob/main/images/Screenshot%20from%20pcb%20editor.png)




3D printed alarm clock body was designed with FreeCAD. 

Inspired by this project: https://github.com/thedalles77/Raspberry-Pi-Pico-LED-Alarm-Clock

Audio player idea from here: https://circuitdigest.com/microcontroller-projects/esp32-based-audio-player

Tetris tune acknowledgements: https://assets.codeclubau.org/assets/tetris-theme.pdf

