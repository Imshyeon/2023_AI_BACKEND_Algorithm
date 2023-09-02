import unittest
import sys
sys.path.append(r'C:\Users\KSH\Desktop\CODE\Algorythm\b_datastructure')
from b_hashtable_q import *

class TestHashTableQ(unittest.TestCase):
    def test_q(self):
        texts = ['hashtable','samsung','aabb']
        for text in texts:
            print(find_uniq_char(text))
            # find_uniq_char(text)
            
if __name__ == '__main__':
    unittest.main()