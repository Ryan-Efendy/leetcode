# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''
        Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
                3
               / \
              9   20
                  / \ 
                 15  7
                 
       postorder = [x0,x1,x2,x3,x4,x5,x6]    1. find root from postorder
                    <--\U0001f446---> <--\U0001f446--->\U0001f446      
                      left     right   root  2. divide left & right subtree in inorder
        inorder  = [x0,x1,x2,x3,x4,x5,x6]
                    <--\U0001f446--->\U0001f446  <--\U0001f446---> 
                    left    root   right
        '''
        value_to_idx = dict()
        for idx, value in enumerate(inorder):
            value_to_idx[value] = idx

        def helper(inorder, inStart, inEnd, postorder, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None
            root = TreeNode(postorder[postEnd])
            inRoot = value_to_idx[root.val]
            numsLeft = inRoot - inStart
            root.left = helper(inorder, inStart, inRoot - 1, postorder, postStart, postStart + numsLeft - 1)
            root.right = helper(inorder, inStart + numsLeft + 1, inEnd, postorder, postStart + numsLeft, postEnd - 1)
            return root

        return helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)