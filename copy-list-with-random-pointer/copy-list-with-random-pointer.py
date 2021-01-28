"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        
        dummy = head
        # 1
        while dummy:
            head2 = Node(dummy.val)
            head2.next = dummy.next
            dummy.next = head2
            dummy = dummy.next.next

        # 2
        dummy = head
        while dummy:
            dummy.next.random = dummy.random.next if dummy.random else None
            dummy = dummy.next.next

        # 3
        slow, fast = head, head.next
        headSlow, headFast = slow, fast
        while slow and slow.next and fast and fast.next:
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            fast = fast.next
        slow.next = None

        return headFast