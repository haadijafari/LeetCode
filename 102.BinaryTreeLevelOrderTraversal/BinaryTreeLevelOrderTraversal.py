# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        self.dummy(root, result, 0)
        
        return result

    def dummy(self, root, result, level):
        if not root:
            return

        try:
            result[level].append(root.val)
        except IndexError:
            result.append([root.val])
        
        self.dummy(root.left, result, level + 1)
        self.dummy(root.right, result, level + 1)