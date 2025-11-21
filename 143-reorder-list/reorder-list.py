# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return None

        # find middle node (s)
        s, f = head, head.next
        while f and f.next:
            s, f = s.next, f.next.next
        second_half_head = s.next
        s.next = None # split lists
        prev = None
        while second_half_head:
            tmp = second_half_head.next
            second_half_head.next = prev
            prev, second_half_head = second_half_head, tmp
        phead, psecond = head, prev
        while head and prev:
            tmp = head.next
            tmp2 = prev.next
            head.next, prev.next = prev, head.next
            phead, psecond = head, prev
            head, prev = tmp, tmp2