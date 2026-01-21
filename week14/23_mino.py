# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        answer = None
        curr = answer
        k = len(lists)

        for i in range(k):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next

        while pq:
            head, node_index = heapq.heappop(pq)

            if not answer:
                answer = ListNode(head)
                curr = answer
            else:
                # print(answer , curr)
                curr.next = ListNode(head)
                curr = curr.next
            
            if lists[node_index]:
                heapq.heappush(pq, (lists[node_index].val, node_index))
                lists[node_index] = lists[node_index].next
            
        return answer
        