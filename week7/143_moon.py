from typing import Optional
from linked_list import ListNode

# 0ms, 23.44MB

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
        slow, fast, prev = head, head, ListNode(None)
        while fast and fast.next:
            fast = fast.next.next

            prev = slow
            slow = slow.next
        
        l2 = prev.next
        prev.next = None
        l1 = head

        # reverse l2
        prev, node = None, l2
        while node:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_

            """
            # 2줄로 처리 가능
            next, node.next = node.next, prev
            prev, node = node, next
            """

        l2 = prev
        while l1 and l1.next and l2 and l2.next:
            next_ = l1.next
            l1.next = l2
            l2 = l2.next # l2 미리 옮겨줌

            l1.next.next = next_
            l1 = l1.next.next

        # 다 끝나고 홀수개수였을때 l2가 남게됨. 뒤에 붙여주기만 하면 됨
        if l2:
            l1.next = l2

  