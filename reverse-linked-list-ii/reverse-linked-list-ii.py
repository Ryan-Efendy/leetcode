# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        head = [1,2,3,4,5], n = 2, m = 4
        Output: [1,4,3,2,5]
        
           n   m
        [1,2,3,4,5] -> [1,2,5] -> [1,3,2,5] -> [1,4,3,2,5]
        
                 curr
                  \U0001f447  
        \U0001f921 -> 1 -> 2-> 3 -> 4 -> 5 -> NULL
             \U0001f446        \U0001f446
           prev       nxt
        
        Goal: end of range m to n (at pos n) to be the next node of before
        1. traverse until we reach `n` and we keep assigning `nxt` nodes to be next to `prev`
        2. reverse the inner links in the range m to n
        3. we want the 'curr' of the range to be the end of the range after reversing
        
        '''
        dummy = ListNode(next=head)
        prev = dummy

        for _ in range(0, m - 1):
            prev = prev.next

        curr = prev.next
        nxt = curr.next

        for _ in range(0, n - m):
            curr.next = nxt.next #1
            nxt.next = prev.next #2
            prev.next = nxt      #3
            nxt = curr.next      #4

        return dummy.next
