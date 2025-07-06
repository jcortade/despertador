import time
import network

from wifi import *


# Conectar a Wi-Fi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando a Wi-Fi...")
        try:
            sta_if.active(True)
            sta_if.connect(SSID, PASSWORD)
            while not sta_if.isconnected():
                time.sleep(1)
        except OSError as e:
            print(f"Conexión fallida:", e)
    print("Conexión Wi-Fi establecida")
    print("Dirección IP:", sta_if.ifconfig()[0])


# Desconecta el Wi-Fi
def disconnect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        # Desconecta de la red actual
        sta_if.disconnect()
        print("Desconectado el Wi-Fi...")
        sta_if.active(False)
    print("Conexión Wi-Fi apagada")
