# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value, curr, carry = 0, ListNode(), 0
        head = curr
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next

            curr.val = carry % 10
            carry //= 10

            if l1 or l2 or carry:
                curr.next = ListNode()
                curr = curr.next
        
        return head