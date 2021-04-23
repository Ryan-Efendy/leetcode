# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        https://www.youtube.com/watch?v=ihj4IQGZ2zc
        
        1. the first val in preorder -> root
           [3, 9, 20, 15, 7]
            \U0001f446 
        2. use root to partition the left & right subtree in inorder
           [9, 3, 15, 20, 7]
left subtree <-\U0001f446  -> right subtree    
        '''
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])
        return root