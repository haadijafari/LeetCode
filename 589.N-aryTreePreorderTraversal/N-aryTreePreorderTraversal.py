"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.dummy(root, result)
        return result
    
    def dummy(self, root, results):
        if not root:
            return
        else:
            results.append(root.val)
            for child in root.children:
                self.dummy(child, results)