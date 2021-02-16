# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        dummy = root
        while dummy:
            if dummy.val < val:
                if dummy.right:
                    dummy = dummy.right
                else: 
                    dummy.right = TreeNode(val)
                    return root
            else:
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy.left = TreeNode(val)
                    return root
        
            