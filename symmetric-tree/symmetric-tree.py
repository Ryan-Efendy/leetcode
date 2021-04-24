# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
            1
           /|\
          2 | 2  ✅
         / \|/ \
        3  4|4  3 
            | 
        
            1
           / \
          2   2  ❌
           \   \
            3   3
        '''
        def helper(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and helper(p.left, q.right) and helper(p.right, q.left)
        
        if not root: return True
        return helper(root, root)