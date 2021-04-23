# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        # find root by getting max val
        i = nums.index(max(nums))
        node = TreeNode(nums[i])
        
        # left subtree - nums[:1]
        node.left = self.constructMaximumBinaryTree(nums[:i])
        # right subtree - nums[i+1:]
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])

        return node