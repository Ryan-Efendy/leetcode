# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        sizeA, sizeB = 0, 0
        dummyA = headA
        while dummyA:
            sizeA += 1
            dummyA = dummyA.next
        
        dummyB = headB
        while dummyB:
            sizeB += 1
            dummyB = dummyB.next
        
        diff = sizeA - sizeB if sizeA > sizeB else sizeB - sizeA
        
        headC, headD = (headA, headB) if sizeA > sizeB else (headB, headA)
        while diff:
            headC = headC.next
            diff -= 1
            
        while headC and headD and headC != headD:
            headC = headC.next
            headD = headD.next
        
        return headC if headC == headD else None
