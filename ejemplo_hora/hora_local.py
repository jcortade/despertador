import ntptime
import time
import network
from machine import RTC

from wifi import *



# Conectar a Wi-Fi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando a Wi-Fi...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print("Conexión Wi-Fi establecida")
    print("Dirección IP:", sta_if.ifconfig()[0])


# Configuración del servidor NTP
NTP_SERVER = "es.pool.ntp.org"

# Zona horaria (en horas)
TIMEZONE_OFFSET = 1  # Para España (CET) es +1


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
    #connect_wifi()
    #ntptime.host = NTP_SERVER
    #ntptime.settime()
    print("Local time after synchronization：%s" %str(time.localtime()))
    rtc = RTC()
    year, month, day, weekday, hour, minute, second, _ = rtc.datetime()
    hour_adjusted = adjust_for_daylight_saving(year, month, day, hour)
    return (year, month, day, hour_adjusted, minute, second)

def set_current_time():
    connect_wifi()

    #ntptime.host = NTP_SERVER
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
            time.sleep(5)  # Espera 5 segundos antes de reintentar
    else:
        print("No se pudo sincronizar la hora después de varios intentos")
