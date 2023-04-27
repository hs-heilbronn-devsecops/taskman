import unittest

def reverse_string(string):
    return string[::-1]

class TestReverseString(unittest.TestCase):

    def test_reverse_empty_string(self):
        result = reverse_string('')
        self.assertEqual(result, '')

    def test_reverse_single_character_string(self):
        result = reverse_string('a')
        self.assertEqual(result, 'a')

    def test_reverse_long_string(self):
        result = reverse_string('hello, world!')
        self.assertEqual(result, '!dlrow ,olleh')

if __name__ == '__main__':
    unittest.main()