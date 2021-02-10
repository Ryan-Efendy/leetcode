# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def helper(root):
            if not root: return (0, True)
            if not root.left and not root.right: return (1, True)
            left_count, left_uni_value = helper(root.left)
            right_count, right_uni_value = helper(root.right)
            
            if left_uni_value and right_uni_value:
                if root.left and root.left.val != root.val:
                    return (left_count+right_count, False)
                if root.right and root.right.val != root.val:
                    return (left_count+right_count, False)
                return (left_count+right_count+1, True)
                
            return (left_count+right_count, False)
        return helper(root)[0]
                