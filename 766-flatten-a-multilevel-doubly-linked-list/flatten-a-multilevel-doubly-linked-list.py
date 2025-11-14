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
        prev = dummy
        while stack:
            curr = stack.pop()
            prev.next = curr
            if curr.next: stack.append(curr.next)
            if curr.child: stack.append(curr.child)
            curr.child = None
            curr.prev = prev
            prev = curr
        head.prev = None
        return dummy.next
    # T: O(n), S: O(n)
