# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            # when the input lists is empty
            return None
        if len(lists) == 1:
            return lists[0]

        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]):
            if l1 is None or (l2 and l1.val > l2.val):
                # swap
                l1, l2 = l2, l1
            
            if l1 is None:
                return l2
            
            l1.next = mergeTwoLists(l2, l1.next)

            return l1

        result = lists[0]
        while len(lists) > 1:
            # exits when all the lists is merged into one list
            l_ = lists.pop()
            result = mergeTwoLists(result, l_)
        
        return result