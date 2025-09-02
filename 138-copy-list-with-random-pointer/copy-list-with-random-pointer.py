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
        if not head: return None
        oldToNew = {}
        ptr = head
        while ptr:
            oldToNew[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            newNode = oldToNew[ptr]
            newNode.next = None if not ptr.next else oldToNew[ptr.next]
            newNode.random = None if not ptr.random else oldToNew[ptr.random]
            ptr = ptr.next
        return oldToNew[head]