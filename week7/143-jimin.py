# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 중간 지점 찾기
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 중간 지점부터 뒤집기
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev

        # 합치기
        curr = head
        curr2 = head2
        while curr and curr2:
            head_next = curr.next
            head2_next = curr2.next
            curr.next = curr2
            curr2.next = head_next
            curr = head_next
            curr2 = head2_next

        return head
