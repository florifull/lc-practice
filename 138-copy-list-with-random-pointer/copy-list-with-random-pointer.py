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
        originalNodes = collections.defaultdict(list)
        ptr = head
        # traverse og LL, add mapping (node : [newNode, node.next, node.random])
        while ptr:
            originalNodes[ptr].extend([Node(ptr.val), ptr.next, ptr.random])
            ptr = ptr.next

        ogPtr = head
        while ogPtr:
            freshNode, nextPtr, randomPtr = originalNodes[ogPtr]
            # extract new node object for each of the original nodes
            if nextPtr:
                freshNode.next = originalNodes[nextPtr][0]
            if randomPtr:
                freshNode.random = originalNodes[randomPtr][0]
            # move on
            ogPtr = ogPtr.next
        return originalNodes[head][0]