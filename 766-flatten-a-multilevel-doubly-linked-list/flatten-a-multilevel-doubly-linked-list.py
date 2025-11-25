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
        prev = dummy
        stack = [head]
        while stack:
            node = stack.pop()
            if node.next: stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
            node.prev = prev
            prev.next = node
            prev = node
        head.prev = None
        return dummy.next
    # T: O(n), S:O(n)