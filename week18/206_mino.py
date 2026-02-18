Given the head of a singly linked list, reverse the list, and return the reversed list.

# Given
# a singly linked list

# Goal
# reverse the list

# Constaints
# list.length <= N

# Observations
# Every node points to the next node in a singly linked list
# In order to reverse the list, we need to restructure the linked list from the last element
# Extra memory usage: O(N) -> Use a single list
# We need to know the prev and next node in the array -> iterate the array: for 

# Example
# [1,2,3,4,5] -> [5,4,3,2,1]: [2,1]

# Hint: Think “3 hands”: you need a handle to current, its next, and the previous node you already reversed.

# Approach
# current = head
# prev = None
# next = head.next

# current -> prev => current.next = prev
# prev = current
# current = next
# next = next.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	current, prev, nxt = head, None, head.next
      while current:
        current.next = prev
        prev = current
        current = nxt
        nxt = nxt.next
        
      return prev
        
      next_node = None
      while head:
        temp = head # 1
        head = head.next # 2
        next_node = head.next # 3
        
        head.next = temp # 2->1
        head = next_node # 