
import network
import time
from machine import RTC
from machine import Pin

from hora_local import *



led = Pin(2, Pin.OUT)

cat6 = Pin(4, Pin.OUT)
cat8 = Pin(15, Pin.OUT)
cat9 = Pin(16, Pin.OUT)
cat12 = Pin(17, Pin.OUT)

led1 = Pin(5, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(21, Pin.OUT)

num_led = 1

# Zona horaria (en horas)
TIMEZONE_OFFSET = 1  # Para España (CET) es +1

last_execution_hour = -1    

# Función principal
def main():
    
    global num_led
    
    while True:

        global last_execution_hour
        year, month, day, hour, minute, second = get_current_time()
        print("Fecha: {:04d}-{:02d}-{:02d} Hora: {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second))

        # Verifica si la hora ha cambiado
        if hour != last_execution_hour:
            # Ejecuta la tarea diaria
            set_current_time()
            year, month, day, hour, minute, second = get_current_time()
            # Actualiza la variable con el día actual
            last_execution_hour = hour
        
        
        if led.value():
            led.off()
        else:
            led.on()
        
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        
        cat6.off()
        cat8.off()
        cat9.off()
        cat12.off()
            
        if num_led == 1:
            led1.on()
            cat6.on()
        elif num_led==2:
            led2.on()
            cat6.on()
        elif num_led==3:
            led3.on()
            cat6.on()
        elif num_led==4:
            led4.on()
            cat6.on()
        elif num_led==5:
            led1.on()
            cat8.on()
        elif num_led==6:
            led2.on()
            cat8.on()
        elif num_led==7:
            led3.on()
            cat8.on()
        elif num_led==8:
            led4.on()
            cat8.on()
        elif num_led==9:
            led1.on()
            cat9.on()
        elif num_led==10:
            led2.on()
            cat9.on()
        elif num_led==11:
            led3.on()
            cat9.on()
        elif num_led==12:
            led4.on()
            cat9.on()
        elif num_led==13:
            led1.on()
            cat12.on()
        elif num_led==14:
            led2.on()
            cat12.on()
        elif num_led==15:
            led3.on()
            cat12.on()
        elif num_led==16:
            led4.on()
            cat12.on()                
        
        num_led = num_led + 1
        
        if num_led == 17:
            num_led = 1
            

        # Espera un segundo
        time.sleep(1)
        

# Ejecutar el script
if __name__ == "__main__":
    main()
