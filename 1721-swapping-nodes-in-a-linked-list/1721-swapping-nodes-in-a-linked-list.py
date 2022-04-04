# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = pre_right = pre_left = ListNode(next=head)
        
        right = left = head
        
        
        # Assuming we have the LL as 1->2->3
        # we need to go k=3. 
        # first iteration pre_left=1, left=2
        # second iteration pre_left=2, left = 3
        for _ in range(k-1):
            pre_left = left
            left = left.next
            
        end = left
        
        # assuming we need to stop at k=3 from end
        # assuming our ll is 5->6->7->8 from the end
        # as we stop at 8, we need to have pointer just before k nodes. hence use end.next
        while end.next:
            pre_right = right
            right = right.next
            end = end.next
            
        if left == right: return head
        
        pre_left.next, pre_right.next = right, left
        right.next, left.next = left.next, right.next
        return dummy.next
            
        