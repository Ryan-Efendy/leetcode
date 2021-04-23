# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        we need to check at every node if s & t are same
        '''
        if not p and not q:
            return True
        if not q: # we're done checking T
            return True 
        if not p: # there's something in T that's not in S 
            return False
        return self.isSameTree(p, q) or self.isSubtree(p.left, q) or self.isSubtree(p.right, q)
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:return True
        if not p or not q: return False
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)