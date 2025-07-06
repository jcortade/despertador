# Based on example from RasPi.TV
# https://raspi.tv/2015/how-to-drive-a-7-segment-display-directly-on-raspberry-pi-in-python

from machine import Pin
import time


# GPIO ports for the 7seg pins
# 					A, B, C, D, E, F, G, DP
segments_pin_num =  [16,17,18,19,21,22,23,26]
segments_pins = [Pin(pin, Pin.OUT) for pin in segments_pin_num]

for pin in segments_pins:
    pin.off()
    
# GPIO ports for the digit 0-3 pins 
digits_pin_num = (12,13,14,15)
# 7seg_digit_pins (12,9,8,6) digits 1-4 respectively
digits_pins = [Pin(pin, Pin.OUT) for pin in digits_pin_num]

for digit in digits_pins:
    digit.off()



# Segments patterns
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

def display_character(char, digit, dp):

    global segment_pins, digits_pins

    pattern = num[char]
    
    for n in range(4):
        if n==digit:
            digits_pins[n].on()
        else:
            digits_pins[n].off()

    for segment, state in zip(segments_pins, pattern):
        segment.value(state)        

    segments_pins[7].value(dp)
           
        
def display_all(chars, dp_list):

    for pos in range(4):
   
        display_character(chars[pos], pos, dp_list[pos])
        time.sleep_ms(2)
        display_character(' ', pos, 0)
