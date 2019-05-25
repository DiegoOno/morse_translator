import sys
from text_functions import text_to_morse, text_to_audio
from morse_functions import morse_to_text, morse_to_audio

def main():
    file_path = sys.argv[1]
    aux = file_path.split('.')
    file_extension = aux[len(aux) - 1]

    if file_extension == 'txt':
        print('Morse and Audio.\n')
        text_file = open(file_path, 'r')
        text = text_file.read()
        # text -> morse code
        morse_file = open('out/code.morse', 'w')
        morse_code = text_to_morse(text)
        morse_file.write(morse_code)
        text_to_audio(text)
        morse_file.close()
        text_file.close()
        
    elif file_extension == 'morse':
        print('TXT and Audio.\n')
        # morse -> text
        text_file = open('out/text.txt', 'w')
        morse_file = open(file_path, 'r')
        morse_code = morse_file.read()
        text = morse_to_text(morse_code)
        text_file.write(text)
        morse_to_audio(morse_code)
        morse_file.close()
        text_file.close()   
        
        
    elif file_extension == 'wav':
        print('TXT and Morse.\n')
    else:
        print('Wrong extension.\n')


if (__name__ == '__main__'):
    main()
