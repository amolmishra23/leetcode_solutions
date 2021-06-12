class Solution:
    def minSteps(self, n: int) -> int:
        """
        In case of 1, we already have it on screen, hence answer is 0
        In case of 2, we copy once, and paste once. Hence answer is 2. 
        """
        if n==1: return 0
        if n==2: return 2
        
        prev = [None]*(n+1)
        prev[1], prev[2] = 0, 2
        
        """
        Even for 3, its 3 operations, simple. 
        But for higher numbers, to perform copy paste, it needs to be a multiple, to paste exactly that many times.
        Hence we find all the multiples of that number, and check is it worth using that multiple, and pasting the multiple required times. Like for 9, we can get to 3. And copy 3, and pasten 3,3. Hence we have 9. 
        """
        for i in range(3, n+1):
            prev[i] = i
            # finding all the multiples of i. 
            # for 12, the multiples are 6, 4, 3, 2. Hence we try to find by pasting of all the possible multiples. 
            for j in range(i//2, 0, -1):
                # if a number perfectly divides it
                if (i%j==0): prev[i] = min(prev[i], prev[j]+i//j)
                    
        return prev[n]