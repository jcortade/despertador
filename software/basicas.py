# FUNCIONES BÁSICAS

# Escalado analógicas. Entrada en uV
# -------------------
def scale_ai(ai_uv, min_eng_units, max_eng_units):
    ea_eng_units= ai_uv * (max_eng_units - min_eng_units) / 3300000 + min_eng_units
    return ea_eng_units
    

    
# Hysteresis comparison
def compare_hyst(analog_in, threshold, hyst, high):
    
    if analog_in >= threshold:
        high = 1
    if analog_in< threshold-hyst:
        high = 0    
    
    return high
    
