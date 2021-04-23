# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
                1           2              1+2               3
               / \         / \                              / \
              3   2   +   1   3    =>  3+1      2+3        4   5
             /             \   \                          / \   \ 
            5               4   7    5+0  0+4      0+7   5   4   7   
        Output: [3,4,5,5,4,null,7]
        
        '''
        # base case
        if not p and not q: return None
        # merge
        pVal = p.val if p else 0
        qVal = q.val if q else 0
        
        root = TreeNode(pVal + qVal)
        
        root.left = self.mergeTrees(p.left if p else None, q.left if q else None)
        root.right = self.mergeTrees(p.right if p else None, q.right if q else None)
        
        return root