class Solution:
    def minSteps(self, n: int) -> int:
        @functools.lru_cache(None)
        def solve(n):
            """
            In case of 1, we already have it on screen, hence answer is 0
            In case of 2, we copy once, and paste once. Hence answer is 2. 
            """
            if n==1: return 0
            if n==2: return 2
            
            """
            Even for 3, its 3 operations, simple. 
            But for higher numbers, to perform copy paste, it needs to be a multiple, to paste exactly that many times.
            Hence we find all the multiples of that number, and check is it worth using that multiple, and pasting the multiple required times. Like for 9, we can get to 3. And copy 3, and pasten 3,3. Hence we have 9. 
            
            To get 9, we can also put 3 in 3 steps.
            Then we copy the 3, and paste it twice. Hence 6 steps
            """
            for i in range(2, int(math.sqrt(n))+1):
                if n%i==0: return i+solve(n//i)
                
            return n
        
        return solve(n)