import unittest
from treebalanced import AVLTree, Node

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def test_insert(self):
        root = None
        nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
        for num in nums:
            root = self.avl.insert(root, num)

        # Check the balance of the AVL tree
        self.assertEqual(self.avl.getBalance(root), 1)

if __name__ == '__main__':
    unittest.main()