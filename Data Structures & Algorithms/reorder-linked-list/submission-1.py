# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = []

        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        

        newNode = []
        for i in range(len(node)//2):
            newNode.append(node[i])
            newNode.append(node[len(node)-1-i])
        
        if len(node) % 2:
            newNode.append(node[len(node)//2])
        
        for i in range(len(newNode) - 1):
            newNode[i].next = newNode[i+1]
        
        newNode[-1].next = None
        return None