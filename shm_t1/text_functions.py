from utils import morse_dict, get_morse_key
from morse_functions import morse_to_audio

def text_to_morse(text):
    morse_text = ''
    text = text.upper()
    for char in text:
        
        if morse_dict.get(char) == None and char != ' ' and char != '\n':
            print('Caracter \"' + char + '\" eh invalido. Abortando.\n')
            exit(1)

        if char != ' ' and char != '\n':
            morse_text += morse_dict[char]
            morse_text += '000' 
        else:
            morse_text += '0000'
    morse_text = morse_text[:-3]

    return morse_text

def text_to_audio(text):
    morse_to_audio(text_to_morse(text))



