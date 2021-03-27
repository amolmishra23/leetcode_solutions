# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before, after = ListNode(None), ListNode(None)
        before_copy, after_copy = before, after
        temp = head
        
        while temp:
            if temp.val < x:
                before.next = temp
                before = before.next
            else:
                after.next = temp
                after = after.next
            temp = temp.next
            
        
        after.next = None
        before.next = after_copy.next
        
        return before_copy.next