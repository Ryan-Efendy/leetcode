# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        n = 3  

        [1,null,3,2]  [1,null,2,null,3]    [2,1,3]
        1                     1               2
         \                     \             / \
          3                     2           1   3
         /                       \
        2                         3 
        
        [3,1,null,null,2]  [3,2,null,1]
                3                3
               /                /
              1                2
               \              /
                2            1
                
        numTree[3] = numTree[0] * numTree[2] +
                     numTree[1] * numTree[1] +
                     numTree[2] * numTree[0] +
        '''
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick a root nodes[i]
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1) # nodes[start:i-1]
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end) # nodes[i+1:end]
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []