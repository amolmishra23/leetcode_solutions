# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy, min_heap = ListNode(0), []
        tail = dummy
        
        for l in lists:
            if l:
                elem = (l.val, id(l), l)
                heappush(min_heap, elem)
            
        while min_heap:
            val, _, node = heappop(min_heap)
            tail.next = node
            tail = tail.next
            
            if node.next:
                heappush(min_heap, (node.next.val, id(node.next), node.next))
                
        return dummy.next
            