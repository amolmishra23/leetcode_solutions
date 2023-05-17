# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        res=0
        
        # Finding middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reversing half of the linked list
        curr_node = slow
        next_node, prev_node = None, None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        # Finding answer in pairs of node
        start, end = head, prev_node
        while start and end and start!=end:
            res = max(res, start.val + end.val)
            start, end = start.next, end.next
        
        return res