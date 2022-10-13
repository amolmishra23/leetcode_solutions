# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        just cache the next value into node
        and node's next points to next's next pointer. 
        """
        node.val = node.next.val
        node.next = node.next.next