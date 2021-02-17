# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, i, j):
            if i >= j: return
            mid = (i + j) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, i, mid)
            root.right = helper(nums, mid+1, j)
            return root
        
        return helper(nums, 0, len(nums))