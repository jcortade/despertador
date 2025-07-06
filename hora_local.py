import ntptime
import time
import network
from machine import RTC
import uasyncio as asyncio

from wifi import *
from wifi_functions import *

# Configuración del servidor NTP
NTP_SERVER = "es.pool.ntp.org"

# Zona horaria (en horas)
TIMEZONE_OFFSET = 1  # Para España (CET) es +1

last_execution_hour = -1
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0


# Función para ajustar la hora según el horario de verano/invierno
def adjust_for_daylight_saving(year, month, day, hour):
    # En España, el horario de verano comienza el último domingo de marzo y termina el último domingo de octubre
    if month > 3 and month < 10:
        return hour + 1 + TIMEZONE_OFFSET# Horario de verano (CEST)
    elif month == 3:
        # Último domingo de marzo
        last_sunday = 31 - (5 * year // 4 + 4) % 7
        if day >= last_sunday and hour >= 2:
            return hour + 1 + TIMEZONE_OFFSET
    elif month == 10:
        # Último domingo de octubre
        last_sunday = 31 - (5 * year // 4 + 1) % 7
        if day < last_sunday or (day == last_sunday and hour < 3):
            return hour + 1 + TIMEZONE_OFFSET
    return hour + TIMEZONE_OFFSET  # Horario de invierno (CET)

# Función para obtener la hora actual
def get_current_time():
    print("Local time after synchronization：%s" %str(time.localtime()))
    rtc = RTC()
    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()
    hour_adjusted = adjust_for_daylight_saving(year, month, day, hour)
    return (year, month, day, hour_adjusted, minute, second)

# Función para poner en hora con sincronización 
def set_current_time():
    connect_wifi()

    ntptime.host = NTP_SERVER
    #ntptime.settime()
    
    # Número máximo de reintentos
    max_retries = 5

    for i in range(max_retries):
        try:
            ntptime.settime()
            print("Hora sincronizada correctamente")
            break  # Sale del bucle si tiene éxito
        except OSError as e:
            print(f"Intento {i + 1} fallido:", e)
            await uasyncio.sleep(5) #time.sleep(5)  # Espera 5 segundos antes de reintentar
    else:
        print("No se pudo sincronizar la hora después de varios intentos")
    
    disconnect_wifi()

async def synchronize():
    
    global last_execution_hour
    global year, month, day, hour, minute, second
    
    ntptime.host = NTP_SERVER
    
    # Número máximo de reintentos sincronización NTP
    max_retries = 5
    
    while True:
        
        # Verifica si son las 12. A las 12 se sincroniza
        if (minute != last_execution_hour): # and (hour==12):
            
            connect_wifi()
            
            await asyncio.sleep(1)

            for i in range(max_retries):
                try:
                    ntptime.settime()
                    print("Hora sincronizada correctamente")
                    break  # Sale del bucle si tiene éxito
                except OSError as e:
                    print(f"Intento {i + 1} fallido:", e)
                    await asyncio.sleep(5)  # Espera 5 segundos antes de reintentar
            else:
                print("No se pudo sincronizar la hora después de varios intentos")
            
            
            disconnect_wifi()
            last_execution_hour = minute # = hour
            
        await asyncio.sleep(1)