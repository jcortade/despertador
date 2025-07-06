from machine import Pin, ADC, Timer, PWM, RTC
import time
import network
from basicas import *
from hora_local import *
from seven_segments import *
import uasyncio as asyncio
from sounds import *

last_execution_hour = -1
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0

alarm_hour = 6
alarm_minute = 0
enable_alarm = 0	# Goes high when user activates alarm
flag_activate_alarm = 0 # Goes high when alarm time is reached
state = "IDLE"

flag_1s = 0
flag_500ms = 0
square_500ms = 0

#PIR - Digital Input (GPIO33) <- MPIR sensor	
PIR = Pin(33, Pin.IN, Pin.PULL_DOWN)     # create input pin on GPIO33


# Analog Input (GPIO32) <- LDR
EA32 = ADC(Pin(32)) # LDR input
EA32.atten(ADC.ATTN_11DB)  # Full range of 0 to 3.3V

# Set up ADC on GPIO4 <- Temperature	
EA4 = ADC(4)



#SW1 - Digital Input (GPIO27) <- Main button
main_button = Pin(27, Pin.IN, Pin.PULL_DOWN)
debounce_time = 250  # ms
last_time = 0
flag_main_button = 0

def main_button_handler(pin):
    global last_time, flag_main_button
    now = time.ticks_ms()

    if abs(now - last_time) > debounce_time:
        #if pin.value() == 1:  # Confirm button is still pressed (optional)
            print("Debounced button press!")
            flag_main_button = 1
    last_time = now

main_button.irq(trigger=Pin.IRQ_RISING, handler=main_button_handler)

#SW2 - Digital Input (GPIO35) <- Minus button
minus_button = Pin(35, Pin.IN)
last_time_minus = 0
flag_minus_button = 0

def minus_button_handler(pin):
    global last_time_minus, flag_minus_button
    now = time.ticks_ms()

    if abs(now - last_time_minus) > debounce_time:
        #if pin.value() == 1:  # Confirm button is still pressed (optional)
            print("Debounced button press!")
            flag_minus_button = 1
    last_time_minus = now

minus_button.irq(trigger=Pin.IRQ_FALLING, handler=minus_button_handler)

#SW3 - Digital Input (GPIO34) <- Plus button
plus_button = Pin(34, Pin.IN)
last_time_plus = 0
flag_plus_button = 0

def plus_button_handler(pin):
    global last_time_plus, flag_plus_button
    now = time.ticks_ms()

    if abs(now - last_time_plus) > debounce_time:
        #if pin.value() == 1:  # Confirm button is still pressed (optional)
            print("Debounced button press!")
            flag_plus_button = 1
    last_time_plus = now

plus_button.irq(trigger=Pin.IRQ_RISING, handler=plus_button_handler)

# Digital Output (GPIO5) -> LED
DO5 = Pin(5, Pin.OUT)    # LED output
led_pwm = PWM(DO5, freq=1000)
led_duty = 0
led_pwm.duty_u16(led_duty)

# Set up PWM on GPIO25 -> SPEAKER
speaker_pin = Pin(25, Pin.OUT)
speaker_pwm = PWM(speaker_pin, freq=1000, duty_u16=0)  # 32768 -> 50% duty (silence initially)
freq = 1000

# TIMERS DEFINITION
t_1s = Timer(-1)  # Use virtual timer (-1)
t_500ms = Timer(-2) # Use virtual timer (-2)

def funcion_1s(t):
    global EA32_uv, EA32, EA4, volts_ldr, flag_1s
    EA32_uv = EA32.read_uv() #microvoltios    

    volts_ldr = scale_ai(EA32_uv, 0, 3.3)
    print("Volts:", volts_ldr)
    
    #EA4_uv = EA4.read_uv() #microvoltios    
    #print("microvoltios:", EA4_uv)
    
    #temperatura = scale_ai(EA4_uv, -50, 280)    
    #print("Temperatura:", temperatura)

    flag_1s = 1

def funcion_500ms(t):
    global flag_500ms, square_500ms
    
    flag_500ms = 1
    
    if square_500ms==0:
        square_500ms=1
    else:
        square_500ms=0
    

# periodic at 1s
t_1s.init(mode=Timer.PERIODIC, freq=1, callback=funcion_1s)
# periodic at 2Hz
t_500ms.init(mode=Timer.PERIODIC, freq=2, callback=funcion_500ms)


    

