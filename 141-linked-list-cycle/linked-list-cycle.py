# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow, fast = head, head.next
        while fast.next and fast.next.next:
             if slow == fast: return True
             slow, fast = slow.next, fast.next.next
        return False
    # T: O(n), S: O(1)