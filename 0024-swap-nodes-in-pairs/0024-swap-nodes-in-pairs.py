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
            prev, new_tail = None, node
            
            for _ in range(k):
                if curr:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                else:
                    break
            
            # curr is next element
            # prev is new_head
            # new_tail is new_tail
            return curr, prev, new_tail
        
        k = 2
        curr = head
        dummy = prev = ListNode(None, head)
        
        while curr:
            next_, new_head, new_tail = rev_k_nodes(curr, k)
            prev.next = new_head
            new_tail.next = next_
            prev = curr
            curr = next_
            
        prev.next = curr
        return dummy.next