import unittest
import sys
sys.path.append(r'C:\Users\KSH\Desktop\CODE\Algorythm\b_datastructure')
from a_list_q import *
import random

class TestListQ(unittest.TestCase):
    def test_max(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        self.assertEqual(max(arr),check_max(arr))
        # print(len(arr))

    def test_max2(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        answer=check_max2(arr)
        arr.sort(reverse=True)
        expect = arr[:2]
        self.assertEqual(expect, answer)
        
    def test_palindrome(self):
        texts = ['AAAABBBBBBAAAA','tomato', '토마토', '기러기' ,'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if(check_palindrome(text)):
                print(text + ' 는 회문입니다.')
            
if __name__ == '__main__':
    unittest.main()