# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        '''
        pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
                    1
                   / \
                  2   3
                 / \ / \
                4  5 6  7 
                    
            startLeftSubTree                startLeftSubTree
                \U0001f447                             \U0001f447
        pre = [1,2,4,5,3,6,7],        pre = [1,2,4,5,3,6,7],
               \U0001f446 |_                            _|\U0001f446 endLeftSubTree
              root |                          /
                   |                        startSubTree   
                  \U0001f447 endLeftSubTree           \U0001f447   \U0001f447 endLeftSubTree
       post = [4,5,2,6,7,3,1]         post = [4,5,2,6,7,3,1]
                           \U0001f446                             \U0001f446
                           root                          root
        
        root -> Node(pre[preStart])
        root.left = constructFromPrePost(pre[preStart+1 : preStart+delta], post[postStart : postIdx])
        root.right = constructFromPrePost(pre[preStart+delta+1 : preEnd], post[postIdx+1 : postEnd-1])
        '''
        def helper(preStart, preEnd, postStart, postEnd):
            if preStart > preEnd:
                return None
            if preStart == preEnd:
                return TreeNode(pre[preStart])

            root = TreeNode(pre[preStart])
            postIdx = value_to_idx[pre[preStart + 1]]
            delta = postIdx - postStart + 1

            root.left = helper(preStart + 1, preStart + delta, postStart, postIdx)
            root.right = helper(preStart + delta + 1, preEnd, postIdx + 1, postEnd - 1)

            return root

        if not pre or not post: return None
        value_to_idx = {}
        for idx, val in enumerate(post):
            value_to_idx[val] = idx
            
        return helper(0, len(pre) - 1, 0, len(post) - 1)