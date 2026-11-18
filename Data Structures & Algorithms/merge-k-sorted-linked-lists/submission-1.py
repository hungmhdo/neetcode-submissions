# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        heap = []
        counter = count()

        # Add the first node from each non-empty list
        for node in lists:
            if node is not None:
                heapq.heappush(heap, (node.val, next(counter), node))

        while heap:
            _, _, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next is not None:
                heapq.heappush(
                    heap,
                    (node.next.val, next(counter), node.next)
                )

        curr.next = None
        return dummy.next