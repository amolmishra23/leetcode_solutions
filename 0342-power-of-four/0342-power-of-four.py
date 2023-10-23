class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        We need to find the bit manupulation logic for solving this
        Lets try a few random examples, and find some common pattern
        
             No            Bit_re             SetBitPos       No_of_setBit          Valid_power_of_four
     64         1 0 0 0 0 0 0           7                  1                        True         <= :)
     128        1 0 0 0 0 0 0 0         8                  1                        False        <=2nd Condition fail :(
     18         1 0 0 1 0               5,2                2                        False        <=1st Condition Fail :( 
     32         1 0 0 0 0 0             6                  1                        False        <=2nd Condition fail :
        """
        if n<0: return False
        
        count, last_one_pos = 0, 0
        curr_pos = 0
        
        while n:
            curr_pos += 1
            if n&1:
                count += 1
                last_one_pos = curr_pos
            n = n>>1
            
        return count==1 and (last_one_pos&1)
        