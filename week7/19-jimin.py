# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# two-pass : 끝까지 읽어서 몇개 있는지 확인하고 len-n번째 있는 항목 지우기
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode(0, head)
        cur = dummy

        for _ in range(length - n):
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next
