# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        curr_diff, min_diff = 0, math.inf
        min_diff_node = None
        while root:
            curr_diff = abs(root.val - target)
            if curr_diff < min_diff:
                min_diff = curr_diff
                min_diff_node = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return min_diff_node
            