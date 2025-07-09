# Alarm clock based on ESP32

This is an alarm clock based on ESP32 programmed in micropython. Its main features are:

- Four digits seven segments display. Oldie but goodie.
- Three push buttons for alarm time selection.
- LM386 audio power amplifier with a 1W speaker. It plays Tetris tune.
- LDR used to power off the display in the dark.
- PIR detector to see time in the dark and turn off the alarm.
- "Dimmable" LED using PWM ouput.
- It connects via wifi to an NTP server and synchronize automatically. It also even calculates summer/winter time!

Prototyping phase:
![Protoboard with a mess of wiring](https://github.com/jcortade/despertador/blob/main/images/IMG_20250525_185729.jpg)

Preparing PCB for solder paste application:
![PCB](https://github.com/jcortade/despertador/blob/main/images/IMG_20250606_174817.jpg)

PCB with components soldered:
![PCB with all components soldered](https://github.com/jcortade/despertador/blob/main/images/IMG_20250621_182720.jpg)

Final result:
![Final result](https://github.com/jcortade/despertador/blob/main/images/IMG_20250628_181656.jpg)

![Final result](https://github.com/jcortade/despertador/blob/main/images/IMG_20250630_230623.jpg)


PCB was designed with kiCAD. 

![PCB editor screenshot](https://github.com/jcortade/despertador/blob/main/images/Screenshot%20from%20pcb%20editor.png)

![3D PCB visualizer screenshot](https://github.com/jcortade/despertador/blob/main/images/despertador_3d_pcb.png)

3D printed alarm clock body was designed with FreeCAD. 

![FreeCAD Screenshot 1](https://github.com/jcortade/despertador/blob/main/images/freecad01.png)

![FreeCAD Screenshot 2](https://github.com/jcortade/despertador/blob/main/images/freecad02.png)

![FreeCAD Screenshot 3](https://github.com/jcortade/despertador/blob/main/images/freecad03.png)


Inspired by this project: https://github.com/thedalles77/Raspberry-Pi-Pico-LED-Alarm-Clock

Audio player idea from here: https://circuitdigest.com/microcontroller-projects/esp32-based-audio-player

Tetris tune acknowledgements: https://assets.codeclubau.org/assets/tetris-theme.pdf

