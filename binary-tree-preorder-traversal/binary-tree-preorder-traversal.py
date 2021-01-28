# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode, res: List[int]) -> None:
            if not root: return
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
        
        res = []
        preorder(root, res)
        return res
        