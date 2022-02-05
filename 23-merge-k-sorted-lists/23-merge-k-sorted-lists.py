# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail, k = dummy, len(lists)
        min_heap = []
        
        for i in range(k):
            if lists[i]:
                elem = (lists[i].val, id(lists[i]), lists[i])
                heappush(min_heap, elem)
            
        while min_heap:
            val, _, node = heappop(min_heap)
            tail.next = node
            tail = node
            if node.next:
                heappush(min_heap, (node.next.val, id(node.next), node.next))
                
        return dummy.next