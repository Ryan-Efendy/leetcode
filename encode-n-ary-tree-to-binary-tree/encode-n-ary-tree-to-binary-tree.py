"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    # traverse N-ary tree in parallel with constructing BinaryTree -> pair(n-ary_tree_node, binary_tree_node).
    def encode(self, nt_root: 'Node') -> TreeNode:
        if not nt_root: return None
        bt_root = TreeNode(nt_root.val)
        queue = collections.deque([(bt_root, nt_root)])
        # traverse each child one by one
        while queue:
            parent, curr = queue.popleft()
            prevBNode = headBNode = None
            
            for child in curr.children:
                newBNode = TreeNode(child.val)
                # chain this child node with its previous neighbor sibling node
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode
                prevBNode = newBNode
                # add child node into queue
                queue.append((newBNode, child))
        
            # use the first child in the left node of parent
            parent.left = headBNode
        return bt_root
                
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, bt_root: TreeNode) -> 'Node':
        if not bt_root: return None
        nt_root = Node(bt_root.val, [])
        queue = collections.deque([(nt_root, bt_root)])
        
        while queue:
            parent, curr = queue.popleft()
            
            firstChild = curr.left
            sibling = firstChild
            
            while sibling:
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right
                
        return nt_root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))