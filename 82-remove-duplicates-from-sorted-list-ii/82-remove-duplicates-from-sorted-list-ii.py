# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Core logic lies around same prev, curr pointers.
    We have a clean(prev) and dirty(curr) list
    We keep checking if curr is equal to next elem. If yes, we traverse all those elements, and ignore them. And finally attach next unique to the prev.
    If the elements are unique, we increment and move normally. Making curr as prev(including it in the clean part). And moving curr by 1. 
    
    One case is, if starting elem itself was repeated. In that case, we need to move head to the 1st clean element. Thats taken care of, in last part of the code. 
    """    

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = curr
                curr = curr.next
            else:
                while (curr.next and curr.val == curr.next.val):
                    curr = curr.next
                curr = curr.next
                if prev: prev.next = curr
                else: head = curr
        
        return head
                