# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Time complexity: O(n) & Space complexity: O(h)
        
        Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
        
                _______3️⃣______
               /              \
            __5️⃣__          ___1️⃣__
           /      \        /      \
           6      _2       0       8
                 /  \
                 7   4
        
        Input: p = 5, q = 1
        Output: 3
        Explanation: The LCA of of nodes 5 and 1 is 3.
        
                _______3______
               /              \
            __5️⃣__          ___1__
           /      \        /      \
           6      _2       0       8
                 /  \
                 7   4️⃣        
        
        Input: p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

        For a given root, recursively call LCA(root.left, p, q) and LCA(root.right, p, q
        '''
        def dfs(root):
            if not root: return root
            # if both returns a valid node -> p, q are in different subtrees, then root will be their LCA.
            if root == p or root == q: return root
            left = dfs(root.left)        
            right = dfs(root.right)
            if left and right: return root
            # if only one valid node returns, which means p, q are in the same subtree, return that valid node as their LCA.
            return left if left else right
        
        return dfs(root)
            