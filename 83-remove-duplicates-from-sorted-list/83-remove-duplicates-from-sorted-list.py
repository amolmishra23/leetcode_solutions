# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        
        while curr and curr.next:
            if curr.val != curr.next.val: curr = curr.next
            else: curr.next = curr.next.next
        
        return head