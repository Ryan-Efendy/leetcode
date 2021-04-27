# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode()
        minHeap = []

        # heap keeps (node val, node id, and node). Smallest node value has the most priority.
        for node in lists:
            if node:
                # id(node) is for the comparator in case two nodes are of the same value
                # workaround: cannot modify ListNode to create custom comperator
                heapq.heappush(minHeap, (node.val, id(node), node))

        # While our priority queue still has nodes
        while minHeap:
            # Get the smallest node inside our priority queue and remove it
            curr.next = heapq.heappop(minHeap)[2]
            
            curr = curr.next

            # If our node has a next, add it to our priority queue
            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, id(curr.next), curr.next))

        return dummy.next
