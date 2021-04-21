# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            levelSize = len(res)
            level = []
            for _ in range(n):
                node = queue.popleft()
                if node:
                    if levelSize % 2 == 0:
                        level.append(node.val)
                    else:
                        level.insert(0, node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res