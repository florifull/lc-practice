# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        m, f = head, head.next
        while f and f.next:
            m, f = m.next, f.next.next
        # s is now set at middle
        prev = None
        # reverse 2nd half LL
        while m:
            tmp = m.next
            m.next = prev
            prev, m = m, tmp
        # reorder
        l, r = head, prev
        # r will go Null if it passes middle, & even lists l & r will exit if overlap
        while l and r and l != r:
            tmpL, tmpR = l.next, r.next
            l.next = r
            l = tmpL
            r.next = l
            r = tmpR