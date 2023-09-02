import unittest
import sys
sys.path.append(r'C:\Users\KSH\Desktop\CODE\Algorythm\b_datastructure')
from a_list import *


class TestList(unittest.TestCase):
#------------------------------         
    def test_append(self):
        list=LinkedList()
        
        for i in range(10):
            list.append(i)
            
        print(list)
#------------------------------             
    def test_prepend(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i) 
                
        list.prepend(10000)    
        print(list)
#------------------------------             
    def test_insert(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i)   
              
        list.insert(2,10000)    
        print(list)
#------------------------------     
    def test_len(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i)     
        print(len(list))
#------------------------------                 
    def test_pop(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i)     
        print(list.pop())   # 9 
        print(list)         # [0, 1, 2, 3, 4, 5, 6, 7, 8]
#------------------------------        
    def test_popleft(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i)     
            
        print(list.popleft()) 
        print(list)  
#------------------------------     
    def test_remove(self):   
        list=LinkedList()
        
        for i in range(10):
            list.append(i)     
        
        print(list.remove(7)) 
        print(list) 
#------------------------------ 
    def test_iter(self):
        list=LinkedList()
        
        for i in range(10):
            list.append(i) 
            
        for e in list:
            print(e)
#------------------------------ 
    def test_reverse(self):
        list=LinkedList()
        
        for i in range(10):
            list.append(i) 
        
        list.reverse()
        print(list)
        


if __name__ == '__main__':
    unittest.main()
    