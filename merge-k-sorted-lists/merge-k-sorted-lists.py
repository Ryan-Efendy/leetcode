# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, nodes: List[ListNode]) -> ListNode:
        '''
        lists = [  \U0001f447 
                  [1,4,5],     minHeap =  1
                  [1,3,4],               / \
                   \U0001f446                   1   2
                  [2,6]
                   \U0001f446
                ]
                
        lists = [    \U0001f447 
                  [1,4,5],     minHeap =  1
                  [1,3,4],               / \
                     \U0001f446                 1    2
                  [2,6]                / \  / \
                     \U0001f446               3   4 6
                ]
                
        lists = [      \U0001f447 
                  [1,4,5],     minHeap =  1
                  [1,3,4],               / \
                       \U0001f446               1    2
                  [2,6]                / \  / \
                       \U0001f446             3   4 6  4
                ]                    /
                                    5 
        Output: [1,1,2,3,4,4,5,6]
        
        
        '''
        minHeap = []
        # heap keeps (node val, node id, and node). Smallest node value has the most priority.
        for node in nodes: # iterate 
            while node:
                # id(node) is for the comparator in case two nodes are of the same value
                # workaround: cannot modify ListNode to create custom comperator
                # TypeError: '<' not supported between instances of 'ListNode'
                # heapq.heappush(minHeap, (node.val, id(node), node))
                heapq.heappush(minHeap, (node.val, id(node)))
                node = node.next

        dummy = curr = ListNode()
        # While our priority queue still has nodes
        while minHeap:
            # Get the smallest node inside our priority queue and remove it
            # curr.next = heapq.heappop(minHeap)[2]
            curr.next = ListNode(heapq.heappop(minHeap)[0])
            curr = curr.next

            # If our node has a next, add it to our priority queue
            # if curr.next:
            #     heapq.heappush(minHeap, (curr.next.val, id(curr.next), curr.next))

        return dummy.next
