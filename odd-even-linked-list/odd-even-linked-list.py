# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        odd = head
        evenDummy = head.next
        even = evenDummy
​
        while odd or even:
            if odd:
                odd.next = odd.next.next if odd.next else None
                if not odd.next: break
                odd = odd.next
            if even:
                even.next = even.next.next if even.next else None
                even = even.next
​
        odd.next = evenDummy
        return head
