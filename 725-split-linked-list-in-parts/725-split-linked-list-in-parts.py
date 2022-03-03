# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # finding length of the linkedlist
        def _length(head):
            count = 0
            while head is not None:
                count += 1
                head = head.next
                
            return count
        
        list_size = _length(head)
        # size of each part
        # extra size of each part (only front ones get 1 extra node, for the remainder)
        part_size, rem_size = list_size//k, list_size%k
        ans = []
        
        while head is not None:
            curr_size = part_size
            # adding 1 extra for the front nodes
            if rem_size > 0:
                rem_size -= 1
                curr_size += 1
                
            ans.append(head)
            
            # now lets break after curr_size nodes
            for _ in range(curr_size-1):
                head = head.next
                
            # we are already at end of the LL. Hence time to break and add empty None elements. 
            if head==None: break
            
            # if not head.next=None means breaking the list
            # head = head.next meaning, for the next iteration to continue from the head.next element. 
            head.next, head = None, head.next
            
        # adding empty none elements. 
        while len(ans)<k: ans.append(None)
        return ans
            