import unittest
from main import *

# Retribution, Ida B. Luckie
# https://opinion.premiumtimesng.com/2018/10/19/sol-plaatje-prophesying-the-future-of-his-dreams-by-kole-omoto%E1%B9%A3o/
poem = """
    Alas, My Country!  Thou wilt have no need
    Of enemy to bring thee to thy doom . . .
    For not alone by war a nation falls.
    Though she be fair, serene as radiant morn,
    Though girt by seas, secure in armament,
    Let her but spurn the vision of the Cross;
    Tread with contemptuous feet on its command
    Of mercy, Love and Human Brotherhood,
    And she, some fateful day, shall have no need
    Of enemy to bring her to the dust.

    Some day, though distant it may be -- with God
    A thousand years are but as yesterday --
    The germs of hate, injustice, violence,
    Like an insidious canker in the blood,
    Shall eat that nation's vitals.  She shall see
    Break forth the blood-red tide of anarchy,
    Sweeping her plains, laying her cities low,
    And bearing on its seething, crimson flood
    The wreck of Government, of home, and all
    The nation's pride , its splendour and its power.
    On with relentless flow, into the seas
    Of God's eternal vengeance wide and deep.
    But, for God's grace!  Oh may it hold thee fast,
    My Country, until justice shall prevail
    O'er wrong and o'er oppression's cruel power,
    And all that makes humanity to mourn.
"""

class Test(unittest.TestCase):
    def test_word_frequency(self):
        frequencies = word_frequency(poem)
        self.assertEqual(frequencies["pride"], 1)
        self.assertEqual(frequencies["be"], 2)
        self.assertEqual(frequencies["the"], 6)
        self.assertEqual(frequencies["doom"], 1)
        self.assertEqual(frequencies["to"], 5)
        self.assertEqual(frequencies["its"], 4)
        self.assertEqual(frequencies["splendour"], 1)

if __name__ == '__main__':
    unittest.main()
