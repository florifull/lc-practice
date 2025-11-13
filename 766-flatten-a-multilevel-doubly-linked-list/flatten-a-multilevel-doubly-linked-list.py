"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dummy = Node()
        dummy.next = head
        stack = [head]
        curr = dummy
        while stack:
            node = stack.pop()
            nxt, child = node.next, node.child
            curr.next, node.prev = node, curr
            node.child = None
            if nxt: stack.append(nxt)
            if child: stack.append(child)
            curr = curr.next
        dummy.next.prev = None
        return dummy.next