# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
        head = [1,2,3,4,5], k = 2
           |     |     |                       nxt
           |     |     |                       \U0001f447               cur.next = prev.next
        \U0001f921 ->1->2->3->4->5->❌        \U0001f921 ->1->2->3->4->5->❌     prev.next.next = next
           |     |     |              \U0001f446     \U0001f446                 prev.next = cur
           |     |     |             prev   cur      nxt       prev = prev.next
                                                     \U0001f447 
        \U0001f921 ->2->1->3->4->5->❌        \U0001f921 ->2->1->3->4->5->❌ 
           |     |     |                     \U0001f446    \U0001f446    
           |     |     |                    prev  cur
        \U0001f921 ->2->1->4->3->5->❌ 
        Output: [2,1,4,3,5]
        
        '''
        dummy = ListNode(next=head)
        curr, prev = head, dummy

        while curr:
            tail = curr
            idx = 0

            while curr and idx < k:
                curr = curr.next
                idx += 1
                # left-out nodes remain as is
                if idx != k:
                    prev.next = tail
                else:
                    prev.next = self.reverse(tail, k)
                    prev = tail
        return dummy.next

    def reverse(self, head: ListNode, k: int):
        prev, cur = None, head
        while cur and k > 0:
            nxt = cur.next # tmp store nxt
            cur.next = prev #reverse curr node
            prev = cur # before we move to the next node, point prev to curr
            cur = nxt # advance to next node
            k -= 1
        return prev