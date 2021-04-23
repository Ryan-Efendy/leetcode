# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque()
        queue.append([root, 0])
        maxWidth = 1

        while queue:
            start = queue[0][1] # first item in queue
            end = queue[-1][1] # last item in queue
            maxWidth = max(maxWidth, end - start + 1)

            for _ in range(len(queue)):
                curr, idx = queue.popleft()
                if curr.left:
                    queue.append([curr.left, 2*idx+1])
                if curr.right:
                    queue.append([curr.right, 2*idx+2])

        return maxWidth