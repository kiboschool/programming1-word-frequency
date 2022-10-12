import unittest
from main import *

# Retribution, Ida B. Luckie
# https://opinion.premiumtimesng.com/2018/10/19/sol-plaatje-prophesying-the-future-of-his-dreams-by-kole-omoto%E1%B9%A3o/
with open("poem.txt") as f:
    POEM = f.read()

class Test(unittest.TestCase):
    def test_word_frequency(self):
        frequencies = word_frequency(POEM)
        self.assertEqual(frequencies["pride"], 1)
        self.assertEqual(frequencies["be"], 2)
        self.assertEqual(frequencies["the"], 6)
        self.assertEqual(frequencies["doom"], 1)
        self.assertEqual(frequencies["to"], 5)
        self.assertEqual(frequencies["its"], 4)
        self.assertEqual(frequencies["splendour"], 1)

if __name__ == '__main__':
    unittest.main()
