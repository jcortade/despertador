from machine import ADC
import time
from basicas import *

# Set up ADC on GPIO4
EA4 = ADC(4)



# Test: TMP36
while True:
    EA4_uv = EA4.read_uv() #microvoltios

    
    print("microvoltios:", EA4_uv)
    
    temperatura = scale_ai(EA4_uv, -50, 280)
    
    print("Temperatura:", temperatura)
    
    time.sleep(0.5)