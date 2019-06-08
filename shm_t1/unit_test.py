import unittest
from text_functions import text_to_morse
from morse_functions import morse_to_text

class my_tests(unittest.TestCase):

    def test_text_to_morse(self):
        word = 'computador'
        result = '11101011101000111011101110001110111000101110111010001010111000111000101110001110101000111011101110001011101'
        self.assertEqual(text_to_morse(word), result)

    def test_morse_to_text(self):
        morse = '101010100010001011101010001011101010001110111011100000001011101110001110111011100010111010001011101010001110101'
        result = 'HELLO WORLD'
        self.assertEqual(morse_to_text(morse), result)

if __name__ == '__main__':
    unittest.main()