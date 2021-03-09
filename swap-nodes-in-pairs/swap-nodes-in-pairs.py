# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        d1 = d = ListNode(-1)
        d.next = head
        
        if not d.next or not d.next.next:
            return head

        while d.next and d.next.next:
            p, q = d.next, d.next.next
            d.next = q
            p.next = q.next
            q.next = p
            
            d = p
        return d1.next
        
        