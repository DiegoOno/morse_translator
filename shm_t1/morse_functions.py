from utils import *
import wave
import struct
import numpy as np
import math

def morse_to_text(morse_code):
    zero_count = 0
    morse_char = ''
    text = ''

    for i, char in enumerate(morse_code):
        if char == '1':
            if zero_count == 1:
                morse_char += morse_code[i - 1]
            if zero_count == 3:
                text += get_morse_key(morse_char)
                morse_char = ''
            if zero_count == 7:
                text += get_morse_key(morse_char)
                text += ' '
                morse_char = ''
            if i == len(morse_code) - 1:
                morse_char += char    
                text += get_morse_key(morse_char)    
            zero_count = 0
            morse_char += char
        else:
            zero_count += 1
    return text

def morse_to_audio(morse_code):
    n_samples = int((sampling_rate * len(morse_code) / 4))
    morse_numpy_array = np.array(list(morse_code)).astype(np.int64)
    sine_mask = morse_numpy_array.repeat(12000)
    sine_wave = [np.sin(2 * np.pi * frequency * x / sampling_rate) for x in range(n_samples)]
    morse_wave = [sine_wave[i] if sine_mask[i] == 1 else 0 for i in range(len(sine_wave))]

    wave_file = wave.open('out/audio.wav', 'w')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(sampling_rate)

    for i in morse_wave:
        wave_file.writeframes(struct.pack('h', int(i * amplitude)))

    wave_file.close()
