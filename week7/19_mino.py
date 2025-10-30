# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        current = head
        while current != None:
            current = current.next
            total += 1

        target = total - n
        # print(total, target)
        current = head
        while target > 1:
            current = current.next
            target -= 1

        if target == 0:
            head = head.next
            return head

        current.next = None if current.next == None else current.next.next
        return head

        