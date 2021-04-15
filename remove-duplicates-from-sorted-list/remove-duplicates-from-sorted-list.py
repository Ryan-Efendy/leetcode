# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        head = 1->1->2->❌
        Output: 1->2->❌
        
        Input: head = 1->1->2->3->3->❌
        Output: 1->2->3->❌

        '''
        if not head: return head
        dummy = ListNode(next=head)
        prev, curr = dummy, dummy.next
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
        