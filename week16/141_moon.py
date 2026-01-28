# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 47ms, 22.85MB
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # visited = set()
        # node = head
        # while node and node.next:
        #     if node not in visited:
        #         visited.add(node)
        #         node = node.next
        #     else:
        #         return True
        
        # return False

        slow, fast = head, head
        while slow and slow.next and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False