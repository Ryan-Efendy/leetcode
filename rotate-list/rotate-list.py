# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return head
        n = 0
        dummy = head
        while dummy.next:
            n += 1
            dummy = dummy.next
        n += 1
        dummy.next = head

        k = k%n
        k = n - k
        prev, curr = dummy, dummy.next
        while k:
            prev = curr
            curr = curr.next
            k -= 1

        prev.next = None
        return curr
        
        
        