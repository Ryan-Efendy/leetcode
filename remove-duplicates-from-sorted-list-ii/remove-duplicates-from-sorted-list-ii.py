# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        head = 1->1->2->2->2->2->3->3->4->❌
                    __________________
                   /                  \
         \U0001f921 -->1-->1-->2-->2-->2-->2-->3-->3-->4-->❌
               \U0001f446  \U0001f446  \U0001f446       \U0001f446  \U0001f446
              cur nxt nxt.nxt  tmp tmp.nxt
        
        '''
        dummy = ListNode(next=head)
        cur = dummy
        
        while cur:
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                tmp = cur.next.next
                
                while tmp and tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                    
                cur.next = tmp.next
            else:
                cur = cur.next
        
        return dummy.next
                
                
        