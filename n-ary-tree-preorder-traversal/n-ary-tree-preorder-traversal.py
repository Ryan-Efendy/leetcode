"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def helper(root, res):
            if not root: return
            res.append(root.val)
            for child in root.children:
                helper(child, res)
            return res
    
        res = []
        helper(root, res)
        return res