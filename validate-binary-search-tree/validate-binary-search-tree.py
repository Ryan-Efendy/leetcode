# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, floor: int, ceiling: int) -> bool:
            if not root: return True
            if not (floor < root.val < ceiling): return False
            return helper(root.left, floor, root.val) and helper(root.right, root.val, ceiling)
        return helper(root, -math.inf, math.inf)