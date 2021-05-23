import AnagramsFromFile
import unittest

class Test_GetAnagramsFromFile(unittest.TestCase):

    def test_getAnagramsFromFile(self):
        AnagramsFromFile.wordList = ['amor', 'huevo', 'roma']
        self.assertTrue(AnagramsFromFile.getAnagram(AnagramsFromFile.wordList) == [('amor', 'roma')])


class Test_NotDuplicate(unittest.TestCase):

    def test_isNotDuplicated(self):
        line = ('amor', 'roma')
        self.assertTrue(AnagramsFromFile.isNotDuplicated(line))

class Test_Duplicate(unittest.TestCase):

    def test_isDuplicated(self):
        line = ('amor', 'amor')
        self.assertFalse(AnagramsFromFile.isNotDuplicated(line))

    
if __name__ == '__main__':
    unittest.main()