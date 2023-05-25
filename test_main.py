import unittest
from main import *

from gradescope_utils.autograder_utils.decorators import weight

# Retribution, Ida B. Luckie
# https://opinion.premiumtimesng.com/2018/10/19/sol-plaatje-prophesying-the-future-of-his-dreams-by-kole-omoto%E1%B9%A3o/
with open("poem.txt") as f:
    POEM = f.read()

UNSEEN_STR = 'for every action there is an equal and opposite reaction. In other words, action and reaction are equal and opposite. Same in magnitude but opposing each other.'
HINT_MSG = 'Try your word_frequency function with the following sentence: "I see you. Do you see me?" Check the frequency of the word "you".'
class Test(unittest.TestCase):
    @weight(30)
    def test_word_frequency(self):
        frequencies = word_frequency(POEM)
        self.assertEqual(frequencies["pride"], 1)
        self.assertEqual(frequencies["be"], 2)
        self.assertEqual(frequencies["the"], 6)
        self.assertEqual(frequencies["doom"], 1)
        self.assertEqual(frequencies["to"], 5)
        self.assertEqual(frequencies["its"], 4)
        self.assertEqual(frequencies["splendour"], 1)

    @weight(5)
    def test_frequency_not_hardcoded(self):
        frequencies = word_frequency(UNSEEN_STR)
        print(frequencies)
        self.assertEqual(frequencies["action"], 2)
        self.assertEqual(frequencies["equal"], 2)
        self.assertEqual(frequencies["and"], 3)
        self.assertEqual(frequencies["magnitude"], 1)
        self.assertEqual(frequencies["opposite"], 2, HINT_MSG)

if __name__ == '__main__':
    unittest.main()
