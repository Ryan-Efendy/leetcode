# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def helper(self, inorder, i1, i2, postorder, p1, p2):
        if i1 > i2: return None
        root = TreeNode(postorder[p2])
        idx = inorder.index(root.val)
        delta = idx - i1
        
        root.left = self.helper(inorder, i1, idx-1,
                                postorder, p1, p1+delta-1)
        root.right = self.helper(inorder, i1+delta+1, i2,
                                 postorder, p1+delta, p2-1)
        return root