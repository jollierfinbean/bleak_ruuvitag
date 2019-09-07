# Taken from
# https://github.com/ttu/ruuvitag-sensor/blob/master/ruuvitag_sensor/decoder.py
def twos_complement(value, bits):
    if (value & (1 << (bits - 1))) != 0:
        value = value - (1 << bits)
    return value