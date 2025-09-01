# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if not head.next and n == 1: return None

        # traverse the LL
        rcounter = 0
        r = head
        while r:
            rcounter += 1
            r = r.next
        # edge case
        if rcounter - n + 1 == 1:
            return head.next
        lcounter = 0
        prev, l = None, head
        while l:
            lcounter += 1
            if rcounter - lcounter + 1 == n:
                prev.next = l.next
            else:
                prev, l = l, l.next
        return head