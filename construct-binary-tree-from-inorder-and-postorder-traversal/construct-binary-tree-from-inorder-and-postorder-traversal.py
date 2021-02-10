# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(inorder, postorder):
            if not inorder or not postorder: return None
            root = TreeNode(postorder[-1])
            idx = idx_map[postorder[-1]]

            root.left = self.buildTree(inorder[:idx], postorder[:idx])
            root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(inorder, postorder)