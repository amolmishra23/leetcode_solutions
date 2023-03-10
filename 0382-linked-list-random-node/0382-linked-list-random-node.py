# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        curr, counter, res = self.head, 1, -1
        
        while curr is not None:
            if random()<1/counter:
                res = curr.val
            curr = curr.next
            counter += 1
            
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()