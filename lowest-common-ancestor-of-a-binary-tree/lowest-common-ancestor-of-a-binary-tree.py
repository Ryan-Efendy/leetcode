# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root: return None
            # if both returns a valid node -> p, q are in different subtrees, then root will be their LCA.
            if root == p or root == q: return root
            left = dfs(root.left)        
            right = dfs(root.right)
            if left and right: return root
            # if only one valid node returns, which means p, q are in the same subtree, return that valid node as their LCA.
            return left if left else right
        
        return dfs(root)