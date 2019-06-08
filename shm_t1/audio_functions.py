import wave
import struct
import numpy as np
from utils import duration, sampling_rate
from morse_functions import morse_to_text

def load_wave(audio_path):
    
    with wave.open(audio_path) as wave_file:
        num_frames = wave_file.getnframes()
        data = wave_file.readframes(num_frames)
        data = struct.unpack(f'{num_frames}h', data)
        return np.array(data)

def audio_to_morse(audio_path):
    loaded_wave = load_wave(audio_path)
    generated_morse = ''
    frames_per_code = int(sampling_rate * duration)
    for i in range(int(frames_per_code / 2), len(loaded_wave), frames_per_code):
        generated_morse += '1' if max(loaded_wave[range(i - 10, i + 10)], key = abs) != 0 else '0'

    return generated_morse

def audio_to_text(audio_path):

    return morse_to_text(audio_to_morse(audio_path))