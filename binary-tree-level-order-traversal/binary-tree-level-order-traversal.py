# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        queue = [root]
        while queue:
            tmp, n  = [], len(queue)
            while n:
                curr = queue.pop(0)
                tmp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                n -= 1
            res.append(tmp)
        return res