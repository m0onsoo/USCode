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
        count, curr = 1, head
        while curr.next != None:
            curr = curr.next
            count += 1

        half_count, middle = (count + 1) // 2, head
        while half_count > 0:
            middle = middle.next
            half_count -= 1
        
        prev, curr = None, middle
        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first_half, second_half = head, prev
        while first_half != None and second_half != None:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next
        
        if first_half is not None:
            first_half.next = None
        
        