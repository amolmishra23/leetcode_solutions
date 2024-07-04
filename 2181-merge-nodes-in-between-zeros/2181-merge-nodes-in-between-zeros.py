# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = res_head = ListNode(None)

        while head:
            head = head.next
            curr_sum = 0
            while head and head.val != 0:
                curr_sum += head.val
                head = head.next
            if curr_sum:
                res_head.next = ListNode(curr_sum)
                res_head = res_head.next
            
        return tmp.next
            
            
        