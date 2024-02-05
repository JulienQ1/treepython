#tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if self.val:
            if key < self.val:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.val:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.val = key
            
    def depth(self) -> int:
        return 1 +max(self.right.depth() if self.right is not None else 0, self.left.depth() if self.left is not None else 0)

# Binary search Tree

class Record:
    def __init__(self, key, data):
        self.key = key
        self.data = data

class BSTIndex:
    def __init__(self):
        self.root = None

    def insert(self, record):
        # This is a simplified version of the BST insert method
        if self.root is None:
            self.root = Node(record.key)
        else:
            self.root.insert(record.key)

    def search(self, key):
        # This is a simplified version of the BST search method
        if self.root is None:
            return None
        else:
            return self.root.search(key)
        

#BstGreg



