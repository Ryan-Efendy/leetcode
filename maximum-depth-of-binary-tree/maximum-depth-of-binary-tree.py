# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root, 0)
        
    def helper(self, root, res):
        if not root: return res
        left = self.helper(root.left, res+1)
        right = self.helper(root.right, res+1)
        if left > right:
            return left
        else:
            return right