"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        def copyNode(node):
            if node in dic:
                return dic[node]
            if not head:
                return None
            else:
                newNode = Node(node.val)
                dic[node] = newNode
                if node.next != None:
                    newNode.next = copyNode(node.next)
                
                if node.random != None:
                    newNode.random = copyNode(node.random)
                
                return newNode
        
        return copyNode(head)
