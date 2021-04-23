# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
  H=5            4
  \U0001f446            /  \
  H=4         3    2
  \U0001f446         / \  /  \  
❌ H=3,1     2  0  1   1       
  \U0001f446       / \   / \ / \   
✅ H=2,1   1  0  0  0 0  0 
  \U0001f446     /
✅ H=1   0 
        '''
        def dfs(root: TreeNode) -> int:
            # base case 1 null/empty node
            if not root: return 0
            # base case 2 leaf node
            if not root.left and not root.right: return 1
            
            leftHeight, rightHeight = dfs(root.left), dfs(root.right)
            
            # check if balance
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight-rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1
            
        return dfs(root) >= 0
            
            