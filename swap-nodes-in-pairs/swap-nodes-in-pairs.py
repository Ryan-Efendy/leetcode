# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
               \U0001f447 nxt
        \U0001f921 ->1->2->3->4->❌ 
        \U0001f446  \U0001f446
       prev cur
              ____          nxt, nxtNxt = cur.next, curr.next.next #save ptrs
             /    \         nxt.next = curr
        \U0001f921  1<-2  3->4->❌  nxt.next = curr
         \____/             prev.next = nxt
        \U0001f446  \U0001f446 \U0001f446            prev, curr = curr, nxtNxt # update ptrs
       prev cur nxt        
        '''
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        
        # at least 2 nodes to reverse
        while curr and curr.next:
            # save ptrs
            nxt, nxtNxt = curr.next, curr.next.next

            # reverse this pair
            nxt.next = curr
            curr.next = nxtNxt
            prev.next = nxt

            # update ptrs
            prev = curr
            curr = nxtNxt

        return dummy.next