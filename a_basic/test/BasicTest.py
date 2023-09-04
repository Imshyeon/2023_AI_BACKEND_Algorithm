import unittest
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/a_basic')
from c_math import *
from math import *
import random

class TestBasic(unittest.TestCase):
    def test_is_prime(self):
        # print('hello test')
        # self.assertTrue(True)
        self.assertTrue(is_prime(7))    # 나
        # self.assertTrue(is_prime_ans(7))    # 답1
    def test_is_prime2(self):
        self.assertTrue(is_prime_plus(7))

    def test_primes(self):
        print(prime_numbers(150))
    
    def test_gcd1(self):
        left = round(random.randrange(1,1000))
        right= round(random.randrange(1,1000))
        
        if left < right:
            left,right = right, left    # 둘 중에 더 큰 값을 left로 함
            
        self.assertTrue(gcd(left,right) == gcd2(left,right))
    
    def test_lcm(self):
        left = round(random.randrange(1,1000))
        right= round(random.randrange(1,1000))
        
        if left < right:
            left,right = right, left    # 둘 중에 더 큰 값을 left로 함
            
        self.assertTrue(lcm(left,right) == lcm1(left,right))
        
    def test_factorial(self):
        # print(fac1(4))
        n = round(random.randrange(1,20))
        self.assertEqual(factorial(n),factorial_tail(n))
        
    def test_fibonacci(self):
        for i in range(1,8):
            # print(fibonacci(i))
            # print(fibo_recursive(i))
            print(fibo_tail(i))
        
if __name__ == '__main__':
    unittest.main()
    