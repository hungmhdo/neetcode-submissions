# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr != None:
            arr.append(curr)
            curr = curr.next
        
        index = len(arr) - n
        del arr[index]

        if len(arr):
            newHead = curr = arr[0]
            for i in range(1, len(arr)):
                curr.next = arr[i]
                curr = curr.next
            curr.next = None
            return newHead
        return None
        

