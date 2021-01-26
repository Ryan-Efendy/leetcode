# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1, arr2 = [], []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
            
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
            
        str1, str2 = ''.join(str(i) for i in arr1[::-1]), ''.join(str(j) for j in arr2[::-1])
        res = int(str1) + int(str2)
        arr3 = list(str(res)[::-1])
        returnHead = ListNode(-1)
        dummy = returnHead
        for num in arr3:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return returnHead.next
