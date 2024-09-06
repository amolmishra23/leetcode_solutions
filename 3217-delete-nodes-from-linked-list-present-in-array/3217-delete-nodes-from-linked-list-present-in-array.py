# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nums = ListNode("a"), set(nums)
        res = prev
        curr = head
        
        while curr:
            if curr.val in nums:
                curr = curr.next
            else:
                next_ = curr.next
                curr.next = None
                prev.next = curr
                prev = curr
                curr = next_
            
        return res.next