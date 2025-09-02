# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1val = 0 if not l1 else l1.val
            l2val = 0 if not l2 else l2.val
            sumVal = l1val + l2val + carry
            
            carry = sumVal // 10 #ex 15 // 10 = 1
            newNodeVal = sumVal % 10

            newNode = ListNode(newNodeVal)
            ptr.next = newNode
            ptr = ptr.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return dummy.next
