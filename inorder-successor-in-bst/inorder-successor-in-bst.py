# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    idx = None
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inorder(root, p):
            res, stack = [], []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    curr = stack.pop()
                    if curr.val == p.val:
                        self.idx = len(res)
                    res.append(curr)
                    root = curr.right
            return res
        
        res = inorder(root, p)
        if self.idx+1 < len(res):
            return res[self.idx+1]
        return None

                