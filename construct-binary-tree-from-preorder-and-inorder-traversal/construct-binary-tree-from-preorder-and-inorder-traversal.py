# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
            
        def helper(preorder, p1, p2, inorder, i1, i2):
            if p1 >= p2 or i1 >= i2: return None
            root = TreeNode(preorder[p1])
            # idx = inorder.index(root.val)
            idx = map_inorder[root.val]
            delta = idx - i1

            root.left = helper(preorder, p1+1, p1+1+delta,
                                inorder, i1, i1+delta)
            root.right = helper(preorder, p1+delta+1, p2,
                                inorder, i1+delta+1, i2)
            return root
            
        return helper(preorder, 0, len(preorder), inorder, 0, len(inorder))