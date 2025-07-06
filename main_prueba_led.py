from machine import Pin,ADC, Timer, PWM
import time
from basicas import *

DO5 = Pin(5, Pin.OUT)    # create output pin on GPIO16
led_pwm = PWM(DO5, freq=1000)

led_duty = 0

# Test: led
while True:


    print(led_duty)
    led_pwm.duty_u16(led_duty)

    led_duty = led_duty + 1
    
    if led_duty>=65535:
        led_duty = 0
            
    
    time.sleep_ms(20)
    
    