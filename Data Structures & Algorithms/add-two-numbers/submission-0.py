# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        k = 0
        dummy = ListNode(0, None)
        curr = dummy

        while l1 and l2:
            a = l1.val
            b = l2.val
            l1 = l1.next
            l2 = l2.next
            num = a + b + k
            if num >= 10:
                num = num % 10
                k = 1
            else:
                k = 0
            node = ListNode(num, None)
            curr.next = node
            curr = curr.next
        
        while l1:
            num = l1.val + k
            l1 = l1.next
            if num >= 10:
                num = num % 10
                k = 1
            else:
                k = 0
            node = ListNode(num, None)
            curr.next = node
            curr = curr.next
        
        while l2:
            num = l2.val + k
            l2 = l2.next
            if num >= 10:
                num = num % 10
                k = 1
            else:
                k = 0
            node = ListNode(num, None)
            curr.next = node
            curr = curr.next
        
        if k != 0:
            curr.next = ListNode(1, None)
        return dummy.next
        