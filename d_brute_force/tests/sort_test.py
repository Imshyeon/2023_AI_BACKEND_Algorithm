import unittest
import random
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/d_brute_force')
from a_bubble_sort import *
from b_selection_sort import *

class TestBubble(unittest.TestCase):
    def test_buble_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(bubble_sort_ans4(arr))

    def test_selection_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(selection_sort_ans(arr))
        
if __name__ == '__main__':
    unittest.main()