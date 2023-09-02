import random
import unittest
import sys
sys.path.append(r'C:\Users\KSH\Desktop\CODE\Algorythm\b_datastructure')
from c_stack import *

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        print(stack)
        
    def test_pop(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
            
        for i in range(10):
            print(stack.pop(), end='\n')
            
    def test_pick(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
            
        for i in range(10):
            print(stack.peek(), end='\n')    
        print(f'스택이 비었냐? {stack.is_empty()}')
        print('---')  
        for i in range(10):
            print(stack.pop(), end='\n')    
        print(f'스택이 비었냐? {stack.is_empty()}')
                              

if __name__ == '__main__':
    unittest.main()