# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode, res: List[int]) -> None:
            if root:
                postorder(root.left, res)
                postorder(root.right, res)
                res.append(root.val)
            
        res = []
        postorder(root, res)
        return res