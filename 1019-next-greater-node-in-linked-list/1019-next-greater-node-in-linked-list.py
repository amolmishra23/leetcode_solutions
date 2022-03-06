# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        We cannot do it the normal aditya verma way
        because its linkedlist and cant iterate backwards. 
        
        So, we kepe iterating forwards, and everytime we find some big element during iteration, and keep popping from stack
        We keep setting the next greater element, as current element. 
        This is the hack to do it for linkedlists
        """
        result, stk = [], []
        
        while head:
            while stk and stk[-1][1]<head.val: # as soon as we find a bigger element, we replace next bigger element for all previous elements in the stack
                result[stk.pop()[0]] = head.val
            stk.append([len(result), head.val]) # alias to i or counter variable here
            result.append(0)
            head = head.next
        
        return result