def idle(hora_display):
    global flag_main_button, flag_plus_button, flag_minus_button, enable_alarm
    
    if volts_ldr>2.5 and not PIR.value():
        display_all((' ',' ',' ',' '), (0,0,0,0))
    else:        
        display_all(hora_display, (0,1,0,enable_alarm))
    
    flag_plus_button=0
    flag_minus_button=0    
    
    if flag_main_button == 1 and flag_activate_alarm==0:
        if enable_alarm==1:
            print("ALARMA DESACTIVADA")
            enable_alarm = 0
            flag_main_button = 0
            return "IDLE"
        else:
            print("CAMBIA A HORAS")
            enable_alarm = 1
            flag_main_button = 0
            return "HOURS"
    return "IDLE"

def hours_selection(hora_display):
    global flag_main_button, flag_plus_button, flag_minus_button, alarm_hour
    
    if square_500ms==1:
        display_all((' ',' ',' ',' '), (0,1,0,0))
    else:        
        display_all((str(alarm_hour//10),str(alarm_hour%10),' ',' '), (0,1,0,0))
    
    if flag_plus_button==1:
        if alarm_hour<23:
            alarm_hour = alarm_hour + 1
        else:
            alarm_hour = 0            
        flag_plus_button = 0
    
    if flag_minus_button==1:
        if alarm_hour>0:
            alarm_hour = alarm_hour - 1
        else:
            alarm_hour = 23            
        flag_minus_button = 0
        
    if flag_main_button == 1:
        print("CAMBIA A MINUTOS")
        flag_main_button = 0        
        return "MINUTES"
    return "HOURS"

def minutes_selection(hora_display):
    global flag_main_button, flag_plus_button, flag_minus_button, alarm_hour,alarm_minute
    
    if square_500ms==1:
        display_all((str(alarm_hour//10),str(alarm_hour%10),' ',' '), (0,1,0,0))
    else:        
        display_all((str(alarm_hour//10),str(alarm_hour%10),str(alarm_minute//10),str(alarm_minute%10)), (0,1,0,0))

    if flag_plus_button==1:
        if alarm_minute<59:
            alarm_minute = alarm_minute + 1
        else:
            alarm_minute = 0    
        flag_plus_button = 0
    
    if flag_minus_button==1:
        if alarm_minute>0:
            alarm_minute = alarm_minute - 1
        else:
            alarm_minute = 59
        flag_minus_button = 0


    if flag_main_button == 1:
        print("CAMBIA A IDLE")
        flag_main_button = 0  
        return "IDLE"
    return "MINUTES"

# Mapeo de estados a funciones
states = {
    "IDLE": idle,
    "HOURS": hours_selection,
    "MINUTES": minutes_selection,
}


#INTRO
for i in range(10):
    display_character(' ', 3, 1)
    display_character(str(9-i), 3, 1)
    led_duty = led_duty + 1000
    led_pwm.duty_u16(led_duty)
    time.sleep(0.2)
   
led_duty = 0
led_pwm.duty_u16(led_duty)
speaker_pwm.duty_u16(32768)
speaker_pwm.freq(440)
time.sleep(0.5)

speaker_pwm.duty_u16(0)



while True:
    
    synchronize()
    
    year, month, day, hour, minute, second = get_current_time()
    
    if (hour//10)>0:
        hora_display = (str(hour//10),str(hour%10),str(minute//10),str(minute%10))
    else:
        hora_display = (' ',str(hour%10),str(minute//10),str(minute%10))
    
    state = states[state](hora_display)  # Ejecuta la función del estado actual y actualiza el estado
    
    if PIR.value():
        print("Movement detectected!!")
            
    if hour==alarm_hour and minute==alarm_minute and second==0 and enable_alarm==1:
        flag_activate_alarm = 1
    
    if main_button.value() == 0 or PIR.value():
        flag_activate_alarm = 0
    
    if flag_activate_alarm == 1:

        for tone, length in zip(melody, rhythm):

            if led_duty>=65535:
                led_duty = 0
            else:
                led_duty = led_duty + 100
            if PIR.value():
                break
            led_pwm.duty_u16(led_duty)
            speaker_pwm.duty_u16(32768)
            speaker_pwm.freq(tones[tone])
            time.sleep(tempo/length)
    else:
        led_duty = 0
        led_pwm.duty_u16(led_duty)
        speaker_pwm.duty_u16(0)  # 0% duty 
        


    
