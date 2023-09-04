import random
import unittest
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/b_datastructure')
from d_queue import *

class TestQueue(unittest.TestCase): # TestProgram으로 잘못 넣었더니 오류 발생
                                    #(TypeError: TestQueue.test_enqueue() missing 1 required positional argument: 'self' )
    def test_enqueue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        print(queue)

    def test_dequeue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        for i in range(10):
            print(queue.dequeue(), end=' -> ')
        print(queue)
        
    def test_q_card(self):  # 얘는 아무것도 아닌 거 같음
        queue = Queue()
        for i in range(1,5):
            queue.enqueue(i)
        # print(result)
if __name__ == '__main__':
    unittest.main()