import random
import unittest
import sys
sys.path.append(r'/Users/gangsuhyeon/Desktop/AI BACKEND/Algorithm/b_datastructure')
from e_bst import *

class TestBST(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        
        for i in [10, 1002, 345, 11, 7545, 44, 12612, 232]:
            bst.insert(i)
        
        print(bst.dfs('inorder'))

    def test_dfs(self):
        bst = BinarySearchTree()
        
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)
        print(bst.dfs('inorder'))  
        print(bst.dfs('preorder'))  # 전위순회하여 결과를 반환
        print(bst.dfs('postorder'))   # 후위순회하여 결과를 반환
        
        # bst.root = Node(8)
        # bst.root.left_child = Node(3)
        # bst.root.right_child = Node(10)
        # bst.root.left_child.left_child = Node(1)
        # bst.root.left_child.right_child = Node(6)
        # bst.root.right_child.right_child = Node(14)
        # bst.root.left_child.right_child.left_child = Node(4)
        # bst.root.left_child.right_child.right_child = Node(7)
        # bst.root.right_child.right_child.left_child = Node(13)
if __name__ == '__main__':
    unittest.main()