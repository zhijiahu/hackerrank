
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


          100
         /   \
        90    101
       /  \
      89  102
"""

import sys

def checkBST(root):
    return checkNode(root, 0, sys.maxsize)


def checkNode(node, min, max):
    if node is None:
        return False

    if node.data < min:
        return False

    if node.data > max:
        return False
    
    if node.left is not None:
        if node.left.data < node.data:
            if not checkNode(node.left, min, node.data):
                return False
        else:
            return False
                
    if node.right is not None:
        if node.right.data > node.data:
            if not checkNode(node.right, node.data, max):
                return False
        else:
            return False

    return True
