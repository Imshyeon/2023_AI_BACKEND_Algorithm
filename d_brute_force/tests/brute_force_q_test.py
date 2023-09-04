import unittest
import random
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/d_brute_force')
from c_brute_force_q import *

class TestQuiz(unittest.TestCase):
    def test_doom(self):
        n = round(random.randrange(1,11))
        # print(dooms_day(n), 'n : ', n)
        print(doom_day(n), 'n : ', n)
        
    def test_dwarf(self):
        arr = [round(random.randrange(10,15)) for _ in range(7)]
        t = 100 - sum(arr)
        arr[6] = arr[6] + t
        
        arr.append(round(random.randrange(1,20)))
        arr.append(round(random.randrange(1,20)))

        print(dwarf(arr))
        print(dwarf_ans(arr))
        
if __name__ == '__main__':
    unittest.main()