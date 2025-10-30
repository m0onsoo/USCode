from typing import Optional
from linked_list import ListNode

# 0ms, 17.74MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a root node before head
        root = ListNode(None)
        root.next = head
        node = head
        
        # 1. calculate the length of the the linked list
        length = 0
        while node:
            length += 1
            node = node.next
        
        # 2. calculate the target index
        target = length - n + 1
        
        # 3. find the target and skip
        node = root
        cnt = 0
        while node and node.next:
            if cnt + 1 == target:
                node.next = node.next.next
                break

            cnt += 1
            node = node.next
        
        return root.next