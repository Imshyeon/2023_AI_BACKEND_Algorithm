import unittest
import random
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/e_devide_conqure')
from a_merge_sort import *
from a_merge_sort2 import *
from b_quick_sort import *
from b_quick_sort2 import *

class TestMerge(unittest.TestCase):
    def test_merge(self):
        arr1 = [round(random.randrange(1,300)) for _ in range(300)]
        arr1.sort()
        
        arr2 = [round(random.randrange(1,300)) for _ in range(300)]
        arr2.sort()
        print(merge(arr1, arr2))
    
    def test_merge_sort(self):  # 0.002s
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(mergesort(arr))
        
    def test_merge_sort2(self): # 0.002s
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        mergesort2(arr, 0 ,len(arr)-1) 
        print(arr)
    
    def test_quick_sort(self):  # 0.001s
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        quicksort(arr, 0 ,len(arr)-1) 
        print(arr)
    
    def test_quick_sort2(self):  # 0.001s
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        quicksort2(arr, 0 ,len(arr)-1) 
        print(arr)
        
if __name__ == '__main__':
    unittest.main()