import Anagrams
import unittest

class Test_AreAnagrams(unittest.TestCase):
    
    def test_Anagrams(self):
        f = ('aam', 'ama')
        self.assertTrue(f == Anagrams.anagrams[0])

    
if __name__ == '__main__':
    unittest.main()