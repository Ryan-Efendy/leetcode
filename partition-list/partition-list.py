# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(), ListNode()
        lessThanHead, greaterThanHead = left, right

        while head:
            if head.val < x:
                lessThanHead.next = head
                lessThanHead = lessThanHead.next
            else:
                greaterThanHead.next = head
                greaterThanHead = greaterThanHead.next
            head = head.next

        lessThanHead.next = right.next
        greaterThanHead.next = None
        return left.next