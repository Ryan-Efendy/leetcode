# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        https://www.youtube.com/watch?v=ptYUCjfNhJY
        https://www.youtube.com/watch?v=MbN_mhJntHg
        
        add node of each LL into the heap. Pop node from minHeap and make it the next node in the dummyList until minHeap is empty.
        Time: O(Nlogk) Space: O(N)
        '''
        dummy = node = ListNode(-1)
        minHeap = []
        for lst in lists:
            while lst:
                heappush(minHeap, lst.val)
                lst = lst.next
                
        while minHeap:
            node.next = ListNode(heappop(minHeap))
            node = node.next
        return dummy.next
