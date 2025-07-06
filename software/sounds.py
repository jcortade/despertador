# Based of following wiki page
# https://www.sketching-with-hardware.org/wiki/Piezo_Speaker

#notes and corresponding frequency
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    'B': 247,
    'A': 220,
    ' ': 0,
}

tempo = 2

#melody = 'cdefggaaaagaaaag'
#rhythm = [8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 4, 8, 8, 8, 8, 4, 4, 4]
# TETRIS
# A, B, C, D, C, B, A, C, E, D, C, B, B, C, E, C, A, A
melody = 'eeBcddcBAAAceedcBBBcddeeccAAAAAA' #acedcbbcecaa'
rhythm = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8] # 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

def play_tone(freq, duration_ms):
    pwm.freq(freq)  # Set frequency (Hz)
    pwm.duty_u16(32768)  # 50% duty (square wave)
    time.sleep_ms(duration_ms)
    pwm.duty_u16(0)  # Silence 
        