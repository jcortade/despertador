from machine import Pin,ADC, Timer, PWM
import time
from basicas import *

DO5 = Pin(5, Pin.OUT)    # create output pin on GPIO16
led = PWM(DO5, freq=1000)

DO16 = Pin(16, Pin.OUT)    # create output pin on GPIO16
DO17 = Pin(17, Pin.OUT)    # create output pin on GPIO17
DO18 = Pin(18, Pin.OUT)    # create output pin on GPIO18
DO19 = Pin(19, Pin.OUT)    # create output pin on GPIO19
DO21 = Pin(21, Pin.OUT)    # create output pin on GPIO21
DO22 = Pin(22, Pin.OUT)    # create output pin on GPIO22
DO23 = Pin(23, Pin.OUT)    # create output pin on GPIO23
DO26 = Pin(26, Pin.OUT)    # create output pin on GPIO26

DI33 = Pin(33, Pin.IN, Pin.PULL_DOWN)     # create input pin on GPIO33

EA32 = ADC(Pin(32)) # LDR input
EA32.atten(ADC.ATTN_11DB)  # Full range of 0 to 3.3V

DI33_old = 0
activa_led = 0
night = 0
movement_detected = 0
volts = 0

# Create a one-shot timer
tim = Timer(-1)  # Use virtual timer (-1)
t_1s = Timer(-2)  # Use virtual timer (-2)


# Timer callback function
def timer_callback(t):
    print("One-shot timer expired!")
    global movement_detected
    movement_detected = 0

def funcion_1s(t):
    global EA32_uv, EA32, volts
    EA32_uv = EA32.read_uv() #microvoltios    
    #print("microvoltios:", EA32_uv)
    volts = scale_ai(EA32_uv, 0, 3.3)
    print("Volts:", volts)

# periodic at 1kHz
t_1s.init(mode=Timer.PERIODIC, freq=1, callback=funcion_1s)

# Test: DI
while True:

    # Detect night (night = LDR voltage is high)
    if movement_detected == 0:		#If movement detected turn on leds anyways
        night = compare_hyst(volts, 1.4, 0.1, night) 

    activa_led = movement_detected or not night
    
    if activa_led:
        if DO26.value():
            DO26.off()
        else:
            DO26.on()
    else:
        DO26.off()
    
    
    if DI33.value() != DI33_old:
        print(DI33.value())       # get value, 0 or 1
        DI33_old = DI33.value()
        if DI33.value():
            #tim.init(mode=Timer.ONE_SHOT, period=10000, callback=timer_callback)  # Re-init to start
            movement_detected = 1
            print("Movement detectected!!")
        else:
            movement_detected = 0
    
#     if DI33.value():
#         movement_detected = 1
#         print("Movement detectected!!")
    
    if DO26.value():
        DO16.on()
        DO17.on()
        DO18.on()
        DO19.on()
        DO21.on()
        DO22.on()
        DO23.on()
    else:
        DO16.off()
        DO17.off()
        DO18.off()
        DO19.off()
        DO21.off()
        DO22.off()
        DO23.off()    


#     EA32_uv = EA32.read_uv() #microvoltios
# 
#     
#     #print("microvoltios:", EA32_uv)
#     volts = scale_ai(EA32_uv, 0, 3.3)
#     print("Volts:", volts)
#     
    time.sleep_ms(10)
    
    