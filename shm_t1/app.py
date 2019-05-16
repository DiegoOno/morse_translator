import sys

morse_dict = {
    # Letters
    'A': '10111', 'B': '111010101', 'C': '11101011101',
    'D': '1110101', 'E': '1', 'F': '101011101',
    'G': '111011101', 'H': '1010101', 'I': '101',
    'J': '1011101110111', 'K': '111010111',
    'L': '101110101', 'M': '1110111', 'N': '11101',
    'O': '11101110111', 'P': '10111011101', 'Q': '1110111010111',
    'R': '1011101', 'S': '10101', 'T': '111', 'U': '1010111',
    'V': '101010111', 'W': '101110111', 'X': '11101010111',
    'Y': '1110101110111', 'Z': '11101110101',
    # Numbers
    '1': '10111011101110111', '2': '101011101110111',
    '3': '10101011101110111', '4': '10101010111', '5': '101010101',
    '6': '11101010101', '7': '1110111010101', '8': '111011101110101',
    '9': '11101110111011101', '0': '1110111011101110111'}


def get_morse_key(val):
    for key, value in morse_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def text_to_morse(morse_file, text):
    morse_text = ''
    text = text.upper()
    for char in text:
        if not char == ' ':
            morse_text += morse_dict[char]
            morse_text += '000' 
        else:
            morse_text += '0000'
    morse_text = morse_text[:-3]

    morse_file.write(morse_text)

#def morse_to_text(text_file, morse_list):

def main():
    file_path = sys.argv[1]
    aux = file_path.split('.')
    file_extension = aux[len(aux) - 1]

    if file_extension == 'txt':
        print('Morse and Audio.\n')
        text_file = open(file_path, 'r')
        text = text_file.read()
        # text -> morse code
        morse_file = open('code.morse', 'w')
        text_to_morse(morse_file, text)
        morse_file.close()
        text_file.close()
        # TO DO text to audio

    elif file_extension == 'morse':
        print('TXT and Audio.\n')
        

    elif file_extension == 'wav':
        print('TXT and Morse.\n')
    else:
        print('Wrong extension.\n')


if (__name__ == '__main__'):
    main()
