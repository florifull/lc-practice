# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if not head.next and n == 1: return None

        dummy = ListNode()
        dummy.next = head
        l, r = dummy, head
        windowDistance = 1
        while r and windowDistance < n:
            windowDistance += 1
            r = r.next
        # get to end of LL
        while r and r.next:
            l, r = l.next, r.next
        l.next = l.next.next
        return dummy.next