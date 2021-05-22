import Anagrams
import unittest

class Test_GetAnagrams(unittest.TestCase):

    def test_getAnagrams(self):
        Anagrams.wordList = ['amor', 'huevo', 'roma']
        self.assertTrue(Anagrams.getAnagram(Anagrams.wordList) == [('amor', 'roma')])


class Test_NotDuplicate(unittest.TestCase):

    def test_isNotDuplicated(self):
        line = ('amor', 'roma')
        self.assertTrue(Anagrams.isNotDuplicated(line))

class Test_Duplicate(unittest.TestCase):

    def test_isDuplicated(self):
        line = ('amor', 'amor')
        self.assertFalse(Anagrams.isNotDuplicated(line))

    
if __name__ == '__main__':
    unittest.main()