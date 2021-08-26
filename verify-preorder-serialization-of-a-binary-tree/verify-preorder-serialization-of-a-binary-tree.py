class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        normal nodes will:
        1. occupy one place.
        2. creates 2 slots, for 2 child nodes.
        
        Empty nodes will:
        1. occupy one place. 
        """
        
        p = preorder.split(",")
        
        # for the root node
        slot = 1
        
        for node in p:
            # if we have an empty slot and trying to insert a node means pre-order traversal is wrong. 
            if slot==0: return False
            
            if node=="#": slot-=1
            else: slot+=1 # (Also same as -1+2)
                
        # in the end we should not have any empty slots. 
        return slot==0