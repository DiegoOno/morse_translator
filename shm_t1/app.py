import sys

morse_dict = {
            # Letters
            'A': '0111', 'B': '111000', 'C': '11101110',
            'D': '11100', 'E': '0', 'F': '001110', 'G': '1111110',
            'H': '0000', 'I': '00', 'J': '0111111111', 'K': '1110111',
            'L': '011100', 'M': '111111', 'N': '1110', 'O': '111111111',
            'P': '01111110', 'Q': '1111110111', 'R': '01110', 'S': '0000',
            'T': '111', 'U': '00111', 'V': '000111', 'W': '0111111',
            'X': '11100111', 'Y': '1110111111', 'Z': '11111100',
            # Numbers
            '1': '0111111111111', '2': '00111111111', '3': '000111111111',
            '4': '0000111', '5': '00000', '6': '1110000', '7': '111111000',
            '8': '11111111100', '9':'1111111111110', '0': '111111111111111', ' ': ' '}

def text_to_morse(text_file, text):
    text = text.upper()
    for char in text:
        text_file.write(morse_dict[char])
        text_file.write('\n')

def main():
    #file_path = sys.argv[1]
    #aux = file_path.split('.')
    #file_extension = aux[len(aux) - 1]

    # if file_extension == 'txt':
    #     print('Morse and Audio.\n')
    # elif file_extension == 'morse':
    #     print('TXT and Audio.\n')
    # elif file_extension == 'wav':
    #     print('TXT and Morse.\n')
    # else:
    #     print('Wrong extension.\n')
    morse_file = open('code.morse', 'w')
    text_to_morse(morse_file, 'Diego Kazuo Ono')
    morse_file.close()

if (__name__ == '__main__'):
    main()
