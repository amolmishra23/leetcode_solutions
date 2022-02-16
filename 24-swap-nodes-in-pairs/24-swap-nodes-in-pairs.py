# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        
        def rev_k_nodes(node, k):
            curr = node
            # curr now will be traversed the last node in linkedlist. 
            # hence we store it as new_tail
            prev, new_tail = None, curr
            
            for _ in range(k):
                if curr:
                    next_ = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_
                else:
                    break
            
            # curr is next node to traverse
            # prev is the new head of the LL
            # new_tail is the new last node of the LL
            return curr, prev, new_tail
        
        
        k = 2
        curr = head
        dummy = prev = ListNode(None, head)
        
        while curr:
            next_, new_head, new_tail = rev_k_nodes(curr, k)
            new_tail.next = next_
            prev.next = new_head
            prev = new_tail
            curr = next_
            
        prev.next = curr
        return dummy.next