# Given
# a linked list
# head

# Goal
# determine if there's a cycle in the linked list
# A cycle exists if a node can be reached again by following the next pointer

# Constraints
# linkedList.length <= 1000
# No constraints on memery usage -> up to O(N)

# Example
# [1,2,3,null] -> False
# [1,2,3,1] -> true

# Approach
# Two pointers - slow and fast pointers
# The fast pointer moves twice each time whereas the slow pointer one step each time
# If they meet at a certain node, a cycle exists
# If the slow pointer reaches the end of the linked list, return false

# Input / Output
# Input: ListNode
# Output: bool

# TC: O(N)
# SC: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast_pointer, slow_pointer = head.next.next, head.next
  
        while fast_pointer:
            
            if fast_pointer == slow_pointer:
                return True
            
            if not fast_pointer.next:
                break
            
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return False
