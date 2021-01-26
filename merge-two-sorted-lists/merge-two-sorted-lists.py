# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, p: ListNode, q: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while p and q:
            if p.val <= q.val:
                dummy.next = p
                p = p.next
            else:
                dummy.next = q
                q = q.next
            dummy = dummy.next
        
        if p:
            dummy.next = p
        
        if q:
            dummy.next = q
            
        return head.next
