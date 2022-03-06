# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    """
    The core logic being, if the linkedlist is 
    3,4,2,-6,1,1,5,-6
    3,7,9,3,4,5,10,4
    
    We store a dict of all values -> nodes mapping
    If we see a value twice, means something in between has sum 0. Hence we remove those elements in between. 
    And directly point prev value, to the next of curr.val
    Basically remove 7,9,3. And directly make the previous 3 point to 4.     
    """
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0, head)
        
        prefix = 0
        lookup = collections.OrderedDict()
        
        while curr:
            prefix += curr.val
            node = lookup.get(prefix, curr)
            
            while prefix in lookup: lookup.popitem()
                
            lookup[prefix] = node
            node.next = curr.next
            curr = curr.next
        
        return dummy.next