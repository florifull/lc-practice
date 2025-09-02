# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse l1
        l1Array = []
        tmp1 = l1
        while tmp1:
            l1Array.append(str(tmp1.val))
            tmp1 = tmp1.next
        l2Array = []
        tmp2 = l2
        while tmp2:
            l2Array.append(str(tmp2.val))
            tmp2 = tmp2.next
        # l1 and l2 vals are contained within our arrays
        ourSum = int(''.join(l1Array[::-1])) + int(''.join(l2Array[::-1]))
        ourArraySum = [int(_) for _ in str(ourSum)]
        dummy = ListNode()
        prev = dummy
        for i in range(len(ourArraySum) - 1, -1, -1):
            curr = ListNode(ourArraySum[i])
            prev.next = curr
            prev = curr
        return dummy.next