import unittest
import sys
sys.path.append(r'C:\Users\KSH\Desktop\CODE\Algorythm\b_datastructure')
from b_hashtable import *

class TestHashTable(unittest.TestCase):
    def test_add(self):
        hashtable = HashTable()
        hashtable.add('a', 100)
        hashtable.add('b', 100)
        hashtable.add('c', 100)
        hashtable.add('d', 100)
        hashtable.add('d', 101)
        print(hashtable)
        # hashtable.add(10,10) 문자열만 반환하도록 설정했다. 따라서 이렇게 하면 TypeError
    
    def test_set(self):
        hashtable = HashTable()
        hashtable.add('a', 100)
        hashtable.set('a', '히히히')
        hashtable.add('b', 100)
        hashtable.set('b', '크크크')
        print(hashtable)
        
        
    def test_get(self):
        hashtable = HashTable()
        hashtable.add('a','blur')
        #contains 확인
        if 'a' in hashtable:
            print('yes!')
        self.assertEqual('blur',hashtable.get('a'))
        print(hashtable.get('a'))
        
    def test_contains(self):
        hashtable = HashTable()
        for i in range(10):
            hashtable.add(str(i),i)
        if '9' in hashtable:
            print('9를 키로 가지는 데이터가 존재.')
        else:
            print('존재하지 않는 키 값')
            
    def test_iter(self):
        hashtable = HashTable()
         
        for i in range(10):
            hashtable.add(str(i),i)
        
        for e in hashtable:
            print(e)
            
        
if __name__ == '__main__':
    unittest.main()