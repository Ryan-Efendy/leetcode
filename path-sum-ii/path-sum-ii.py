# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def helper(root: TreeNode, targetSum: int, paths: List[int]):
            if not root:
                return False
            paths.append(root.val)
            if not root.left and not root.right and targetSum - root.val == 0:
                res.append(paths)
                return
            helper(root.left, targetSum - root.val, paths[:])
            helper(root.right, targetSum - root.val, paths[:])
        
        helper(root, targetSum, [])
        return res