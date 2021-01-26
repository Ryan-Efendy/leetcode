# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head
        size = 0
        sentinel = ListNode(-1)
        sentinel.next = head
        head = sentinel
        dummy = head.next
        while dummy:
            size += 1
            dummy = dummy.next
        n = size - n
        dummy = head
        while n:
            dummy = dummy.next
            n -= 1
        dummy.next = dummy.next.next
        return head.next
        
