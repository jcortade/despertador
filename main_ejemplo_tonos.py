from machine import Pin, PWM
import time

# Set up PWM on GPIO19
speaker_pin = Pin(19, Pin.OUT)
pwm = PWM(speaker_pin, freq=2000, duty_u16=32768)  # 50% duty (silence initially)

def play_tone(freq, duration_ms):
    pwm.freq(freq)  # Set frequency (Hz)
    pwm.duty_u16(32768)  # 50% duty (square wave)
    time.sleep_ms(duration_ms)
    pwm.duty_u16(0)  # Silence

# Test: Play a sequence of tones
while True:
    for freq in [200, 300, 400, 500, 600, 700, 800]:
        play_tone(freq, 500)
    time.sleep(1)