
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if root is None:
        return False
        
    if root.left is not None:
        if root.left.data < root.data:
            if not checkBST(root.left):
                return False
        else:
            return False
                
    if root.right is not None:
        if root.right.data > root.data:
            if not checkBST(root.right):
                return False
        else:
            return False

    return True
