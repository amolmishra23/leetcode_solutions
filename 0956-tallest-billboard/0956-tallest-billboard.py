class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        Very similar to finding subsequence with a particular sum. 
        But here sum could be less than sum(arr)//2
        So, we start with assumption we have left_arr, right_arr. 
        And doing 3 choices. Add to left/add to right/dont add. Via dp. 
        Some combination should come where we have perfect match. 
        """
        @lru_cache(None)
        def solve(idx, diff):
            if idx == len(rods): return 0 if diff==0 else float("-inf")
            
            options = []
            
            options.append(rods[idx] + solve(idx+1, diff + rods[idx]))
            options.append(rods[idx] + solve(idx+1, diff - rods[idx]))
            options.append(solve(idx+1, diff))
            
            return max(options)
        
        return solve(0, 0)//2