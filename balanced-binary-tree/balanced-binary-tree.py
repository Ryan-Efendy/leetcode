# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(root: TreeNode, depth) -> int:
            if not root: return 0
            if depth == -1: return depth
            
            left = helper(root.left, depth)
            right = helper(root.right, depth)
            if left == -1 or right == -1 or abs(left-right) > 1: return -1
            return max(left, right)+1

        if not root: return True
        if helper(root, 0) != -1: return True
        return False
        
        
        