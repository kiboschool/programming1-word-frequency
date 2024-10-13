import unittest
from main import *

# Retribution, Ida B. Luckie
# https://opinion.premiumtimesng.com/2018/10/19/sol-plaatje-prophesying-the-future-of-his-dreams-by-kole-omoto%E1%B9%A3o/
with open("poem.txt") as f:
    POEM = f.read()

WITH_FULLSTOP_STR = 'I cannot see you. Can you really see me?'
HINT_MSG = 'Try your word_frequency function with the following sentence: "I see you. Do you see me?" Check the frequency of the word "you".'

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

    def test_frequency_not_hardcoded(self):
        frequencies = word_frequency(WITH_FULLSTOP_STR)
        print(frequencies)
        self.assertEqual(frequencies["you"], 2, HINT_MSG)
        self.assertEqual(frequencies["really"], 1)
        self.assertEqual(frequencies["cannot"], 1)
        self.assertEqual(frequencies["I"], 1)
        self.assertEqual(frequencies["see"], 2)

if __name__ == '__main__':
    unittest.main()