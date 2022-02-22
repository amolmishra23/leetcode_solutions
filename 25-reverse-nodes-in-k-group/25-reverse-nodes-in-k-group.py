# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        
        def has_k_nodes(node, k):
            temp = node
            while node is not None and k:
                node = node.next
                k -= 1
            return k==0
        
        def reverse_k_nodes(curr, k):
            new_tail, prev = curr, None
            
            for _ in range(k):
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
                
            return curr, prev, new_tail
        
        dummy = prev = ListNode(None, head)
        curr = head
        
        while has_k_nodes(curr, k):
            next_, new_head, new_tail = reverse_k_nodes(curr, k)
            prev.next = new_head
            new_tail.next = next_
            prev = new_tail
            curr = next_
            
        prev.next = curr
        return dummy.next