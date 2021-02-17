"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(root, level):
            if not root: return 0 
            max_depth = 0
            for child in root.children:
                max_depth = max(max_depth, helper(child, level))
            return max_depth + 1

        
        if not root: return 0
        return helper(root, 0)