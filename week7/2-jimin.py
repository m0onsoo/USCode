# https://leetcode.com/problems/add-two-numbers/submissions/1816293527/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        temp = 0
        head = ListNode(0, None)
        cur = head
        while l1 or l2:
            if l1 and l2:
                val = cur.val + l1.val + l2.val
            if not l1:
                val = cur.val + l2.val
            if not l2:
                val = cur.val + l1.val
            cur.val = val % 10
            temp = 1 if val >= 10 else 0

            # next digit
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # next node
            if temp == 1 or l1 or l2:
                node = ListNode(temp, None)
                cur.next = node
                cur = node

        return head
